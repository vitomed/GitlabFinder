from flask import jsonify, render_template, request, redirect, url_for
from gitlab.exceptions import GitlabSearchError
from app import app, db, gl
from .application import Storage


@app.route('/base', methods=["GET"])
def base():
    return render_template("base.html"), 200


@app.route('/', methods=["GET"])
@app.route('/search/', methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        row = request.form.get("row")
        return redirect(url_for('send', search=row)), 301
    return render_template("form.html"), 200


@app.route('/projects/')
def send():
    row = request.args.get('search', '')
    if row:
        try:
            response = gl.search('projects', row)
        except GitlabSearchError as err:
            raise GitlabSearchError("Проблемы при обращении к API Gitlab")
        res = Storage.commit(response)
        return res, 200


@app.route('/storage/', methods=["GET"])
def get_storage():
    response = Storage.get_data()
    return jsonify(response), 200


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
