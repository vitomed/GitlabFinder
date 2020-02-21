from typing import List

from app import db
from app.models import Project


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
            if db.session.query(Project).get(project_id):
                continue
            else:
                p = Project(project_id=project_id, description=description,
                            name=name, last_activity=last_activity)
                projects.append(p)

        db.session.add_all(projects)
        identity = db.session.new
        db.session.commit()

        resp = f"{len(identity)} new repositories added" \
            if identity else "Added nothing repositories!"

        return resp

    @classmethod
    def view_projects(cls) -> List:
        columns = Project.metadata.tables["project"].columns.keys()

        projects = db.session.query(Project.project_id,
                                    Project.description,
                                    Project.name,
                                    Project.last_activity,
                                    Project.created_at).all()

        response = [dict(zip(columns, lst)) for lst in projects]

        return response
