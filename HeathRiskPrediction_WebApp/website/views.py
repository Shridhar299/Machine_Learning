from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template('base.html')


@views.route("/heart")
def heart():
    return render_template('heart_index.html')


@views.route("/heart_form")
def heart_form():
    return render_template('heart.html')
