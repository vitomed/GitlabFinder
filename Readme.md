Gitlab поисковик проектов
========


* Структура проекта:

	```
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
	    test_pytest.py
	    /log
	```

* Запустить проект:

	```user@:~/my_project/$ python3 main.py```


* Рабочие API:

	```http://localhost:5000/``` - начальная страница

	```http://localhost:5000/search/``` - поиск проектов

	```http://localhost:5000/projects/``` - JSON, содержащий искомые проекты, полученные из локальной БД.


* Запуск тестов:

	```user@:~/my_project/$ python3 -m pytest tests/test_pytest.py``` 
