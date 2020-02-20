import os
import tempfile

import pytest
from app import app
from app.models import Projects
from app import db


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_base_url(client):

    rv = client.get('/')
    assert rv.status_code == 200


def test_serch_url(client):
    rv = client.post('/search/', data=dict(
        row='Java Django',
    ), follow_redirects=True)

    assert b'new repositories added' in rv.data
    assert b'new repositories added' not in rv.data
    db.drop_all()


# def test_exist_url(client):
#
#     rv = client.post('/search/', data=dict(
#         row='Python Django',
#     ), follow_redirects=True)
#     assert b'new repositories added' not in rv.data

# @pytest.fixture(scope='module')
# def projects_db(tmpdir):
#     """Подключение к БД перед тестами, отключение после."""
#     # Setup : start db
#     db.start_tasks_db(str(tmpdir), 'tiny')
#
#     yield
#
#     # Teardown : stop db
#     db.stop_tasks_db()


# @pytest.fixture(scope='module')
# def new_project():
#     project = Projects(project_id=1, description="First row", name="Den", last_activity="2020-02-19T13:10:18.204Z")
#     return project
#
#
# @pytest.fixture()
# def just_two_projects():
#     project_1 = Projects(project_id=1, description="First row", name="Flask", last_activity="2018-01-17")
#     project_2 = Projects(project_id=2, description="Second row", name="Django", last_activity="2020-02-19")
#     return project_1, project_2
#
#
# @pytest.fixture()
# def db_with_2_projects(projects_db, just_two_projects):
#     """Подключение БД с 2 задачами, все уникальны."""
#     for p in just_two_projects:
#         db.add(p)
#
#
# def test_add_increases_count(db_with_2_projects):
#     """Test projects_db.add() должен повлиять на tasks.count()."""
#     #  GIVEN db с 3 задачами
#     #  WHEN добавляется еще одна задача
#     tasks.add(Task('throw a party'))
#
#     #  THEN счетчик увеличивается на 1
#     assert tasks.count() == 4
#
#
# def test_new_project(new_project):
#
#     assert new_project.project_id == 1
#     assert new_project.description == 'First row'
#     assert new_project.name == 'Den'
#     assert new_project.last_activity == "2020-02-19T13:10:18.204Z"


