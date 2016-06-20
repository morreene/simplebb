# encoding=utf-8
 
from flask_script import Manager
from simplebb import app
from simplebb import models

manager = Manager(app)
app.config['DEBUG'] = True
if __name__ == '__main__':
    manager.run()