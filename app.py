from flask import Flask, render_template

app = Flask(__name__)

# Rutas principales
@app.route('/')
@app.route('/portada')
def portada():
    return render_template('index.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/ciencia')
def ciencia():
    return render_template('ciencia.html')

@app.route('/arte')
def arte():
    return render_template('arte.html')

@app.route('/desarrollador')
def desarrollador():
    return render_template('desarrollador.html')

# Página de error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
