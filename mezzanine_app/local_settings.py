# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "django-insecure-*k5xd8t*e8a%=4@k=6%!cr0h$c8=2*kg^+6*3-fxg^ltw_)doh"
NEVERCACHE_KEY = "&%v6074f6%8rin#kua=ot61nt95!@$3+80rmaj^t=m7@1wk3j$"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
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

# Allowed development hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "::1","192.168.121.151"]
