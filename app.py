from flask import Flask, render_template, redirect

app = Flask(__name__)
 
@app.route('/') # para renderizar a págigina devemos criar uma rota que será chamada /

# toda rota é seguida de uma função
def index(): # a função index() retorna a renderização da página index.html
    
    return render_template('index.html')

if __name__ == '__main__': #Se o nome do arquivo for main, roda o app.run()
    app.run(debug=True)
    # debug=True faz com que a página seja atualizada automaticamente