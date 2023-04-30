from flask import Flask, render_template, redirect, request, flash
# Vamos importar o email e capturar a mensagem
from flask_mail import Mail, Message 
# importando o a página config com os dados email e senha
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

# para enviar o email, precisamos configurar o app.secret_key que fará com o flask criptografe algumas transições externas que estiverem no projeto
app.secret_key = "Robs3110"
 
# adicionando configurações do email gmail
# vamos criar uma página config.py para configurar os dados de entrada do email.

mail_settings={
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA")
}

app.config.update(mail_settings)

mail = Mail (app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


@app.route('/') # para renderizar a págigina devemos criar uma rota que será chamada /

# toda rota é seguida de uma função
def index(): # a função index() retorna a renderização da página index.html
    
    return render_template('index.html')

# criando uma rota de envio

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )

        msg = Message(
                subject = f'{formContato.nome} te enviou uma mensagem no portfólio.',
                sender = app.config.get("MAIL_USERNAME"),
                recipients = ['robsonpdemoraes.dev@hotmail.com', app.config.get("MAIL_USERNAME")],
                body = f'''
                
                    {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

                    {formContato.mensagem}

                '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

if __name__ == '__main__': #Se o nome do arquivo for main, roda o app.run()
    app.run(debug=True)
    # debug=True faz com que a página seja atualizada automaticamente