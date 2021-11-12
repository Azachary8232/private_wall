# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt  #<---- Install to top of controller
bcrypt = Bcrypt(app)

    #  To Home Page
@app.route('/')
def index():
    return render_template('login.html')

#     Create User through Registration Form
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/')

