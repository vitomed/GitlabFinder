from typing import List
from sqlalchemy.exc import IntegrityError
from app import db
from app.models import Projects


class Storage:

    @classmethod
    def commit(cls, dictionaries) -> str:
        for dct in dictionaries:
            try:
                project_id = dct["id"]
                name = dct["name"]
                description = dct["description"]
                last_activity = dct["last_activity_at"]
            except KeyError as exc:
                raise KeyError("Неверный ключ", exc)
            if db.session.query(Projects).get(project_id):
                continue
            else:
                project = Projects(project_id=project_id, description=description,
                                   name=name, last_activity=last_activity)
                db.session.add(project)
        db.session.commit()
        # print(db.session.new)
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
