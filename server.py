from flask import Flask, jsonify, render_template, request,flash,redirect, url_for, session
from model import User, Group, Event, connect_to_db,db
import crud
from jinja2 import StrictUndefined


# from event import (set_map_center, set_markers)

# from event import (
#     get_events, get_event_details, create_new_user, get_venue_details, 
#     get_venue_coordinates, add_bookmark_to_db, get_attendees,
#     get_interested)

# import requests

app = Flask(__name__)
app.secret_key = "may123"
app.jinja_env.undefined



@app.route('/')
def homepage():
    """Show the homepage."""
    
    return render_template("homepage.html")
    


# @app.route("/login")
# def show_login():
#     """Show login form."""
    
#     return render_template("/login.html")

   
@app.route("/login")
def show_login():
    #show login form
    
    return render_template("homepage.html")
   

@app.route("/login", methods=['POST'])
def log_in():
    
    email = request.form.get('email')
    password = request.form.get('password')
    # all queries should be crud functions to call 
    # user = User.query.filter((User.email == email) & (User.password == password)).first()

    user = User.query.filter_by(email=email).first()
    # expect: <User 'bob'>
    print(user)
    user_password = user.password
    user_name = user.fname
    print(password)
    print(user_password)

    if password == user_password: #password is what someone typed from HTML, user_password is from DB
        session["user"] = user_name
        print("YOU'RE IN THE IF STATEMENT", session["user"])
        return render_template("user_profile.html",email = email)

    #If user == None, register user as new_user
    else: 
        return redirect('/login')
    
    


   


@app.route("/logout")
def logout():
    """Log out."""

    # del session["user_id"]
    flash("Logged Out.")
    return redirect("/") 





@app.route("/sign_up")
def show_signup():
    
    
    return render_template("sign_up.html")


@app.route("/sign_up", methods=['POST'])
def signup():
    
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    new_user = crud.get_user_by_email(email)


    new_user = User.query.filter_by(email=email).first()
    # expect: <User 'bob'>
    # print(user)
    # user_password = user.password
    # user_name = user.name


    if new_user:
        flash('Account already exists. Try again.')
    else:
        crud.create_user(name,email, password)
        flash('Account created! Please log in.')


    return redirect('/login')

    # 

    # if User == email:
    #     flash(f'This account is already exist. login or create new one' )
    #     return render_template('sign_up.html')

    # else:
    #     crud.create_user(fname,lname,email,password)
    #     flash('Account has been created.Please log in :)')
    #     return redirect('/log_in')

@app.route("/user_profile")
def view_profile():
    

    return render_template("user_profile.html")
    


@app.route("/maps")
def view_maps():
    

    return render_template("maps.html")



# @app.route('/create-event')
# def render_create_event_template():

#     return render_template('events.html')

@app.route('/maps', methods=['POST'])
def user_creates_event():
    e_name = request.form.get('event_name')
    e_date = request.form.get('event_date')
    e_time = request.form.get('event_time') 
    e_location = request.form.get('event_location')
    e_limitations = request.form.get('event_limitations')
    print(e_name)
    user_fname = session['user']
    e_obj = crud.create_events(e_name,e_location,e_date,e_time,e_limitations) # returns event obj 
    u_obj = crud.get_user_by_fname(user_fname)
    crud.create_userevent(e_obj,u_obj)
    print(e_obj)
    all_events = crud.grab_all_events_user_id(u_obj.users_id)

    return render_template('user_profile.html')
    # return render_template('user_profile.html', all_events=all_events)





@app.route("/calendar")
def show_cal():
    #show login form
    
    return render_template("/calendar.html")

 # homepage - "start your adventure" 
 # from the homepage some route leading logging in or signing up
 # login.html -> form with "email / password" textboxes to submit
 # ^^that form will need an action to the "/profile"

@app.route("/events-api.json")
def get_event_objects():
   events = Event.query.all() # list of event objects
   event_dict = {}
   event_dict["event_name"]  = []
   event_dict["location"] = []
   for event in events:
       event_dict["event_name"].append(event.event_name)
       event_dict["location"].append(event.location)
    # print(event_dict)
    
    # return(jsonify(event_dict))
       return render_template("/maps.html") 







   



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)












































































