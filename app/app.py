from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'Shannu@7426'  # Your MySQL password
app.config['MYSQL_DB'] = 'e_learning_db'

# Initialize MySQL
mysql = MySQL(app)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')  # Serve mobile.html

@app.route('/laptop')
def laptop():
    return render_template('laptop.html')  # Serve laptop.html

@app.route('/tab')
def tab():
    return render_template('tab.html')  # Serve tab.html

@app.route('/pc')
def pc():
    return render_template('pc.html')  # Serve pc.html

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Placeholder for contact us page

# Sign up, login, and other existing routes remain the same

if __name__ == "__main__":
    app.run(debug=True)
