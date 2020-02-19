import json
from app import app, db, gl
from .models import Projects


@app.route('/search/<string:row>/', methods=['GET'])
def search(row: str):
    response = gl.search('projects', f'{row}')

    for element in response[:]:

        project_id = element["id"]
        name = element["name"]
        description = element["description"]
        last_activity = element["last_activity_at"]

        if db.session.query(Projects).get(project_id):
            continue
        else:
            project = Projects(project_id=project_id, description=description, name=name, last_activity=last_activity)
            db.session.add(project)
        db.session.commit()
    return "Ok"


@app.route('/projects/', methods=["GET"])
def get_projects():
    col = Projects.metadata.tables["projects"].columns.keys()

    projects = db.session.query(Projects.project_id,
                                Projects.description,
                                Projects.name,
                                Projects.last_activity,
                                Projects.created_at).all()

    jsn = json.dumps([dict(zip(col, row)) for row in projects], indent=1, default=str)

    return jsn
