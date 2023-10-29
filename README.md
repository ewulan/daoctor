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

* Install dependencies by running
  * pip install -r requirements.txt
    
* Start up the server by running
  * python app.py serve
    * Allow Python through the firewall as needed to enable your application to communicate with other computers or servers.

    
* Visit http://hostIP:5000/ to explore and test.
  The hostIP is the address of the running host. Or you can find it in Powershell:
  ![](https://github.com/ewulan/daoctor/blob/master/static/images/visit.png)
