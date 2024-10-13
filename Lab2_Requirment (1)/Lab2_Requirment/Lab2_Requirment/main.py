from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    mail = request.form['mail']
    return render_template('result.html', name=name, mail=mail)

if __name__ == '__main__':
    app.run(debug=True)
