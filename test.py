from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    data = request.form['data']
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
