1. I am using postgreSQL so in settings.py make changes accordingly
example:-
 'ENGINE': 'django.db.backends.postgresql',  # Specify the database engine
        'NAME': 'your_database_name',  # Replace with your actual database name
        'USER': 'your_database_user',  # Replace with your actual database username
        'PASSWORD': 'your_database_password',  # Replace with your actual database password
        'HOST': 'localhost',  # Replace with your actual database host
        'PORT': '5432',  # Replace with your actual database port

2. In views.py i am using default user/ static user id (user that i have created) for inserting data and viewing
As i am using django default user table (auth_user) for my app
you can insert your user record directly or you can create superuser and with the help of admin panel you can insert the record
to create superuser
--python manage.py createsuperuser 
--set username and password 
-- now Visit to http://localhost:8000/admin
-- insert the user data
    # here i am using default user id (the user that i have created)
    audio_features = AudioFeatures.objects.filter(user_id=your_user's_id)

    # Get the user (Default user)
    user = get_user_model().objects.get(id=your_user's_id)  

Here you can add you user_id 
