from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = ""
    if request.method == 'POST':
        name = request.form.get('name')
        greeting = f"Hello, {name}!, Welcome to our website!"
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug = True)