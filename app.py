from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Calcule le résultat d'une expression arithmétique simple.

    L'expression doit être une chaîne de la forme ``<nombre><opérateur><nombre>``,
    où l'opérateur est l'un de ``+``, ``-``, ``*`` ou ``/``. Un seul opérateur
    est autorisé et les espaces éventuels sont ignorés.

    :param expr: Expression saisie par l'utilisateur.
    :raises ValueError: Si l'expression est vide, mal formée ou contient des
        opérandes non numériques.
    :return: Le résultat numérique de l'opération.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On recherche exactement un seul opérateur binaire dans l'expression
    # normalisée, afin de limiter la calculatrice à des expressions simples.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    # On impose que les deux opérandes soient des nombres réels.
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et traite la soumission du formulaire.

    - En GET : affiche simplement la page avec un résultat vide.
    - En POST : lit l'expression transmise par le formulaire, appelle
      ``calculate`` et injecte le résultat (ou un message d'erreur)
      dans le template ``index.html``.

    :return: Le rendu HTML de la page principale.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)