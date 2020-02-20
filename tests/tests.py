import os
import unittest
import tempfile
from config import basedir
from app import app, db
from app.models import Projects


class TestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'projects.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_make_unique_nickname(self):
        p = Projects(project_id=1, description="First row", name="Den", last_activity="2020-02-19T13:10:18.204Z")
        db.session.add(p)
        db.session.commit()
         = Projects.make_unique_nickname('john')
        assert nickname != 'john'
        u = Projects(nickname=nickname, email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = Projects.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname


if __name__ == '__main__':
    unittest.main()
