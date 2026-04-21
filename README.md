# FATEC PORTAS ABERTAS 2026

Pequeno programa para recepcionar os visitantes do evento FATEC PORTAS ABERTAS, fazer o cadastro deles, e exibir uma mensagem de motivação.

## Decisões

A decisão do Python foi baseada na preferência das pessoas que me ajudarão no projeto pela linguagem, mas fico satisfeito pois me dá a oportunidade de me familiarizar com uma tecnologia com a qual eu não tenho tanto contato.
A decisão de utilizar MySQL (MariaDB) foi baseada na familiaridade que eu tenho com esses banco de dados.
Por ser um projeto relativamente simples, escolhi utilizar Flask para exibir as páginas no navegador, me dando a oportunidade de aprender uma tecnologia nova, e de relembrar conceitos de HTML e CSS.
Ainda devido a simplicidade do projeto, toda a lógica do programa (conexão com banco de dados, rotas, etc.) está estruturada em um único arquivo.

## Como utilizar

#### O que é necessário
- Python
- MySQL ou MariaDB

#### Passo a passo
- No diretório de sua preferência, criar um ambiente virtual para o python e ativá-lo
```
python -m venv venv
source venv/bin/activate
```
- No diretório do projeto, instalar as dependências do [requirements.txt](./requirements.txt)
```
pip install -r requirements.txt
```
- Executar o [schema.sql](./schema.sql)
  - Entrar no banco de dados e digitar ```source caminho/do/arquivo/schema.sql;```
  - -ou-
  - (Testado no Linux) No diretório do arquivo do digitar ```mariadb -u [usuario] -p < schema.sql```

- Editar as credenciais no arquivo [app.py](./app.py)
```
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'nome_de_usuario'
app.config['MYSQL_PASSWORD'] = 'senha_do_usuario'
app.config['MYSQL_DB'] = 'Portas_Abertas'
```

- Executar o programa
```
python3 app.py
```
- Ao término, desativar o ambiente virtual do python
```
deactivate
```

