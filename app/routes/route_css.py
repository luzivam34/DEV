from flask import Blueprint, render_template

css_bp = Blueprint('css_bp', __name__)

@css_bp.route('/css')
def css():
    return render_template('css/index_css.html')

@css_bp.route('/tutorial_css')
def tutorial_css():
    return render_template('css/tutorial_css.html')

@css_bp.route('/introducao_css')
def introducao_css():
    return render_template('css/introducao_css.html')