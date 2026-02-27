#!/usr/bin/env python3
"""Crée des issues GitHub pour chaque test pytest en échec.

Lance la suite de tests avec rapport JUnit, parse les échecs, puis appelle
`gh issue create` pour chaque test qui a échoué (titre, description,
étapes de reproduction, assignation). Évite de créer une issue en double
si une issue ouverte existe déjà avec le même titre.

Usage (depuis la racine du projet TP3---LOG3000) :
    python scripts/create_issues_from_test_failures.py
    python scripts/create_issues_from_test_failures.py --assignee membre-equipe
    python scripts/create_issues_from_test_failures.py --dry-run

Prérequis : GitHub CLI (gh) installé et authentifié (gh auth login).
"""

import argparse
import os
import subprocess
import sys
import xml.etree.ElementTree as ET


# Fichier de rapport JUnit généré par pytest
JUNIT_FILE = "test-results.xml"


def run_pytest(project_root: str) -> bool:
    """Lance pytest avec sortie JUnit. Retourne True si au moins un test a échoué."""
    env = os.environ.copy()
    env["PYTHONPATH"] = project_root
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "tests/",
        "-v",
        f"--junitxml={JUNIT_FILE}",
    ]
    result = subprocess.run(cmd, cwd=project_root, env=env, capture_output=True, text=True)
    return result.returncode != 0


def parse_failures(junit_path: str) -> list[dict]:
    """Parse le fichier JUnit et retourne la liste des tests en échec.

    Chaque élément contient : test_id (nom du test), classname, message, body (extrait).
    """
    failures = []
    tree = ET.parse(junit_path)
    root = tree.getroot()
    for suite in root.findall("testsuite"):
        for tc in suite.findall("testcase"):
            failure = tc.find("failure")
            if failure is None:
                continue
            test_id = tc.get("classname", "") + "::" + tc.get("name", "")
            message = (failure.get("message") or "").strip()
            body_text = (failure.text or "").strip()
            failures.append({
                "test_id": test_id,
                "classname": tc.get("classname", ""),
                "name": tc.get("name", ""),
                "message": message,
                "body": body_text[:1000] if body_text else message,
            })
    return failures


def issue_exists_with_title(project_root: str, title: str) -> bool:
    """Vérifie si une issue ouverte existe déjà avec ce titre (évite doublons)."""
    # Recherche par partie du titre (nom du test) pour éviter problèmes d'échappement
    search = title.replace("[Bogue] Test en échec : ", "").strip()[:50]
    result = subprocess.run(
        ["gh", "issue", "list", "--state", "open", "--search", search, "--json", "number"],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return False
    try:
        import json
        data = json.loads(result.stdout)
        return len(data) > 0
    except Exception:
        return False


def create_issue(project_root: str, failure: dict, assignee: str | None, dry_run: bool) -> bool:
    """Crée une issue GitHub pour un test en échec. Retourne True en cas de succès."""
    title = f"[Bogue] Test en échec : {failure['name']}"
    if len(title) > 80:
        title = title[:77] + "..."
    assignee_note = f"\n- **Assignation** : cette issue est assignée à un membre de l'équipe (via `--assignee`).\n" if assignee else ""
    body = f"""## Description du problème

Le test **`{failure['name']}`** échoue. Comportement observé vs attendu (voir message d’assertion ci‑dessous).

- **Identifiant du test** : `{failure['test_id']}`
- **Message d’échec** : {failure['message'] or '(aucun)'}
{assignee_note}

## Étapes de reproduction / Cas de test en échec

Depuis la racine du projet (`TP3---LOG3000`) :

```bash
pytest {failure['test_id']} -v
```

Le test ci‑dessus doit être corrigé sur une **branche dédiée**, puis validé par un commit dont le message explique comment la modification corrige le problème. Voir le [flux de contribution](README.md#flux-de-contribution) dans le README.

## Détails techniques (trace)

```
{failure['body']}
```
"""
    if dry_run:
        print(f"[DRY-RUN] Création issue : {title}")
        return True
    if issue_exists_with_title(project_root, title):
        print(f"Issue déjà existante, ignorée : {title}")
        return True
    import tempfile
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(body)
        body_file = f.name
    try:
        args = ["gh", "issue", "create", "--title", title, "--body-file", body_file]
        if assignee:
            args.extend(["--assignee", assignee])
        args.extend(["--label", "bug"])
        result = subprocess.run(args, cwd=project_root, capture_output=True, text=True)
    finally:
        os.unlink(body_file)
    if result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        return False
    print(f"Issue créée : {title}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Crée des issues GitHub pour les tests en échec.")
    parser.add_argument("--assignee", default=None, help="Assigner les issues à ce compte (ex. @me ou username)")
    parser.add_argument("--dry-run", action="store_true", help="Ne pas créer d’issues, seulement afficher")
    parser.add_argument("--project-root", default=None, help="Racine du projet (défaut : répertoire courant)")
    parser.add_argument("--junit-file", default=None, help="Utiliser ce rapport JUnit au lieu de lancer pytest")
    args = parser.parse_args()
    project_root = args.project_root or os.getcwd()
    junit_path = args.junit_file or os.path.join(project_root, JUNIT_FILE)

    if not args.junit_file:
        print("Lancement des tests...")
        has_failures = run_pytest(project_root)
    else:
        has_failures = True
    if not os.path.isfile(junit_path):
        print("Rapport JUnit non généré. Vérifiez que pytest s’exécute correctement.", file=sys.stderr)
        return 2
    failures = parse_failures(junit_path)
    if not failures:
        print("Aucun test en échec.")
        return 0 if not has_failures else 1
    print(f"{len(failures)} test(s) en échec. Création des issues...")
    ok = 0
    for f in failures:
        if create_issue(project_root, f, args.assignee, args.dry_run):
            ok += 1
    return 0 if ok == len(failures) else 3


if __name__ == "__main__":
    sys.exit(main())
