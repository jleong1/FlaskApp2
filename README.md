# FlaskApp2
This is another version of our FeelsApp with an updated and more modular structure of the app.

This app was created with flask via virtualenv following tutorials created by [Lalith Polepeddi](https://github.com/lpolepeddi) before being modified. - *P.s: Thanks Lalith!*

### **Before cloing this git!**  
Here are some linux-based commands required to have the app set up for development. 

##### **NOTICE !!**  
*If you're running Windows, follow the "Installation Instructions" on [this link](https://pypi.python.org/pypi/setuptools) to get easy_install up and running on your computer.*

##### Installing virtualenv
If you already have virtualenv installed on your system, 
you will see a version number. Do the following command to check:  

```sh
$ sudo easy_install virtualenv
```  
or:
```sh
$ sudo pip install virtualenv
```  
or:
```sh
$ sudo apt-get install python-virtualenv
```

##### Installing Flask
After installing virtualenv, do the following command:

```sh
$ virtualenv flaskapp
```
This creates a new isolated development environment in your current directory.  
Then, make the new dev-env your present working directory like so:
```sh
$ cd flaskapp
$ . bin/activate
```
Finally, install Flask:
```sh
$ pip install Flask
```
##### ***WAIT !!***  
Here are some additional flask components/frameworks that must be installed to have the app working correctly after cloning this git later:

```sh
$ pip install flask-wtf
$ pip install flask-mail
```

##### ***Finally...*** 
You may clone this git to your ***isolated development*** `flaskapp` *folder*.  

##### ***Don't forget...***  
To continue developing this app in an ***isolated environment*** in the `flaskapp` folder, remember always to do the following command:
```sh
$ . bin/activate
```  
###### ***Also...***  
To have the contact page notify you at your personal email address, remember to change the following lines in [routes.py](/routes.py) to an actual existing email login info.
```python
app.config["MAIL_USERNAME"]='your-username@gmail.com'  app.config["MAIL_PASSWORD"]='your-password'
```# FlaskApp2
