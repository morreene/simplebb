#encoding=utf-8
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request,flash

#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
#app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:12345678@localhost:3306/test"

db = SQLAlchemy(app)
SECERT_KEY="a secret key"
app.config.from_object(__name__)
app.secret_key=app.config['SECERT_KEY']
#from application.models import Message
from simplebb.models import Message

 
@app.route('/',methods=['POST','GET'])
def index():
        if request.method == 'POST':
                name = request.form['name']
                email = request.form['email']
                content = request.form['content']
                title = request.form['title']
                mess = Message(name=name,email=email,content=content,title=title)
                db.session.add(mess)
                db.session.commit()
                flash("Add Message Sucess!!")
                #return name+email+content+title
                return redirect(url_for("index"))
        else:
                mess = Message.query.all()
                return render_template("index.html",message=mess)
 
@app.route('/show/<int:id>')
def show(id):
        mess = Message.query.filter_by(id=id).first()
        if mess !=None:
                return render_template("show.html",message=mess)
        else:
                return redirect(url_for("index"))