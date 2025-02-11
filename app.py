from flask import Flask 



app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'hola Mundo'

@app.route('/alumnos')
def getAlumnos():
    return 'aqui van los alumnos'

if __name__ == '__main__':
    app.run(debug=True)