import pytest

from app import db
from app.routes import app
from app.models import Project
from config import ConfigApp, ConfigTest


@pytest.fixture(scope='module')
def test_app():
    test_app = app
    test_app.config.from_object(ConfigTest)
    db.init_app(test_app)

    with test_app.app_context():
        db.create_all()

        yield (test_app, db)
        db.drop_all()


def test_development_config(test_app):
    test_app[0].config.from_object(ConfigApp)
    assert test_app[0].config['DEBUG']
    assert not test_app[0].config['TESTING']


def test_testing_config(test_app):
    test_app[0].config.from_object(ConfigTest)
    assert test_app[0].config['DEBUG']
    assert test_app[0].config['TESTING']
    assert not test_app[0].config['PRESERVE_CONTEXT_ON_EXCEPTION']


def test_url(test_app):
    rv = test_app[0].test_client()

    resp = rv.get('/')
    assert resp.status_code == 200

    resp = rv.get('/foo/bar')
    assert resp.status_code == 404

    resp = rv.get('/search/')
    assert resp.status_code == 200

    resp = rv.post('/search/', data=dict(row='Kotlin'), follow_redirects=True)
    assert b'new repositories added' in resp.data
    assert resp.status_code == 200

    resp = rv.post('/search/', data=dict(row='Kotlin'), follow_redirects=True)
    assert b'Added nothing repositories!' in resp.data
    assert resp.status_code == 200

    resp = rv.post('/search/', data=dict(row=''), follow_redirects=True)
    assert b'You send empty row' in resp.data
    assert resp.status_code == 200


@pytest.fixture(scope='module')
def new_project():
    project = Project(project_id=23, description="TDD lessons", name="TDD", last_activity="2020-02-19")
    return project


def test_new_project(new_project):

    assert new_project.project_id == 23
    assert new_project.description == 'TDD lessons'
    assert new_project.name == 'TDD'
    assert new_project.last_activity == "2020-02-19T13:10:18.204Z"


def test_add_exist_project(test_app, new_project):
    test_app[1].session.add(new_project)
    test_app[1].session.commit()
    assert test_app[1].session.query(Project).filter(Project.name == "TDD").all()
    assert not test_app[1].session.query(Project).filter(Project.name == "CI").all()


def test_count_elements(test_app):
    p1 = Project(project_id=1, description="row", name="Count", last_activity="2015-02-1")
    p2 = Project(project_id=2, description="row", name="Count", last_activity="1995-12-2")
    test_app[1].session.add_all([p1, p2])
    test_app[1].session.commit()
    assert len(test_app[1].session.query(Project).filter(Project.name == "Count").all()) == 2



