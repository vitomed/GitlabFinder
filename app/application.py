from app import db
from app.models import Projects


class Storage:

    @classmethod
    def commit(cls, response):

        for element in response:

            project_id = element["id"]
            name = element["name"]
            description = element["description"]
            last_activity = element["last_activity_at"]

            if db.session.query(Projects).get(project_id):
                continue
            else:
                project = Projects(project_id=project_id, description=description,
                                   name=name, last_activity=last_activity)
                db.session.add(project)

            db.session.commit()

        return "Ok"

    @classmethod
    def get_data(cls):
        columns = Projects.metadata.tables["projects"].columns.keys()

        projects = db.session.query(Projects.project_id,
                                    Projects.description,
                                    Projects.name,
                                    Projects.last_activity,
                                    Projects.created_at).all()

        response = [dict(zip(columns, lst)) for lst in projects]

        return response
