# encoding=utf-8
 
#from flask.ext.script import Manager
from flask_script import Manager
#from application.app import app

from simplebb import app
from simplebb import models


manager = Manager(app)
app.config['DEBUG'] = True
if __name__ == '__main__':
    manager.run()