from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('desarrollador.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)