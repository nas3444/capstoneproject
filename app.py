import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import true
from models import setup_db, Movie, Actor
import json
from auth import AuthError, requires_auth


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add(
      "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
    )
    response.headers.add(
      "Access-Control-Allow-Methods", "GET,POST,PATCH,DELETE"
    )
    return response

  @app.route('/')
  def index():
    return "hey"

  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(jwt):
    try:
      movies = Movie.query.all()
      movies_format = [movie.format() for movie in movies]
      return jsonify({
        'success': True,
        'movies': movies_format
      })

    except:
      abort(404)

  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(jwt):
    try:
      actors = Actor.query.all()
      actors_format = [actor.format() for actor in actors]
      return jsonify({
        "success": True,
        "actors": actors_format
      })

    except:
      abort(404)

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def post_movie(jwt):
    body = request.get_json()
    title = body.get("title", None)
    release_date = body.get("release_date", None)
    image = body.get("image", None)

    try:
      movie = Movie(title=title, image=image, release_date=release_date)
      movie.insert()
      return jsonify({
      'success': True
      })

    except:
      abort(404)

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def post_actor(jwt):
    body = request.get_json()
    name = body.get("name", None)
    age = body.get("age", None)
    gender = body.get("gender", None)
    movie_id = body.get("movie_id", None)

    try:
      actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)
      actor.insert()
      return jsonify({
      'success': True
      })

    except: 
      abort(404)

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movie(jwt, movie_id):
    body = request.get_json()
    title = body.get("title", None)
    image = body.get("image", None)
    release_date = body.get("release_date", None)

    try:
      movie = Movie.query.get_or_404(movie_id)
      if title:
        movie.title = title
      if image: 
        movie.image = image
      if release_date:
        movie.release_date = release_date
      movie.update()
      return jsonify({
        'success': True
      })

    except:
      abort(404)

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actor(jwt, actor_id):
    body = request.get_json()
    name = body.get("name", None)
    age = body.get("age", None)
    gender = body.get("gender", None)

    try:
      actor = Actor.query.get_or_404(actor_id)
      if name:
        actor.name = name
      if age:
        actor.age = age
      if gender:
        actor.gender = gender
      actor.update()

      return jsonify({
        'success': True
      })

    except:
      abort(404)


  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(jwt, movie_id):
    try:
      movie = Movie.query.get_or_404(movie_id)
      movie.delete()

      return jsonify({
        'success': True
      })

    except:
      abort(404)

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(jwt, actor_id):
    try:
      actor = Actor.query.get_or_404(actor_id)
      actor.delete()

      return jsonify({
        'success': True
      })

    except:
      abort(404)

  
  # Error Handling
  # for 422 error
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422


  # for 404 error
  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404


  # for 400 error
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "bad request"
      }), 400

  # for 401 error
  @app.errorhandler(401)
  def unauthorized(error):
      return jsonify({
          "success": False,
          "error": 401,
          "message": "Unauthorized"
      }), 401

  # for 403 error
  @app.errorhandler(403)
  def forbidden(error):
      return jsonify({
          "success": False,
          "error": 403,
          "message": "Forbidden"
      }), 403

  # for 500 error
  @app.errorhandler(500)
  def internal_server(error):
      return jsonify({
          "success": False,
          "error": 500,
          "message": "internal server error"
      }), 500


  # for auth error
  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error
      }), error.status_code


  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)