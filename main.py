from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classificacao_numero', methods=['POST'])
def classificacao_numero():
    try:
        numero = int(request.form['numero'])
        resultado = numero

        diagnostico = []

        if resultado > 0:
            diagnostico.append("positivo")
        elif resultado < 0:
            diagnostico.append("negativo")
        else:
            diagnostico.append("zero")

        if resultado % 2 == 0:
            diagnostico.append("par")
        else:
            diagnostico.append("ímpar")

        diagnostico = ", ".join(diagnostico)

        return render_template('index.html', resultado=resultado, diagnostico=diagnostico)

    except Exception as e:
        resultado = f'Ocorreu um erro {e}'
        diagnostico = ''
        return render_template('index.html', resultado=resultado, diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)