import os
from flask import jsonify, render_template, request, redirect, url_for
from app import app, gl
from .application import Storage


@app.route('/', methods=["GET"])
@app.route('/search/', methods=['POST', 'GET'])
def search():
    if request.method == "POST":
        row = request.form.get("row")
        return redirect(url_for('send', search=row))
    return render_template("form.html")


@app.route('/projects/')
def send():
    row = request.args.get('search', '')
    response = gl.search('projects', row)
    res = Storage.commit(response)
    return res


@app.route('/storage/', methods=["GET"])
def get_storage():
    response = Storage.get_data()
    return jsonify(response)
