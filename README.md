# MyDBTJourney: Back End
This is the back end for MyDBTJourney! It is also under construction. (Find the front end with information over the application in my other repo!)

## How to Use
This is a Django Rest Framework back end. There's a bit of setting up to do; but luckily Django does a lot of the work for you:
- Clone/copy the repo
- Open it up and create a new virtual environment: python3 venv <yourenvironmentname>
- Activate your virtual environment: source <yourenvironmentname>/bin/activate
- Install the project dependencies: pip install -r requirements.txt
- Set up the db: python manage.py migrate (since this is a personal project, I'm using the built in SQLite db that comes with Django Rest Framework. This may change in the future.)
- I used Cloudinary for image uploads, so you'll either have to change it in the code or use your own Cloudinary account and attach it in a .env file
- If you would like to use the admin page for Django Rest Framework, create a superuser: python manage.py createsuperuser
- Run the server using: python manage.py runserver
