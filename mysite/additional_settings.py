#this should be filled out and added to the end of the settings.py file

DEBUG = False
SECRET_KEY = 
ALLOWED_HOSTS = []

#########
# EMAIL #                                                                                                        
#########

EMAIL_HOST_USER = 
EMAIL_USE_TLS = 
EMAIL_HOST = 
EMAIL_HOST_PASSWORD = 
EMAIL_PORT = 

#############
# DATABASES #
#############                                                                                 

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.",
        # DB name or path to database file if using sqlite3.
        "NAME": "",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

########
# Files #
########

STATIC_ROOT = 
MEDIA_ROOT = 

