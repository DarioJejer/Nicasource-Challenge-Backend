# Nicasource-Challenge-Backend

# How to launch the project

- Clone the repository into your machine.

- Make sure to have Python 3 installed: 
https://www.python.org/downloads/

- Install Django globally or in a virtual environment using pip, be sure to follow: 
https://docs.djangoproject.com/en/3.2/topics/install/

- Install Django REST framework using ```pip install djangorestframework```  on the project folder.

- Now from the "API" run ``` python manage.py migrate MovieApp``` to apply the migrations onto the database.

- To check and modify the database use SQLite Studio that you can download from here: 
https://sqlitestudio.pl/

- To use it, lunch SQLiteStudio executable, on the app, go to Database>AddDatabase>File and select the "db.sqlite3" file on the Django project.

- Next, we need to install cors in order to enable domains to consume the projects endpoints running ``` pip install django-cors-headers```.

- Finally, you can run ```python manage.py runserver``` from the project directory to get server up and running.

- It is sugested to test the endpoints using Postman: https://www.postman.com/