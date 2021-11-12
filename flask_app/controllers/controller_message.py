from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_message


@app.route('/wall')
def wall():

    return render_template('wall.html')
