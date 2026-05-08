from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mysqldb import MySQL
from random import choice

app = Flask(__name__)

########## CONEXAO ##########

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'alunofatec'
app.config['MYSQL_DB'] = 'Portas_Abertas'

bd = MySQL(app)

### Obter lista de mensagens ao iniciar o programa ###

mensagens = []

def obter_mensagens():
    global mensagens
    with open('frases.txt', 'r', encoding='UTF-8') as f:
        mensagens = f.read().splitlines()

########## ROTAS ##########

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        escolaridade = request.form['escolaridade']
        interesses = request.form.getlist('areas[]')
        cursor = bd.connection.cursor()
        cursor.execute(
            "INSERT INTO Visitantes(nome, email, telefone, escolaridade) VALUES (%s, %s, %s, %s);",
            (nome, email, telefone, escolaridade)
        )
        visitante_id = cursor.lastrowid
        for interesse in interesses:
            cursor.execute(
                "INSERT INTO Interesses (visitante_id, interesse) VALUES (%s, %s)",
                (visitante_id, interesse)
            )
        bd.connection.commit()
        cursor.close()
        return redirect(url_for('oraculo'))
    return render_template('index.html')

@app.route('/oraculo')
def oraculo():
    global mensagens
    return render_template('oraculo.html', mensagem=choice(mensagens))

########### EXECUTAR ##########

obter_mensagens()

if __name__ == '__main__':
    app.run(debug=True)
