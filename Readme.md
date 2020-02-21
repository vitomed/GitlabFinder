Gitlab поисковик проектов
========


### Структура проекта:

	my_project/
	  config.py
	  Dockerfile
	  main.py
	  projects.db
	  requirements.txt
	  test.db
	  /app
	    __init__.py
	    models.py	
	    routes.py
	    worker.py
	   /static
	   /templates
	      404.html
	      500.html
	      base.html
	      form.html
	  /env
	  /log
	  /tests
	    connftest.py
	    test_application.py
	    
	

### Как запустить:


	user@:~/my_project/$ python3 main.py


### Рабочeе API:

	http://localhost:5000/ - начальная страница

	http://localhost:5000/search/ - поиск проектов

	http://localhost:5000/projects/ - JSON, содержащий искомые проекты, полученные из локальной БД.


### Запуск тестов:

	user@:~/my_project/$ python3 -m pytest tests/test_application.py

### Ключевые модули Python используемые в проекте

[Flask](https://flask.palletsprojects.com/en/1.1.x/) - micro-framework for web application development

[Jinga2](https://jinja.palletsprojects.com/en/2.11.x/) - templating engine

[SQLAlchemy](https://www.sqlalchemy.org/) - ORM (Object Relational Mapper)

[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - is an extension for Flask that adds support for SQLAlchemy 
to your application.

[Testing Flask Applications using pytest](https://flask.palletsprojects.com/en/1.1.x/testing/) -  pytest - framework for write complex functional testing.

[Search API from python-gitlab library](https://python-gitlab.readthedocs.io/en/stable/gl_objects/search.html) - python-gitlab library provides simple API for gitlab


В проекте использовалась версия интерпретатора Python 3.7.