from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mysqldb import MySQL
from random import choice

app = Flask(__name__)

########## CONEXAO ##########

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'leo-dev'
app.config['MYSQL_PASSWORD'] = 'senha-segura'
app.config['MYSQL_DB'] = 'Portas_Abertas'

bd = MySQL(app)

### Obter lista de mensagens ao iniciar o programa ###
# reduz a consulta ao banco sempre que for exibir uma mensagem

mensagens = []

def obter_mensagens():
    global mensagens
    with app.app_context():
        cursor = bd.connection.cursor()
        cursor.execute("SELECT mensagem FROM Mensagens")
        mensagens = [msg[0] for msg in cursor.fetchall()]
        cursor.close()

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


'''
@app.route('/cadastro', methods=['POST'])
def cadastrar():
    infos = request.get_json()
    cursor = bd.connection.cursor()
    cursor.execute(
        "INSERT INTO Visitantes(nome, email, telefone, escolaridade, interesse) VALUES (%s, %s, %s, %s, %s);",
        (infos.get('nome'), infos.get('email'), infos.get('telefone'), infos.get('escolaridade'), infos.get('interesse'))
    )
    bd.connection.commit()
    novo_id = cursor.lastrowid
    cursor.close()
    return jsonify({"mensagem": f"Visitante cadastrado com id {novo_id}!"}), 201

@app.route('/oraculo', methods=['GET'])
def oraculo():
    mensagem = choice(mensagens)[0]
    return jsonify({'mensagem': mensagem})
'''

########### EXECUTAR ##########

obter_mensagens()

if __name__ == '__main__':
    app.run(debug=True)