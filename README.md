# Seeker RESTful API

Back-end counterpart to the full-stack [Seeker Web App](https://github.com/sncandiani/Seeker-WebApp).

## Setup

1. Clone the repo and cd into it: 
git clone git@github.com:sncandiani/Seeker-API.git && cd seekerproject

2. Set up your virtual environment:
python -m venv seekerEnv

3. Activate virtual environment:
source ./seekereEnv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Run migrations:
python manage.py makemigrations python manage.py migrate

6. Start the API server:
python manage.py runserver


## Technologies Incorporated

* Django
* Python
* SQLite
* ORM
* Models
* API Endpoint Views
* User authentication with authtoken
* Url routing

## Entity Relationship Diagram
![ERD](seekerERD.png)
