from model import db, User, Userevent, Event
# import requests
from datetime import datetime

def user_login(fname,lname,email,password):
    user = User(fname =fname ,lname =lname ,email=email,password=password)
    
    db.session.add(user) 
    db.session.commit()
    return user

def create_user(name,email,password):
    new_user = User(fname = name ,lname= "",email=email,password=password)

    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()
    
    # db.session.add(get_new)
    # db.session.commit()
    

#session.query(MyClass).filter(MyClass.name == 'some name')   MyClass.query._______().

# userevent1 = Userevent(user_id = user.users_id,events_id = event.events_id)

def create_group(id,capacity,creator):
    group = Group(id = id,capacity = capacity ,creator = creator) 

    db.session.add(group) 
    db.commit.session()

    return group 




def create_events(event_name,location, date,time,limitations):
    events = Event(event_name = event_name,location = location,date = date,time = time,limitations =limitations)

    db.session.add(events) 
    db.session.commit()

    return events

def create_userevent(event, user):
    """takes in an event obj and a user obj -> connects them through the userevents table"""
    new_userevent = Userevent(user_id=user.users_id, events_id=event.events_id)
   
    db.session.add(new_userevent)
    db.session.commit()

    return new_userevent



def grab_all_events_user_id(user_id):

    userevents =  Userevent.query.filter(Userevent.user_id ==user_id).all()
    event_ids = []
    events = []
    for userevent in userevents:
        event_ids.append(userevent.events_id)

    for event_id in event_ids:
        event = Event.query.get(event_id)
        events.append(event)

    return events


def get_user_by_fname(fname):
    
    return User.query.filter(User.fname == fname).first()
    




def seed_userevent():

    michael = User.query.get(1) #getting the user with users_id  = 1
    print(michael)
    events = Event.query.all() # [<CatCafe>, <Volleyball>, <Dance>, <....>] list of event objects
    print(events)
    for event in events:
        new_userevent  = create_userevent(michael, event)
        print(new_userevent)
   
   

# def check_email()


# def check_password()