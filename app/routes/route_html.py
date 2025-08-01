from flask import Blueprint, render_template

html_bp = Blueprint('html_bp', __name__)

@html_bp.route('/html')
def html():
    return render_template('html/index_html.html')

@html_bp.route('/tutorial_html')
def tutorial_html():
    return render_template('html/tutorial_html.html')

@html_bp.route('/introducao_html')
def introducao_html():
    return render_template('html/introducao_html.html')