from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2h+y6gs!&7*5l5)aei=_+w!6ocjvkquh^ojwghsb!r!jk=7g79"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["172.20.10.10"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
