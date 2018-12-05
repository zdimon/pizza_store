# Pizza store. Internet shop.

Internet shop for selling food online.

This is an example of Django project for learning and practicing Python language.

This project can be used by all who want to get more experience in programming.  

Using it in the production environment is only under your responsibility because it was created exclusively for educational purposes.

For all questions please contact me zdimon77@gmail.com


## Platform

- Python 3
- Django 2

## Installation
    
    git clone git@github.com:zdimon/pizza_store.git
  	apt-get install python3-venv
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    cd pizza_shop
    ./bin/install
    
Run server

    ./bin/serv
    
## Possible problems.

### If you get this error.

<p style='color:red'>The virtual environment was not created successfully because ensurepip is not
available.</p>

	
	sudo apt-get install python3-pip
	python3 -m venv myvenv --without-pip --system-site-packages
	
	
### If you get this error.

<p style="color: red">locale.Error: unsupported locale setting.</p>
	
	dpkg-reconfigure locales

Then select ru and us UTF-8.
