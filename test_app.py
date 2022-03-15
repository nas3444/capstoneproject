from email import header
from math import prod
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor
from config import DatabaseURI, assistant_token, director_token, producer_token

class CastingAgencyTestCase(unittest.TestCase):

    # to setup the app and initialize the db
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = DatabaseURI.SQLALCHEMY_DATABASE_URI
        
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    # to kill after each test
    def tearDown(self):
        pass

    #Tests - Successed

    # test for getting all movies/ role assistant 
    def test_get_movies(self):
        headers = {
            'Authorization': 'Bearer {}'.format(assistant_token)
        }
        res = self.client().get('/movies', headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    # test for getting all actors / role assistant
    def test_get_actors(self):
        headers = {
            'Authorization': 'Bearer {}'.format(assistant_token)
        }
        res = self.client().get("/actors", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    # test for posting a new movie / role producer
    def test_post_movie(self):
        headers = {
            'Authorization': 'Bearer {}'.format(producer_token)
        }
        res = self.client().post("/movies", headers=headers, json={"title":"vhh", "image":"https://pbs.twimg.com/media/FHfNybWWYAEFME7.png", "release_date":"2022-02-02"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for posting a new actor / role director
    def test_post_actor(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().post("/actors", headers=headers, json={"name":"998", "age":90, "gender":"male"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for patching a specific movie / role director
    def test_patch_movie(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().patch("/movies/5", headers=headers, json={"title":"ffff"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for patching a specific actor / role producer
    def test_patch_actor(self):
        headers = {
            'Authorization': 'Bearer {}'.format(producer_token)
        }
        res = self.client().patch("/actors/10", headers=headers, json={"name":"dddr"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for deleting a specific movie / role producer
    def test_delete_movie(self):
        headers = {
            'Authorization': 'Bearer {}'.format(producer_token)
        }
        res = self.client().delete("/movies/7", headers=headers)
        data = json.loads(res.data)

        movie = Movie.query.get(7)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(movie, None)

    # test for deleting a specific actor / role director
    def test_delete_actor(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().delete("/actors/11", headers=headers)
        data = json.loads(res.data)

        actor = Actor.query.get(11)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(actor, None)

    # Tests - failed (Authorized)

    # Testing case for deleting a non existed movie / role producer
    def test_non_exist_movie(self):
        headers = {
            'Authorization': 'Bearer {}'.format(producer_token)
        }
        res = self.client().delete("/movies/40000", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing case for deleting a non existed actor / role director
    def test_non_exist_actor(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().delete("/actors/900", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing case for patching a non existed movie / role producer
    def test_non_exist_movie(self):
        headers = {
            'Authorization': 'Bearer {}'.format(producer_token)
        }
        res = self.client().patch("/movies/200", headers=headers, json={"title": "NO"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing case for patching a non existed actor / director
    def test_non_exist_actor(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().patch("/actors/200", headers=headers, json={"name": "NO"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing case for  posting an invalid movie / producer
    def test_422_invalid_movie(self):
        headers = {
            'Authorization': 'Bearer {}'.format(producer_token)
        }
        res = self.client().post("/movies", headers=headers, json={"title": "", "image": "", "release_date":""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing case for posting an invalid actor / director
    def test_invalid_actor(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().post("/actors", headers=headers, json={"name":"", "age":"", "gender":""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Testing case for 404 error - not found route / assistant
    def test_404_not_found(self):
        headers = {
            'Authorization': 'Bearer {}'.format(assistant_token)
        }
        res = self.client().get("/movie", headers=headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # Tests for RBAC - Unauthorized
    def test_unauthorized_assistant(self):
        headers = {
            'Authorization': 'Bearer {}'.format(assistant_token)
        }
        res = self.client().patch('/movies', headers=headers, json={"title": "unauthorized"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unauthorized")

    def test_unauthorized_director(self):
        headers = {
            'Authorization': 'Bearer {}'.format(director_token)
        }
        res = self.client().post('/movies', headers=headers, json={"title": "bkb", "image": "ff", "release_date": "2020-02-02"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unauthorized")

    
if __name__ == "__main__":
    unittest.main()