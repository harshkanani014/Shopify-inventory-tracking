# Shopify-inventory-tracking

## Project deployed on heroku : https://shopify-inventory-track.herokuapp.com/

# Project Description
#### Developed a Web App to add, edit , get and delete items in Inventory. API for CRUD operations was developed to maintain scalability and maintainability of project. Also added features to upload image view as thumbnail on index page. Can update item as per order to track each and every item in inventory
 
# Tech Stack Used :
1. Django Rest Framework (Python3 based backend framework)
2. PostgreSQL (SQL Database)
3. Javascript
4. HTML
5. CSS

# Standard Formats :
1. Code Format - PEP-8 (python standard format)
2. API format - REST based

# Tools Used :
1. Heroku (for deployment)
2. Amazon S3 ( To Store Image)
3. Postman (for API testing and API documentation)
4. Git
5. Github
6. VScode


## Web APP Features :
1. Add Inventory Items with item code, item name, quantity, sales, price, location, images.
2. Can update/edit each and every item from Inventory so can track items sales.
3. Delete Item from Inventory.
4. Can Upload Image while adding item and uploaded image can be viewed on homepage as thumbnail.
5. All items in Inventory can be viewied on mainpage in table format.

   
## How to run project on your local setup :
## STEP-1 : Install PostgreSQl with pgAdmin
### How to install PostgreSQL?
##### Download postgreSQL from following link and install 
##### https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

## STEP-2 : Set Up Database 
##### Open PgAdmin and Create a database with name as per choice in PgAdmin.

## STEP-3 : Clone this repository

## STEP-4 : Creating Virtual environment
##### Use following command to set up virtual environment
```py -m venv <env-name>```

##### Activate environment
```<env-name>\Scripts\activate.bat```

## STEP-5 Install requirements.txt
```pip install -r requirements.txt```

## STEP-6 : Go to course_registration/settings.py
##### Replace database_name, database_user and database_password in following code

```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-database-name',
        'USER': 'your-user-name',
        'PASSWORD': 'your-password',
        'HOST': 'localhost'
    }
} 
```

## STEP-7 : Run following commands
```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py runserver```

#### Hurrah your website is running


## Set up superuser
#### Use following command
```python manage.py createsuperuser```

## Thank you


