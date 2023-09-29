from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('greet.html', username=username)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
