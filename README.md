daoctor : 
 Plant Disease Detection
------------------------
 
## Local Set-Up

### Local:
* It is recommended to set up the project inside a virtual environment to keep the dependencies separated.

  * Python : 3.8
  * Conda

* Create and activate your virtual environment.
  * conda create -n pdd python=3.8
  * conda env list
  * conda activate pdd
    
    * If the environment is no longer needed, remove the command: conda remove -n pdd --all
 
* Download the Plant Disease Detection app
  * cd \daoctor
  * 
* In config.py, change the database to an absolute path:
  * SQLALCHEMY_DATABASE_URI='sqlite:///./database/daoctor.sqlite3'

* Install dependencies by running
  * pip install -r requirements.txt.
    
* Start up the server by running
  * python app.py serve.
  * 
* Visit http://localhost:8080/ to explore and test.
