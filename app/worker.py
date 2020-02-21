from typing import List

from app import db
from app.models import Project


class Worker:

    @classmethod
    def send(cls, dictionaries: List) -> str:

        """The method gets a list of dictionaries, checks
        whether the given id exists in the Project table.
        If there is no entry, then save it to the database. Result
        return will be a string with information about the quantity
        table entries
        
        : param dictionaries: list of found repositories with
        projects in the form of a dictionary with parameters
        : return: number of records stored in the table
        """
        projects = []
        for dct in dictionaries:
            try:
                project_id = dct["id"]
                name = dct["name"]
                description = dct["description"]
                last_activity = dct["last_activity_at"]
            except KeyError as exc:
                raise KeyError("Неверный ключ", exc)
            already_exist = db.session.query(Project).get(project_id)
            if already_exist:
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
        """
        Returns all records from the database, converting them
        to the dictionary

        : return: dictionaries containing the desired projects,
        obtained from the database.
        """
        columns = Project.metadata.tables["project"].columns.keys()

        projects = db.session.query(Project.project_id,
                                    Project.description,
                                    Project.name,
                                    Project.last_activity,
                                    Project.created_at).all()

        zippy = [dict(zip(columns, row)) for row in projects]

        return zippy
