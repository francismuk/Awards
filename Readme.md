# [Instagram](https://mukawards.herokuapp.com)
#### Web clone of the Instagram app
#### July 29th, 2019
#### By **[FRANCIS MUKUHA](https://github.com/francismuk)**

## Description
This is a web platform for web developers to showcase their work and rate each other's project based on the design,usability and content. To participate, users and required to have an account and logged in. For users who create account's with P-rates get to have and edit their profile, add projects done and rate other projects show cased.

## Set Up and Installations

### Prerequisites
1. Django
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/francismuk/instagram_clone.git && cd Instagram`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE insta;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations insta
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

Testing the Application
To run the tests for the class files:

    $ python3.6 manage.py test
    

## Known bugs
Review and Profile functionality do not work

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Behavior Driven Development (BDD)
| General Behavior | Input    | Output   |
| :------------- | :------------- | :------------- |
| User is authenticated | On homepage, click the sign up button  | Redirected to the user registration page |
| User can add image posts to their accounts | clicks on add button above gallery  | Redirected to the forms page of adding posts |
| User is able to navigate through the pages | Clicks on the menu options in menu bar | Navigation through the pages |
| User can view more details of project  | User clicks the see more text link | More details is revealed below |
| User can rate project in either of the provided categories | Selects the number of the stars they wish | The stars are highlighted upto the selected number |



## Support and contact details
Contact me on mukd3v3lop3r@gmail.com for any comments, reviews or advice.

### License
[MIT](./License)
Copyright (c) 2019 **FRANCIS MUKUHA**
