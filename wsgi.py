# file wsgi.py 
import os
import sys

full_path = os.path.realpath(__file__)
current_dir = os.path.dirname(full_path) + "/"
sys.path.append(current_dir)

#Assume that you are using virtualenv to dev, change this to your env name
YOUR_ENV_NAME = 'env'

activate_this = current_dir + YOUR_ENV_NAME + '/bin/activate_this.py'

execfile(activate_this, dict(__file__=activate_this))

from main import app
application = app.wsgifunc()


