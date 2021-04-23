import os
import json
from datetime import datetime 

#import crud
from model import User, Group, Event, db, connect_to_db
#import server 

def fake_users():
    user1 = User(fname ='Bob', lname ='Doe',email ='bob@bob',password = 'bob123', group_id=1) 
    user2 = User(fname = 'May',lname = 'maymay',email ='may@may',password ='may123', group_id=1)
    user3 = User(fname ='Pinky', lname ='Pie',email ='pinky@pinky',password = 'pinky123', group_id=1) 
    user4 = User(fname = 'Lucy',lname = 'lu',email ='lucy@lucy',password ='lucy123', group_id=2)

    db.session.add(user1) #adding to our database
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    db.session.commit() # committing to changes and adds we made (just like git commit)
    

def fake_group():
    group1 = Group(capacity=4,creator ="Jeff")
    group2 = Group(capacity=9,creator ="Minni")
    group3 = Group(capacity=5,creator ="Larry")
    group4 = Group(capacity=6,creator ="Micky")

    db.session.add(group1) #adding to our database
    db.session.add(group2)
    db.session.add(group3)
    db.session.add(group4)

    db.session.commit()

def fake_events():
    event1 = Event(event_name ="pool party",location ="Las vegas", date = "2/18/2021", time = "5:00pm", limitations = "none") 
    event2 = Event(event_name ="tennis",location ="florida", date = "3/18/2021", time = "10:00am", limitations = "guys only") 
    event3 = Event(event_name ="dance party",location ="San Francisco", date = "5/18/2021", time = "9:00pm", limitations = "none") 

    db.session.add(event1) #adding to our database
    db.session.add(event2)
    db.session.add(event3)
    db.session.add(event4)

    db.session.commit()



fake_users()
fake_group()
fake_events()

connect_to_db(app)
# db.create_all()