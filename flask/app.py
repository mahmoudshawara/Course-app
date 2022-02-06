#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
import babel
from flask import Flask, render_template, request, flash, redirect, url_for , abort,jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref
import datetime
from datetime import datetime
import sys
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate (app , db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Course (db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable= False)
    start_date = db.Column(db.DateTime(), default=datetime.now)
    
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date

    def insert(self):
        db.session.add(self)
        db.session.commit()    
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

db.create_all()
db.session.commit()
#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y"
  elif format == 'medium':
      format="EE MM, dd, y"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#  List courses sorted by date
#  ----------------------------------------------------------------
@app.route('/')
def course_welcome():
    return 'Hello, Welcome in course app!\n'

@app.route('/courses')
def list_courses():
    all_courses = Course.query.order_by(Course.start_date).all()
    courses=[]
    for course in all_courses:
        courses.append({
        "id": course.id,
        "name": course.name, 
        "start_date":course.start_date.strftime("%Y-%m-%d"),
      })
    if len(courses) == 0:
        abort(404)
    return jsonify({
        'courses': courses,
    })

#  Add a new  course
#  ----------------------------------------------------------------
@app.route('/add_course', methods=['POST'])
def add_course():
    body = request.get_json()
    if not body:
        abort(422)
    new_name = body.get('name', None)
    new_date= body.get('start_date', None)
    new_course = Course(name=new_name,start_date=new_date)
    new_course.insert()
    return jsonify({
        'created': new_course.id,
        'name': new_course.name,
        'date': new_course.start_date.strftime("%Y-%m-%d"),
    })
    

#  Edit course
#  ----------------------------------------------------------------
@app.route('/edit_course/<int:course_id>', methods=['POST'])
def edit_course(course_id):
    course = Course.query.filter (Course.id==course_id).one_or_none()
    body = request.get_json()
    new_name = body.get('name', None)
    new_date= body.get('start_date', None)
    if course:
        if new_name:
            course.name = new_name
        if new_date:
            course.start_date=new_date
        course.update()
        return jsonify({
                'updated': course.id,
                'name': course.name,
                'date': course.start_date.strftime("%Y-%m-%d"),
            })
    else:
        abort(422)


app.errorhandler(404)
def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    migrate = Migrate(app, db)
    app.debug=True
    app.run("0.0.0.0")
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
import babel
from flask import Flask, render_template, request, flash, redirect, url_for , abort,jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref
import datetime
from datetime import datetime
import sys
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate (app , db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Course (db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable= False)
    start_date = db.Column(db.DateTime(), default=datetime.now)
    
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date

    def insert(self):
        db.session.add(self)
        db.session.commit()    
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

db.create_all()
db.session.commit()
#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y"
  elif format == 'medium':
      format="EE MM, dd, y"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#  List courses sorted by date
#  ----------------------------------------------------------------
@app.route('/')
def course_welcome():
    return 'Hello, Welcome in course app from AWS!\n'

@app.route('/courses')
def list_courses():
    all_courses = Course.query.order_by(Course.start_date).all()
    courses=[]
    for course in all_courses:
        courses.append({
        "id": course.id,
        "name": course.name, 
        "start_date":course.start_date.strftime("%Y-%m-%d"),
      })
    if len(courses) == 0:
        abort(404)
    return jsonify({
        'courses': courses,
    })

#  Add a new  course
#  ----------------------------------------------------------------
@app.route('/add_course', methods=['POST'])
def add_course():
    body = request.get_json()
    if not body:
        abort(422)
    new_name = body.get('name', None)
    new_date= body.get('start_date', None)
    new_course = Course(name=new_name,start_date=new_date)
    new_course.insert()
    return jsonify({
        'created': new_course.id,
        'name': new_course.name,
        'date': new_course.start_date.strftime("%Y-%m-%d"),
    })
    

#  Edit course
#  ----------------------------------------------------------------
@app.route('/edit_course/<int:course_id>', methods=['POST'])
def edit_course(course_id):
    course = Course.query.filter (Course.id==course_id).one_or_none()
    body = request.get_json()
    new_name = body.get('name', None)
    new_date= body.get('start_date', None)
    if course:
        if new_name:
            course.name = new_name
        if new_date:
            course.start_date=new_date
        course.update()
        return jsonify({
                'updated': course.id,
                'name': course.name,
                'date': course.start_date.strftime("%Y-%m-%d"),
            })
    else:
        abort(422)


app.errorhandler(404)
def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    migrate = Migrate(app, db)
    app.debug=True
    app.run(host='0.0.0.0')
