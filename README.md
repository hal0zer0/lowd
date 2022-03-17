# Legend of the White Dragon
Recreation of the BBS game "Legend of the Red Dragon" with Django
(currently in very early initial development stage)

## Installation
###Download source
```git clone https://github.com/hal0zer0/lowd.git```

###Install Requirements
```pip install -r requirements.txt```

###Secrets file
Create a ```lowd_secrets.py``` file with a ```settings_secret_key=```containing a long random string LIKE
```python
settings_secret_key='skG7f#8kgjdGD(wON29&3baWeCanDanceIfWeWantTo'
```
This is used for background security stuff and should NOT be added to Git

TEMPORARILY I am including a sqlite db to make initial setup easier for contributors.  Eventually the db will be removed from source control and I will provide fixtures for the data to be imported.

## Running
From within directory containing manage.py
```python manage.py runserver```

Which should give you web access at localhost:8000

Login is required for all views, so first go to /admin and login there with admin/roadhouse.  After that / will give you a site.  I'm making a login page now.

Again, this is temporary.  