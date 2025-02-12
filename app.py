from flask import Flask, request, render_template, url_for

app = Flask(__name__)

'''
Basic application that takes a name from a form a greets the user with a message.

'''
@app.route('/', methods=['GET', 'POST'])
def index():
    greeting = ""
    if request.method == 'POST':
        name = request.form.get('name')
        greeting = f"Hello, {name}!, Welcome to our website!"
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug = True)

'''
Added to GitHub, verify at: https://github.com/Sshieldsmma/BasicFlaskWebsite

'''