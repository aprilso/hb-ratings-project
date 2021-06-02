"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def return_all_users():
    """return all users"""

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)



def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def return_all_movies():
    """Return all movies"""
    
    return Movie.query.all()

def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)



# def create_rating(user_id, movie_title, score)
    # query for the movie using filter_by
    # query for the user using .get (or just use user_id)
def create_rating(user, movie, score):
  """create and return a new rating"""
    
  rating = Rating(user=user, movie=movie, score=score)
  #parameters 'user' and 'movie' are OBJECTS to be passed! query these objects, 
  #store in variable 'user' & 'movie', pass in arguments
  #this is good if you're already accessing the data by objects

  #our original: rating = Rating(user_id=user_id, movie_id=movie_id, score=score)
  ### This solution isn't wrong - if you're querying everything by movie_id, it's ok to continue querying by movie_id
  
  

  db.session.add(rating)
  db.session.commit()

  return rating





if __name__ == '__main__':
    from server import app
    connect_to_db(app)