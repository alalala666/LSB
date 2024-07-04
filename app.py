from flask import Flask, render_template, redirect, url_for, request, send_file, session
import secrets
from Least_Significant_Bit import LSB

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    alert_message = session.pop('alert_message', '')
    return render_template('index.html', alert_message=alert_message)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        text = request.form.get('text')
        operation = request.form.get('operation')
        filename = 'uploaded_image.png'
        file.save(filename)
        if operation == 'encrypt':
            LSB.secret(filename, text, 'uploaded_image2.png')
            #session['alert_message'] = 'File encrypted successfully!\n\n'
            return redirect(url_for('download_file', filename='uploaded_image2.png'))
        elif operation == 'decrypt':
            decrypted_text = LSB.get_secret(filename)
            session['alert_message'] = f'{decrypted_text}'
            return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
