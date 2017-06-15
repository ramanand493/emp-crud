from crud import app, db
from crud.models import crud_model
from flask import render_template, request, redirect, url_for, session
import os

app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template("view.html")

@app.route('/view')
def d_view():
    data = crud_model.Emp.query.all()
    return render_template("view.html", data=data)
