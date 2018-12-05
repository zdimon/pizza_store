##History

Create and activate virtualenv

	apt-get install python3-venv
	python3 -m venv ve
	
### If you see this

	The virtual environment was not created successfully because ensurepip is not
	available.	
	
	sudo apt-get install python3-pip
	python3 -m venv myvenv --without-pip --system-site-packages
	
	
### If you see this 

	locale.Error: unsupported locale setting
	
	dpkg-reconfigure locales

Then select ru and us UTF-8.
	
	
## Requirements

	Django
	
## Installation 

	django-admin startproject pizza
	cd pizza
	./manage.py startapp shop
	./manage.py migrate
	
## Create command of loading users

	mkdir shop/managements
	mkdir shop/managements/commands
	touch shop/managements/__init__.py; touch shop/managements/commands/__init__.py
	
	
## Skeleton

	from django.core.management.base import BaseCommand
	from django.utils import timezone

	class Command(BaseCommand):
		help = 'Displays current time'

		def handle(self, *args, **kwargs):
		    time = timezone.now().strftime('%X')
		    self.stdout.write("It's now %s" % time)	
		    
				
	from django.contrib.auth.models import User

	class Command(BaseCommand):

		def handle(self, *args, **kwargs):
		    print('Поехали')
		    for i in range(10):
		        u = User()
		        u.is_superuser = True
		        u.is_active = True
		        u.is_staff = True
		        u.set_password('123')
		        u.username = 'admin%s' % i
		        u.save()
		        print('Creating %s' % i)
		    print('Done')
		    
## Local bootstrap

	nmp install bootstrap	
	mkdir static	    
	cd static
	ln -s ../node_modules/bootstrap/dist bootstrap
		    
Add template dir
	
	cd ..
	mkdir templates		    

### main template templates/layout.html

	

	{% load staticfiles %}
	<!DOCTYPE html>
	<html lang="en" >
	<head>
		<meta charset="utf-8" />
		<title>{% block title %}Hello{% endblock %}</title>
		<link href="{% static 'bootstrap/css/bootstrap.min.css' %}" rel="stylesheet" type="text/css"/>
		<script src="{% static 'prj.js' %}"></script>
	</head>
	<body>
		<header>
		    <div class="navbar navbar-dark bg-dark shadow-sm">
		      <div class="container d-flex justify-content-between">
		        <a href="#" class="navbar-brand d-flex align-items-center">
		          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
		          <strong>Album</strong>
		        </a>
		        {% block header %}{% endblock %}
		      </div>
		    </div>
		  </header>
	  
		  <main role="main">
	  
		   
	  
		    <div class="album py-5 bg-light">
		      <div class="container">
		        {% block content %}{% endblock %}
		      </div>
		    </div>
	  
		  </main>
	  
		  <footer class="text-muted">
		    <div class="container">
		        {% block footer %}{% endblock %}
		    </div>
		  </footer>
	</html>

		   
Add template dir into settings.py

	TEMPLATES = [
		{
		    'BACKEND': 'django.template.backends.django.DjangoTemplates',
		    'DIRS': [os.path.join(BASE_DIR, 'templates')],
		    ...
	]
		    
		    
## Home page

URL

	from shop.views import home

	urlpatterns = [
    	path('', home, name='home'),		    
    ...
		    
View

	def home(request):
		return render(request,'shop/home.html')
		

## django-extensions
	
	echo 'django-extensions' >> ../requirements.txt
	echo 'werkzeug' >> ../requirements.txt
	pip install -r ../requirements.txt
		    
		    
	INSTALLED_APPS = [
		...
		'django_extensions'
	]		    
		    
		    
	./manage.py runserver_plus		    
	
	
Home template templates/shop/home.html	
		   
	mkdir templates/shop
	

	
	{% extends 'layout.html' %}

	{% block header %}
		<h1>Home page</h1>
	{% endblock %}

	{% block content %}
		<h1>Hello world</h1>
		<div class="row">
		    <div class="col-md-4">
		      <div class="card mb-4 shadow-sm">
		        
		        <div class="card-body">
		          <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
		          <div class="d-flex justify-content-between align-items-center">
		            <div class="btn-group">
		              <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
		              <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
		            </div>
		            <small class="text-muted">9 mins</small>
		          </div>
		        </div>
		      </div>
		    </div>
		    <div class="col-md-4">
		      <div class="card mb-4 shadow-sm">
		       
		        <div class="card-body">
		          <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
		          <div class="d-flex justify-content-between align-items-center">
		            <div class="btn-group">
		              <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
		              <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
		            </div>
		            <small class="text-muted">9 mins</small>
		          </div>
		        </div>
		      </div>
		    </div>
		    <div class="col-md-4">
		      <div class="card mb-4 shadow-sm">
		       
		        <div class="card-body">
		          <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
		          <div class="d-flex justify-content-between align-items-center">
		            <div class="btn-group">
		              <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
		              <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
		            </div>
		            <small class="text-muted">9 mins</small>
		          </div>
		        </div>
		      </div>
		    </div>
		  </div>     
    
{% endblock %}

{% block footer %}
    <h3>This is footer</h3>
{% endblock %}		
	
## Static serving (setting.py)

	STATICFILES_DIRS = [
		os.path.join(BASE_DIR, "static")
	]
	   
	
## Manual autorization

Form

            {% if user.is_authenticated %}
                    <ul class="navbar-nav ">
                    <li class="nav-item active">
                      <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                    </li>
                  </ul>
                
            {% else %}
            <form action="{% url 'login' %}" method="POST" class="form-inline mt-2 mt-md-0">
                    {% csrf_token %}
                    <input class="form-control mr-sm-2" type="text" name="login" placeholder="Login" aria-label="Search">
                    <input class="form-control mr-sm-2" type="text" name="password" placeholder="Password" aria-label="Search">
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">SignIn</button>
            </form>
            {% endif %}
	
	
		    
## Manual Autentication

URL

	path('login', login, name='login'),
    path('logout', logoutme, name='logout'),

	
View	
			    
	from django.contrib.auth.models import User
	from django.contrib.auth import authenticate, login as l

	def login(request):
		username = request.POST['login']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
		    l(request, user)
		    return redirect('home')
		else:
		    return redirect('home')

	def logoutme(request):
		logout(request)
		return redirect('home')
		
## Messages

	from django.contrib import messages		
	
	def login(request):
		...
		if user is not None:
		    l(request, user)
		    return redirect('home')
		else:
		    messages.error(request, 'Error!!!!')
		    return redirect('home')	
		    
		    
Template

     {% if messages %}
    
        {% for message in messages %}
        <div class="alert alert-danger" role="alert">
                {{ message }}
        </div>
        {% endfor %}
   
    {% endif %}		   
    
    
Styles

	class="alert alert-{{ message.tags }}"
	
		 
	from django.contrib import messages
	MESSAGE_TAGS = {
		messages.ERROR: 'danger',
	}				
				
## Manual registration

URL

	path('registration', registration, name='registration'),
				
Form				
		    


	<form action="{% url 'registration' %}" method="POST">
			{% csrf_token %}
		    <div class="form-group">
		      <label for="exampleInputEmail1">Username</label>
		      {{ form.username }}
		      <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
		    </div>
		    <div class="form-group">
		      <label for="exampleInputPassword1">Email</label>
		      {{ form.email }}
		    </div>
		    <div class="form-group">
		      <label for="exampleInputPassword1">Password</label>
		      {{ form.password }}
		      
		    </div>
		    <button type="submit" class="btn btn-primary">Submit</button>
	</form>


View

	def registration(request):
	 if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = RegForm(request.POST)
		# check whether it's valid:
		if form.is_valid():  
		    username = form.cleaned_data['username']
		    messages.success(request, 'Bingo %s !!!' % username)
		    return redirect('home')
		# if a GET (or any other method) we'll create a blank form
		else:
		    form = NameForm()








		    
		    
		    
