from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://darkabout.xyz/desarrollador")

@app.route('/desarrollador')
def desarrollador():
    return render_template('desarrollador.html')

if __name__ == '__main__':
    app.run(debug=True)