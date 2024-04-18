from flask import Blueprint, render_template

from app.models import EditableHTML

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/project1')
def project1():
    return render_template('main/project1.html')

@main.route('/project2')
def project2():
    return render_template('main/project2.html')

@main.route('/project3')
def project3():
    return render_template('main/project3.html')


@main.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
