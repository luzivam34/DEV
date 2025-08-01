from flask import Blueprint, render_template

main_bp = Blueprint('main_bp',__name__)

@main_bp.route('/')
@main_bp.route('/homepage')
def index():
    return render_template("index.html")