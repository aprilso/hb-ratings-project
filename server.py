"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def homepage():
    '''view homepage'''
    return render_template('homepage.html')

@app.route('/movies')
def moviepage():
    """view all movies"""

    movies = crud.return_all_movies()

    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    '''show details of movie'''
    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/movies/<movie_id>/ratings', methods =["POST"])
def rate_movie(movie_id):
    """rate a movie from 0-5"""

    logged_in_user = session.get("user_email") 
    user_rating = int(request.form.get("rating"))

    if logged_in_user is None:
        flash("You must be logged in to a rate a movie")
    elif not user_rating:
        flash("Error: yo didn't rate the movie")
    else:
        user = crud.get_user_by_email(logged_in_user)
        movie = crud.get_movie_by_id(movie_id)

        crud.create_rating(user, movie, user_rating)

        flash(f"We have saved {logged_in_user}, {movie_id}, with a score of {user_rating}")

    return redirect(f"/movies/{movie_id}")


@app.route('/users')
def userpage():
    """view all users"""

    users = crud.return_all_users()

    return render_template("all_users.html", users=users)

@app.route('/users/<user_id>')
def user_details(user_id):
    """show user details"""
    
    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route('/users', methods=['POST'])
def new_user():
    """Creates a new user"""

    email = request.form.get('email')
    password = request.form.get('password')

    new_user = crud.get_user_by_email(email)

    if new_user == None:
        crud.create_user(email, password)
        flash("Yay account created!")
    else:
        flash("An account with that email already exists! Try another email.")


    return redirect('/')

@app.route('/login', methods=["POST"])
def login():
    """login user"""
    email = request.form.get('login_email')
    password = request.form.get('login_password')

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password is incorrect")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}")
    # if user.password == password:
    #     flash (f"Logged in! User id is {user.user_id}")
    #     session['user'] = user.user_id
    # else:
    #     flash ("Wrong password, try again")
    
    return redirect ("/")

# once you're logged in, go to the movie page to rate a movie
# in the movie_details.html page, add rating html code - dropdown menu 1-5 rating, submit (flash message that rating worked)
# create an app route for rating
# update the database with the movie's rating






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
