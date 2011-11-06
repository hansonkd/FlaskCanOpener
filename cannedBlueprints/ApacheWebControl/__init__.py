from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

url_prefix = 'apacheControl'
blueprint_control = Blueprint('apache_control', __name__)

@blueprint_control.route('/', defaults={'page': 'index'})
@blueprint_control.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        return "pow"
        abort(404)