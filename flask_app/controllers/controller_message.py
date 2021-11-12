from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_message
from flask_app.models.model_user import User


@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/')
    users = User.get_all_users()

    return render_template('wall.html', users = users)
