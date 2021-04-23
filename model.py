
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Data model for a user."""

    __tablename__  = 'users'

    users_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    password = db.Column(db.String(50), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey("groups.group_id"))

    #groups = db.relationship("Group", backref="users")

    # can just query User.query.filterBy(group_id=1) --> list of users that are apart of the same group


   # >>> users = User.query.filter_by(group_id=1).all()
   # >>> users
   # [  <User users_id=2 email=bob@bob>,
   #    <User users_id=3 email=may@may>,
    #   <User users_id=4 email=pinky@pinky> ]

    def __repr__(self):
        """Provide helpful representation when printing."""

        return f'<User users_id={self.users_id} email={self.email}>'


class Group(db.Model):

    __tablename__ = "groups" 
    
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    capacity = db.Column(db.Integer, nullable=False)
    creator = db.Column(db.String(50), nullable=False)

    event_id = db.Column(db.Integer, db.ForeignKey("events.events_id"))
    


class Event(db.Model):

    __tablename__ = "events" 
    
    events_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50),nullable=False)
    time = db.Column(db.String(50),nullable=False) 
    limitations = db.Column(db.String(50), nullable=False)

#  event1 = Event(event_name = "Cat Cafe",location ="(36.063965,-115.172241)",date ="3/20/2021",time = " noon", limitations =" No dogs")
#  event2 = Event(event_name = "Volleyball",location ="(36.147335,-115.159708)",date ="3/25/2021",time = " 2pm", limitations =" workout gear necessary")
#  event3 = Event(event_name = "Dance lesson",location ="(36.103411,-115.120877)",date ="3/26/2021",time = " 6pm", limitations ="bring heels")
#  event4 = Event(event_name = "Outdoor Concert",location ="(36.170700,-115.144020)",date ="3/27/2021",time = " 7pm", limitations ="bring mask")
#  event5 = Event(event_name = "Potluck Picnic",location ="(36.151451,-115.249032)",date ="3/28/2021",time = " noon", limitations ="bring food")

class Userevent(db.Model):

    __tablename__ = "userevents" 
    
    user_events_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'))
    events_id = db.Column(db.Integer, db.ForeignKey('events.events_id'))
    

# another table to connect them all?


#         Tables:
# Users - id, fname, lname, email
# Group - id, capacity, leader(the creator of event)
# (Association Table) UserGroups -  id, group_id, user_id 
# Events -  id, location, date, limitations
# (Association Table) UserEvents - id, user_id, event_id


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///meetups'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')





######## IF YOU  UPDATE YOUR DATABASE #########
# ipython -i model.py
# db.create_all()
# user1 = User(fname="bob" ....)
# db.session.add(user1)
# db.session.commit()

# psql meetups
# SELECT *  FROM users; <- semicolon ;) 