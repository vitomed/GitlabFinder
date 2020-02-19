from app import app, db, gl
from .models import Projects
from sqlalchemy.exc import IntegrityError as IntegrityAlchemy
from sqlite3 import IntegrityError as IntegritySqlite


@app.route('/search/<string:row>/', methods=['GET'])
def search(row):
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