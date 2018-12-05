# Pizza store. Internet shop.

Internet shop for selling food online.

This is an example of Django project for learning and practicing Python language.

This project can be used by all who want to get more experience in programming.  

Using it in the production environment is only under your responsibility because it was created exclusively for educational purposes.

[DEMO](http://pizza.webmonstr.com:8888/)

For all questions please contact me zdimon77@gmail.com


## Platform

- Python 3
- Django 2

## Requirements (Ubuntu 16)

    sudo apt-get install python3-venv git npm python3-pip
    

## Installation
    
    git clone git@github.com:zdimon/pizza_store.git ; cd pizza_shop
    python3 -m venv myvenv --without-pip --system-site-packages
    ./bin/install
    
Run server

    ./bin/serv
    
## Possible problems.	
	
### If you get this error.

<p style="color: red">locale.Error: unsupported locale setting.</p>
	
	dpkg-reconfigure locales

Then select ru and us UTF-8.
