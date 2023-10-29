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

* Install dependencies by running
  * pip install -r requirements.txt.
    
* Start up the server by running
  * python app/server.py serve.
  * 
* Visit http://localhost:8080/ to explore and test.
