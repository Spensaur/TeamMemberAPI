# TeamMemberAPI
An example API for managing a team using Django Rest Framework


## Project Setup  - Ubuntu 18.04 LTS
Here are commands to install all of the dependencies you will need for this project.

    apt-get update
    apt-get install python3
    apt-get install python-pip
    apt-get install python3-dev default-libmysqlclient-dev
    apt-get install mysql-server
    
It is recommended that you use a virtualenv for this environment if it is a shared environment:
    
    python3 -m venv ~/.virtualenvs/djangodev
    source ~/.virtualenvs/djangodev/bin/activate
    
Then install the following python libraries in your python env:

    pip install Django
    pip install mysqlclient
    pip install djangorestframework
    pip install markdown
    pip install django-filter

Note: you will need to setup this project with python3 because this is a Django2 project
and Django 2 requires python3
    
You can setup mysql with some additional commands:

    sudo systemctl start mysql
    sudo systemctl enable mysql
    
Then you can log into mysql:

    sudo /usr/bin/mysql -u root -p
    
Then create the django database user and give it permissions so that it can create and destroy databases for tests:

    mysql> CREATE USER django;
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'django'
    
Note: for production environments restrict the permission of django database user more than this.

Create the database that django will use:

    mysql> CREATE DATABASE djangodb
    
You will likely need to migrate your your database settings after setting this up:
    
    python manage.py makemigrations team_api_app
    python manage.py migrate
    
    
You are now all setup to run this app!

## How to Run

Run the following command from the project directory(eg. ../../TeamMemberAPI/)

    python manage.py runserver

You should see some output that looks something like this in your terminal:
    
    Starting development server at http://127.0.0.1:8000/
    
The API is now running at that address. Point your browser to that address to explore it.

## Testing
You can run automated tests with the following command from the project directory:

    python manage.py test
    
Note: you do not need a server running to run tests. This command will run all of the code for you and will
even create and destroy test tables within your database for you!
 
You can do interactive testing/debugging in your python interpreter of choice
with the following command:

    python manage.py shell
    
or if you want to use the Ipython interpreter:

    python manage.py shell -i ipython
    
You can test the API manually with the following commands:

Get a list of team members:

    curl -X GET http://127.0.0.1:8000/team_members/
    
Add a new team member:

    curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/team_members/ -d '{"first_name":"Tim","last_name":"Timmington","phone_number":54321789,"email":"tim.thetimmer@timtown.com","admin_role":true}'
    
Update an existing team member:

    curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/team_members/4/ -d '{"first_name":"Tim","last_name":"Timmington","phone_number":123456789,"email":"tim.thetimmer@timtown.com","admin_role":true}'
    
Delete an existing team member:

    curl -X DELETE http://127.0.0.1:8000/team_members/2/    
    
Note: The Django rest framework has a built in API explorer if you point your browser to a given endpoint
and is another option for testing the API.