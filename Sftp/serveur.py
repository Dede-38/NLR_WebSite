from flask import Flask, render_template, jsonify
import paramiko

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Connexion SFTP
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("www.nlresport.fr", username="nlruser", password="8awCt6XrRy")

    sftp = ssh.open_sftp()
    with sftp.file("/var_www_html/NLR/fichier.txt", 'r') as file:
        content = file.read().decode()

    sftp.close()
    ssh.close()
    return jsonify({"content": content})

if __name__ == '__main__':
    app.run(debug=True)
