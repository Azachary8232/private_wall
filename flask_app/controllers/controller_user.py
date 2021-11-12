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
    print("?????")
    if not User.validate_user(request.form):
        return redirect('/')
    print("222222")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    print("9999999")
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/wall')


#     User Login to Wall
@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    data = { 
        "email" : request.form["email"] 
        }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", category= "login_email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", category= "login_password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/wall")




#   Logout to '/'
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')