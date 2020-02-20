from flask import jsonify, render_template, request, redirect, url_for
from gitlab.exceptions import GitlabSearchError

from app import app, db, gl
from app.worker import Worker


@app.route('/', methods=["GET"])
def base():
    data = request.args.get('data', '')
    return render_template("base.html", data=data), 200


@app.route('/search/', methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        row = request.form.get("row")
        return redirect(url_for('send', search=row)), 301
    return render_template("form.html"), 200


@app.route('/send/')
def send():
    row = request.args.get('search', '')
    if row:
        try:
            response = gl.search('projects', row)
        except GitlabSearchError as exp:
            raise GitlabSearchError("Проблемы при обращении к API Gitlab:", exp)
        res = Worker.commit(response)
        return redirect(url_for('base', data=res)), 301
    return redirect(url_for('base', data="You send empty row!")), 301


@app.route('/projects/', methods=["GET"])
def get_porjects():
    response = Worker.view_projects()
    return jsonify(response), 200


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
