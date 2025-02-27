from flask import Flask, render_template

app = Flask(__name__)

@app.route('/desarrollador')
def desarrollador():
    return render_template('desarrollador.html')

if __name__ == '__main__':
    app.run(debug=True)