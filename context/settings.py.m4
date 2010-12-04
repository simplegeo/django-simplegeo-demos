# Django settings for Wikileaks project.
import django, os, sys

DEBUG = True
TEMPLATE_DEBUG = '__DEBUG__'

ADMINS = (
    ('Joe Stump', 'joe@joestump.net')
)

# Set up our paths
SITE_ROOT = os.path.dirname(os.path.realpath(`__file__'))
sys.path.append("%s%ssite-packages" % (SITE_ROOT, os.sep))

MANAGERS = ADMINS

DATABASE_ENGINE     = '__DATABASE_ENGINE__'
DATABASE_NAME       = __DATABASE_NAME__
DATABASE_USER       = '__DATABASE_USER__'
DATABASE_PASSWORD   = '__DATABASE_PASSWORD__'
DATABASE_HOST       = '__DATABASE_HOST__'
DATABASE_PORT       = '__DATABASE_PORT__'

# PayPal email address
PAYPAL_RECEIVER_EMAIL = "chunkyewok@yahoo.com"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'feuq35c6-!u0z)fal-5viac@hj$za^egrp=@c=3i9uyl4%r_c$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    '%s/templates' % SITE_ROOT
)

TEMPLATE_CONTEXTY_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'context.flickr',
)

# Email settings
DEFAULT_FROM_EMAIL      = '__DEFAULT_FROM_EMAIL__'
EMAIL_HOST_USER         = '__EMAIL_HOST_USER__'
EMAIL_HOST_PASSWORD     = '__EMAIL_HOST_PASSWORD__'
EMAIL_HOST              = '__EMAIL_HOST__'
EMAIL_PORT              = __EMAIL_PORT__

# Where to redirect logged out users
LOGIN_URL = '/user/login/'

# Our session's cookie name
SESSION_COOKIE_NAME = 'context'

FLICKR_API_KEY = '__FLICKR_API_KEY__'
