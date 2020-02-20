from typing import List

from app import db
from app.models import Projects


class Worker:

    @classmethod
    def commit(cls, dictionaries: List) -> str:
        projects = []
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
                p = Projects(project_id=project_id, description=description,
                                   name=name, last_activity=last_activity)
                projects.append(p)

        db.session.add_all(projects)
        identity = db.session.new
        db.session.commit()

        return f"{len(identity)} new repositories added" if identity else "Added nothing repositories!"

    @classmethod
    def view_projects(cls) -> List:
        columns = Projects.metadata.tables["projects"].columns.keys()

        projects = db.session.query(Projects.project_id,
                                    Projects.description,
                                    Projects.name,
                                    Projects.last_activity,
                                    Projects.created_at).all()

        response = [dict(zip(columns, lst)) for lst in projects]

        return response
