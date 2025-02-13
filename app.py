from flask import Flask, request, render_template, url_for, session, flash, redirect, get_flashed_messages

app = Flask(__name__)
app.secret_key = "super_secret_stuff"
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

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    feedback_data = ""
    if request.method == 'POST':
        feedback = request.form.get('feedback')
        flash(f"Feedback submitted successfully: {feedback}","success!")
        session['feedback'] = feedback
        return redirect(url_for('feedback_log'))
    return render_template("feedback.html")


@app.route('/feedback_log', methods=['GET', 'POST'])
def feedback_log():
    feedback = session.get('feedback')     
    messages = get_flashed_messages()
    saved_feedback = f"Saved Feedback: {feedback}"
    return render_template("feedback_log.html", saved_feedback=saved_feedback, messages=messages)




if __name__ == '__main__':
    app.run(debug = True)

'''
Added to GitHub, verify at: https://github.com/Sshieldsmma/BasicFlaskWebsite

'''