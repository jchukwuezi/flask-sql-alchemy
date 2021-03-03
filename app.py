from flask import Flask, render_template, request, redirect, url_for, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.secret_key = "jchukwuezi"

#used to create the database models
db = SQLAlchemy(app)

#making a student model
class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    #function to initialise class
    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route("/")
def show_users():
    #I am passing in students variable into frontend, and it's a query (similar to ResultSet in java)
    return render_template('show-student.html', students = Students.query.all() )

#adding new user to database
@app.route("/new", methods = ['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        #making sure everything has been added to the session
        if not request.form['name'] or not request.form['city'] or not request.form['address'] or not request.form['pin']:
            return "<h1>There was an error with entering the details in the form </h1>"
        else:
            name = request.form['name']
            city = request.form['city']
            address = request.form['address']
            pin = request.form['pin']

            #add user to database
            #constructing an object, similar to java
            student = Students(name, city, address, pin)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for("show_users"))

    return render_template('add-student.html')
        





    




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    
 