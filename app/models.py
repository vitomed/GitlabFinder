from datetime import datetime
from app import db


class Projects(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, unique=True)
    description = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    last_activity = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"{self.project_id}, {self.description}, {self.name}, {self.last_activity}, {self.created_at}"


db.create_all()
