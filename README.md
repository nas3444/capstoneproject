

<h1 align="center">Capstone</h1>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Capstone 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/nas3444" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Final project for Udacity Fullstack Web Developer (Capstone). It is a Casting Agency that is responsible for creating movies and managing and assigning actors to those movies. 
It has three roles assistant, director and producer. Each role has different permissions to access. The final application is deployed on Heroku.

## :sparkles: Features ##

:heavy_check_mark: Movies and Actors can be viewed in the application by assistant, director and producer;\
:heavy_check_mark: Movies can be added to the application by producer;\
:heavy_check_mark: Actors can be added to the application by director and producer;\
:heavy_check_mark: Movies can be deleted from the application by producer;\
:heavy_check_mark: Actors can be deleted from the application by director and producer;\
:heavy_check_mark: Movies and Actors can be edited in the application by director and producer;\
:heavy_check_mark: The application follows RBAC for role-permissions and required access tokens for each role to do specific actions;\
:heavy_check_mark: The application is deployed live on Heroku;


## :rocket: Technologies ##

The following tools were used in this project:



## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and [Posrgresql](https://www.postgresql.org/download/) installed.

## :checkered_flag: Starting ##
### Local ###

```bash
# Clone this project
$ git clone https://github.com/nas3444/capstone_heroku

# Access
$ cd capstone_heroku

# Create a virtual environment
$ python3 -m venv myvenv
$ source myvenv/bin/activate

# Set up the environment variables
$ chmod +x setup.sh
$ source setup.sh

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ python3 app.py

# The server will initialize in the <http://127.0.0.1:5000/>
```

### Deploying to Heroku ###

```bash
# Clone this project
$ git clone https://github.com/nas3444/capstone_heroku

# Access
$ cd capstone_heroku

# Create a virtual environment
$ python3 -m venv myvenv
$ source myvenv/bin/activate

# Set up the environment variables
$ chmod +x setup.sh
$ source setup.sh

# Install dependencies
$ pip install -r requirements.txt

# Login to Heroku
$ heroku login -i

# Initialize Git
# Run it just once, in the beginning
$ git init
# For the first time commit, you need to configure the git username and email:
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"

# Every time you make any edits to any file in the web_app folder
$ git add .
# Check which files are ready to be committed
$ git status
$ git commit -m "your message"

# Create an app in the Heroku Cloud
$ heroku create [my-app-name] --buildpack heroku/python

# Checking the remote repository was added to git
$ git remote -v
# if not add it by
$ git remote add heroku [heroku_remote_git_url]

# Add PostgreSQL addon for our database
$ heroku addons:create heroku-postgresql:hobby-dev --app [my-app-name]

# Configure the App
$ heroku config --app [my-app-name]

# Additional Environment Variables
# add to the application in Heroku > settings > a new variable "EXICTED" with value true.

# after commiting all changes in local
# PUSH IT to Heroku
$ git push heroku master


# The server will initialize in the Heroku Cloud
```

## :link:	Hosted Application

https://capstone-herokuapp.herokuapp.com/

## :key: Authentication ##

All tokens for roles are fresh and existed in the config file of the project.
Also, a collection of postman with the token included in the project folder with a name capstoneherokucollection.json

## :globe_with_meridians: API ## 

### GET '/movies'
* Permission: Assistant, Director, and Producer
* Returns a list of movies in DB
* Request parameters: None
* Response body:
```
{
    "movies": [
        {
            "id": 1,
            "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSfDizH3R69OMtvuSE3i_mEsTK0LWl7tYV-LKdOk3aD1D3_CluT",
            "release_date": "Fri, 08 Jan 1999 04:05:06 GMT",
            "title": "Movie1"
        },
        {
            "id": 2,
            "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSfDizH3R69OMtvuSE3i_mEsTK0LWl7tYV-LKdOk3aD1D3_CluT",
            "release_date": "Fri, 08 Jan 1999 04:05:06 GMT",
            "title": "Movie2"
        }
    ],
    "success": true
}
```

### GET '/actors'
* Permission: Assistant, Director, and Producer
* Returns a list of actors in DB
* Request parameters: None
* Response body:
```
{
    "actors": [
        {
            "age": 30,
            "gender": "female",
            "id": 1,
            "movie_id": null,
            "name": "actor1"
        },
        {
            "age": 27,
            "gender": "male",
            "id": 2,
            "movie_id": null,
            "name": "actor2"
        }
    ],
    "success": true
}
```

### POST '/movies'
* Permission: Producer
* Creates a new movie in DB
* Request parameters: a movie object containing title, image and release_date
* Response body:
```
{
    "success": true
}
```

### POST '/actors'
* Permission: Director and Producer
* Creates a new actor in DB
* Request parameters: an actor object containing name, age and gender
* Response body:
```
{
    "success": true
}
```

### PATCH '/movies/<int:id>'
* Permission: Director and Producer
* Updates the corresponding movie
* Request parameters: a movie object with all parameters or specific ones. 
* Response body:
```
{
    "success": true
}
```

### PATCH '/actors/<int:id>'
* Director and Producer
* Updates the corresponding actor
* Request parameters: an actor object with all parameters or specific ones. 
* Response body:
```
{
    "success": true
}
```

### DELETE '/movies/<int:id>'
* Permission: Producer
* deletes the corresponding movie
* Request parameters: None
* Response body:
```
{
    "success": true
}
```

### DELETE '/actors/<int:id>'
* Permission: Director and Producer
* deletes the corresponding actor
* Request parameters: None
* Response body:
```
{
    "success": true
}
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">{{YOUR_NAME}}</a>

&#xa0;

<a href="#top">Back to top</a>
