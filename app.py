from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from random import choice

app = Flask(__name__)

########## CONEXAO ##########

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'leo-dev'
app.config['MYSQL_PASSWORD'] = 'senha-segura'
app.config['MYSQL_DB'] = 'Portas_Abertas'

bd = MySQL(app)

########## ROTAS ##########

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/oraculo')
def oraculo():
    cursor = bd.connection.cursor()
    cursor.execute("SELECT mensagem FROM Mensagens")
    mensagem = choice(cursor.fetchall())[0]
    cursor.close()
    return render_template('oraculo.html', mensagem=mensagem)

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        curso = request.form['curso']
        cursor = bd.connection.cursor()
        cursor.execute(
            "INSERT INTO Visitantes(nome, email, curso) VALUES (%s, %s, %s)",
            (nome, email, curso)
        )
        bd.connection.commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('cadastro.html')

########### EXECUTAR ##########

if __name__ == '__main__':
    app.run(debug=True)