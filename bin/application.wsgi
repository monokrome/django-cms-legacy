import os, sys, ConfigParser

# Application configuration contains basic application settings, while local
# configuration contains private information that shouldn't be commited to
# your code repository.
conf_paths = (
    './conf/application',
    './conf/local',
)

### Configuration section. Sets up environment variables for django.
#####

for path in conf_paths:
    config = ConfigParser.ConfigParser()
    config.read('{0}.ini'.format(path))

# Read our configuration data, and convert it into environment
# variables that can be used securely from within our django project.

    for section in config.sections():
        for option in config.options(section):
            environment_setting = ('%s_%s' % (section, option)).upper()
            os.environ[environment_setting] = config.get(section, option)

### Start up our django application
#####
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

