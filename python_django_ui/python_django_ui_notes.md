## Dev

#### What is Django?    
Django is a high level framework.    
It has specific way of doing things.    
Hence development is fast with its tools and there are less errors.    
It has security, authentication and administration.    
It is scalable.    
It can use any database. sqlite3 is fine for development but use mongodb, postgresql or mysql in prod.    
    
#### What is the concept of django?    
Website is a project and there are many apps and corresponding dirs inside it like: blog, store, static pages etc    
    
#### What are the pre-requisites of django?    
Download and install python from python.org.    
Create a base directory and navigate to it.    
Create a virtual environment and activate it.    

#### P.S. If you cannot install postgres db on dev box, just use sqlite3 which does not need any installation
#### If you use sqlite3, skip the settings explained for postgres in below dev sections
    
#### What are the db pre-requisites of django?   
Download and install postgresql from https://www.postgresql.org/.    
Download and install pgadmin from https://www.pgadmin.org/ to access db as GUI. (optional)    
Login with postgres user and password.    
```
pip install psycopg2  
pip install psycopg2-binary  
```
      
#### What are the postgres db commands?    
```Create database (dbname) owner (username);``` - username is postgres as of now    
```\q``` - logout    
    
#### What are all the django commands?
```pip install django```  
```python -m pip install --user Pillow``` - for image field  
```python -m pip install --user pylint-django``` - optional  
  
```django-admin help```
```django-admin startproject (projectname) .```
  
```python manage.py help```
```python manage.py startapp (appname)```
```python manage.py runserver```
```python manage.py collectstatic```
```python manage.py makemigrations```
```python manage.py sqlmigrate (appname) (migrationsfilename)``` - shows sql queries that'll be performed    
```python manage.py migrate```  
```python manage.py createsuperuser - name - email - password``` (can login to admin area having users and groups by default)    
    
#### What are all the files created by django?
```
base dir-->
db.sqlite3
    explanation:
        created when we run server - can be deleted as we'll use better db
manage.py-->
    explanation:
        created automatically at start
project dir
    static dir
        explanation:
            create on our own
        css dir:
            explanation:
                create on our own
            css file
                explanation:
                    get created from someone
        js dir:
            explanation:
                create on our own
            js file
                explanation:
                    get created from someone
        webfonts dir:
            explanation:
                create on our own
            webfonts file
                get created from someone
        img dir
            explanation:
                create on our own
            image file
                explanation:
                    get created from someone (logo etc)
    settings.py
        explanation:
            base_dir - of project
            secret_key - for prod
            debug flag - which should be True in Dev and False in prod
            allowed_hosts - domains this website can serve
            installed_apps - default apps at start i.e. admin, auth, sessions etc , django.contrib.humanize for , in int
            middleware - usedby django for security etc
            root_urlconf - main urls file path
            templates - path of templates for generating html to be displayed to user
            wsgi_application - path of wsgi app used by django's builtin server
            databases - default sqlite3 db info - we can change
            auth_password_validators - rules for password
            language_code
            time_zone
            static_url - path for static files like css, js, images
        syntax:
            variablename=list/string value
            new app is added as (appname).apps.(appsclassname)
            templates location is mentioned as os.path.join(BASE_DIR, 'templates') in Templates-->Dirs
            static paths are added as:
            STATIC_ROOT = os.path.join(BASE_DIR, 'static') (below static files & admin static files will be copied here during deployment via collectstatic)
            STATICFILES_DIRS = [os.path.join(BASE_DIR, '(projectdir)/static')]
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media') (for photos)
            MEDIA_URL = '/media/'
            for alert messages:
            from django.contrib.messages import constants as messages
            MESSAGE_TAGS = {messages.INFO: ''}
            change to: MESSAGE_TAGS = {messages.ERROR: 'danger'}
    urls.py
        explanation:
            for routing
            has url and linked view method
            has admin url by default
            each app has separate urls.py just like admin
            they are collected here, just like admin
        syntax:
            app url is put as:
            from django.urls import include
            path('', include('(appname).urls')
            to show images on front end:
            from django.conf import settings
            from django.conf.urls.static import static
            + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    wsgi.py
        explanation:
            web server gateway interface
            describes how web server communicates with webapp and how webapps can be chained together to process a request
            it is for hosting site for other people to access i.e. for deployment
app dir
    migrations
        (n_xx).py
            explanation:
                gets created when we make db migrations after db related changes like addition of tables, columns, datatypes etc
                (there are default migrations for auth and admin i.e. migrations files are already created but we need to run them)
    models.py
        explanation:
            for creating data models as per requirement
        syntax:
            from datetime import datetime
            from (otherapp).models import (othermodelclass)
            class (Modelname)(models.Model):
                # (int autoincrement id gets added by default)
                (fieldname) = models.ForeignKey(othermodelclass, on_delete=models.DO_NOTHING)
                (fieldname) = models.CharField(max_length=200)
                (fieldname) = models.TextField(blank=True)
                (fieldname) = models.IntegerField(default=0)
                (fieldname) = models.DecimalField(max_digits=2, decimal_places=1)
                (fieldname) = models.BooleanField(default=True)
                (fieldname) = models.DateTimeField(default=datetime.now, blank=True).order_by('(other_field_name)').reverse().filter((other_field_name))=True)[:3]
                (fieldname) = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) - refers media folder
                 def __str__(self):  # for showing in admin area as a list of (fieldname)s else it will show object 1 object 2
                    return self.(fieldname)
    tests.py
        explanation:
            for running tests
    views.py
        explanation:
            methods that are linked to urls
        syntax:
            from .models import (modelclassname)
            from django.http import HttpResponse
            def (purposemethodname)(request):
                data = (modelclassname).objects.all
                context = {'data': data}
                return render(request, '(appname)/(templatefilename)', context)
            if url sends parameter, accept same in views method
            pagination:
            from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
            def index(request):
                data = (modelclassname).objects.all
                paginator = Paginator(data, 2)
                page = request.GET.get('page')
                paged_data = paginator.get_page(page)
                context = {'data': paged_data}
                return render(request, '(appname)/(templatefilename)', context)
            for single item route:
            from django.shortcuts import get_object_or_404
            item = get_object_or_404((modelclassname), pk=(parameterpassedbyurl))
            context = {'item': item}
            access form inputs from GET request as:
            if keywords in request.GET:
                keywords = request.GET['keywords']
                if keywords:  # not empty check
                    queryset_list = queryset_list.filter(description__icontains=keywords)
            preseve values of form after clicking button
            'values': request.GET to context
            redirect to url as return redirect('urlname')
            check request method as if request.method == "POST"
            display messages as:
            from django.contrib import messages
            messages.error(request, 'testing error msg')
            register user as:
            from django.contrib.auth.models import User
            from django.contrib import auth
            def register(request):
                if request.method == "POST":
                    first_name = request.POST['first_name']
                    last_name = request.POST['last_name']
                    username = request.POST['username']
                    email = request.POST['email']
                    password = request.POST['password']
                    password2 = request.POST['password2']
                    if password == password2:
                        if User.objects.filter(username=username).exists():
                            messages.error(request, 'That username is taken')
                            return redirect('register')
                        else:
                            if User.objects.filter(email=email).exists():
                                messages.error(request, 'That email is being used')
                                return redirect('register')
                            else:
                                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                                user.save()
                                messages.success(request, 'You are now registered and can log in')
                                return redirect('login')
                    else:
                        messages.error(request, 'Passwords do not match')
                        return redirect('register')
                else:
                    return render(request, '(template)')
            login as:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
    apps.py
        explanation:
            app class name
    urls.py
        explanation:
            need to create on our own for app specific urls
        syntax:
            from django.urls import path
            from . import views
            urlpatterns = [path('', views.(viewsmethodname), name='(urlname)')]
            urlpatterns = [path('(purposeurlpart)', views.(viewsmethodname), name='(urlname)')]
            path('(<daatype):(dynamicparameter)>', views.(viewmethodname), name='(routename)')
    admin.py
        explanation:
            to register our app's model on admin area and edit how its displayed
        syntax:
            from .models import (Modelclassname)
            class ListingAdmin(admin.ModelAdmin):
                list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
                list_display_links = ('id', 'title')
                list_filter = ('realtor',)
                list_editable = ('is_published',)
                search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
                list_per_page = 25
            admin.site.register(Listing, ListingAdmin)
templates dir
    explanation:
        we have to create on our own
    partials dir
        explanation:
            we have to create on our own
            partial html content that can be included in other templates like base.html for clarity
        _(common_section).html
            explanation:
                we have to create on our own
            syntax:
                {% load static %} if required
                current link is highlighted as:
                <li {% if '(urlword)' in request.path %} class="nav-item active mr-3"  {% else %} class="nav-item mr-3" {% endif %}> (use if '/' for root)
                read alert messsages as:
                {% if messages %}
                    {% for message in messages %}
                        <div id="message" class="container">
                            <div class="alert alert-{{ message.tags }} alert-dismissible text-center" role="alert">
                                <button class="close" type="button" data-dismiss="alert"><span aria-hidden="true">&times;</span></button>
                                <strong>
                                    {% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}
                                        Error:
                                    {% else %}
                                        {{ message.tags|title }}
                                    {% endif %}
                                </strong>
                                {{ message }}
                            </div>
                        </div>
                    {% endfor %}
            {% endif %}
            check if user is authenticated as:
            {% if user.is_authenticaed %}
                hello
            {% else %}
                (all content)
            {% endif %}
    base.html
        explanation:
            common html layout for multiple other templates
            will include formatting from css and js static files and include html content for topbar, navbar and footer
        syntax:
            {% load static %}
            (css jss static files referring - not included on purpose)
            common content like title
            {% block content%} {% endblock %} - placeholder for each template's unique content
            {% include 'partials/(common_section).html' %}
            for page titles:
            <title>Real Estate {% block title %}{% endblock %}</title>
    app dir
        explanation:
            we have to create on our own
        purpose html
            explanation:
                we have to create on our own
            syntax:
                {% extends 'base.html' %} - common content
                {% block content %}unique html content for this page{% endblock %}
                {% load static %} if required
                other page url is passed to href link as: <a class="nav-link" href="{% url '(urlname)' %}">(optionallinkname)</a>
                {% load humanize %} if required
                loop over entries from context as:
                {% if data %}
                  {% for item in data %}
                        "{{ item.(photofieldname).url }}"
                        ${{ item.(pricefieldname)|intcomma }}
                        {{ item.(normalstringfieldname) }}
                        {{ item.(datefieldname) | timesince }}
                  {% endfor %}
                {% else %}
                    <p>No data Available</p>
                {% endif %}
                going to a particular element like:
                <a href="{% url '(routenameforasingleelement)' item.(fieldname) %}" class="btn btn-primary btn-block">More Info</a>
                pagination:
                  {% if data.has_other_pages %}
                    <ul class="pagination">
                      {% if data.has_previous %}
                        <li class="page-item">
                          <a href="?page={{data.previous_page_number}}" class="page-link">&laquo;</a>
                        </li>
                      {% else %}
                        <li class="page-item disabled">
                          <a class="page-link">&laquo;</a>
                        </li>
                      {% endif %}
                      {% for i in data.paginator.page_range %}
                        {% if data.number == i %}
                          <li class="page-item active">
                            <a href="" class="page_link">{{i}}</a>
                          </li>
                        {% else %}
                          <li class="page-item">
                            <a href="?page={{i}}" class="page-link">{{i}}</a>
                          </li>
                        {% endif %}
                      {% endfor %}
                       {% if data.has_next %}
                        <li class="page-item">
                          <a href="?page={{data.next_page_number}}" class="page-link">&raquo;</a>
                        </li>
                      {% else %}
                        <li class="page-item disabled">
                          <a class="page-link">&raquo;</a>
                        </li>
                      {% endif %}
                    </ul>
                  {% endif %}
                go over key value pairs from context as:
                {% for key, value in satte_choices.items %}
                  <option value={{ key }}>{{value}}</option>
                {% endfor %}
                (name attribute of html goes to url)
                preserve inputs of form after clicking button
                value="{{values.keywords}}"
                when you do post, tie form to user session to prevent cross site forgery
                <form action="{% url 'register' %}" method="POST">
                {% csrf_token %}
                logout as:
                <l1 class="nav-item mr-3">
                    <a href="javascript:{document.getElementById('logout').submit()}" class="nav-link">
                        <i class="fas fa-sign-out-alt"></i> Logout
                    </a>
                    <form action="{% url 'logout' %}" method="POST" id="logout">
                        {% csrf_token %}
                        <input type="hidden">
                    </form>
                </l1>
                for title:
                {% block title %} | Welcome {% endblock %}
    admin dir:
        explanation:
            we have to create on our own
        base_site.html
            explanation:
                common html content for admin area
            syntax:
                {%  extends 'admin/base.html' %}
                {% load static %}
                {% block branding %}
                (common content)
                {% endblock %}
                static files are referred in html as "{% static '(foldername)/(filename)' %}"
                add images, add css styling from admin.css - syntax not included on purpose
media dir
    explanation:
        created when pic is uploaded via admin area - further structure - /photos/year/month/day/photos
```
   
#### What are the further requirements to save code remotely on git?    
Download and install git from git-scm.com.    
create .gitignore file with venv and django contents from gitignore.io. make media as /media.    
go to github on browser - create new repo - give project name    
    
#### What are all the git commands?  
```
git init
git add .
git commit -m '(message)'
git remote add origin https://github.com/SmitaPatankar/DjangoUI.git
git push -u origin master
```
  
#### What are the urls of django app?  
```
localhost:8000 front end
localhost:8000/admin admin area
```
  
## Deployment  
  
#### Generate ssh keys on windows  
```cd ~```
```ssh-keygen```
Private and public keys will get generated in ```./.ssh/id_rsa_do```.  
  
#### Login to linux server with root user  
```ssh root@(ip)```  
  
#### Add ssh identity to linux server  
```ssh-add ./.ssh/id_rsa_do```  
  
#### Create djangoadmin user  
```adduser djangoadmin```  
  
#### Add djangoadmin user to djangoadmin group  
```usermod -aG sudo djangoadmin```  
  
#### Add our windows public key to linux server  
```
cd /home/djangoadmin
mkdir .ssh
cd .ssh
vi authorized_keys
```
put our public key  
```
exit
```
  
#### Login to linux server with djangoadmin user  
```ssh djangoadmin@(ip)```
  
#### Edit sshd_config to disable root login  
```
sudo vi /etc/ssh/sshd_config
```
Permitrootlogin - no  
passwordauthentcication - no  
  
#### Reload sshd service  
```
sudo systemctl reload sshd
```
  
#### Update firewall settings to Allow OpenSSH  
```
sudo ufw allow OpenSSH
```
  
#### Enable firewall  
```sudo ufw enable```
  
#### Update packages  
```sudo apt update```  
```sudo apt upgrade```  
  
#### Install packages needed for deployment  
```sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl```  
  
#### Perform postgres db operations as postgres user  
```sudo -u postgres psql (postgres is default user)```  
  
#### Create db for our project  
```CREATE DATABASE realestate_prod;```  
  
#### Create dbadmin user  
```CREATE USER dbadmin WITH PASSWORD 'abc123!';```  
  
#### Set default encoding, tansaction isolation scheme (Recommended from Django)  
```
ALTER ROLE dbadmin SET client_encoding TO 'utf8';  
ALTER ROLE dbadmin SET default_transaction_isolation TO 'read committed';  
ALTER ROLE dbadmin SET timezone TO 'UTC';  
```

#### Grant permission to dbadmin user for our project  
```GRANT ALL PRIVILEGES ON DATABASE realestate_prod TO dbadmin;```  
  
#### Come out of db operations  
```\q```  

#### Install venv  
```sudo apt install python3-venv```  
  
#### Make main directory for our project and navigate to it  
```
cd ~  
mkdir pyapps  
cd pyapps  
```
  
#### Create virtualenv and source it  
```
python3 -m venv ./venv  
source ./venv/bin/activate  
```
  
#### Clone our code from github  
```git clone https://github.com/SmitaPatankar/DjangoUI.git```  
Enter username and pwd  
  
#### Navigate to project directory  
```cd realestate_project```  
  
#### Install requirements.txt modules  
```pip install -r requirements.txt```  
  
#### Navigate to the main child folder of our project  
cd realestate  
  
#### Local Settings Setup  
```sudo vi local_settings.py```  
copy secret key, debug and allowed hosts syntax from our dev settings  
edit secret key to something else  
make debug false  
add ip of our server to allowed hosts  
copy db stuff  
enter user and pwd as per server and db name and email  
  
#### Run Migrations  
```  
python manage.py makemigrations
python manage.py migrate
```  
  
#### Create superuser  
```python manage.py createsuperuser (username)``` - brad  
enter email - brad@gmail.com  
enter password - abc123!  
enter y  
  
#### Create static files  
```python manage.py collectstatic```  
  
#### Update firewall rules  
```sudo ufw allow 8000```  
  
#### Run server  
```python manage.py runserver 0.0.0.0:8000```  
  
#### Test the website  
  
#### Install gunicorn  
```pip install gunicorn```  
  
### Test Gunicorn serve from main folder where wsgi.py is  
```gunicorn --bind 0.0.0.0:8000 realestate.wsgi```  
  
#### Make gunicorn.socket file  
```
sudo nano /etc/systemd/system/gunicorn.socket
```
```
[Unit]
Description=gunicorn socket
[Socket]
ListenStream=/run/gunicorn.sock
[Install]
WantedBy=sockets.target
```
  
#### Make gunicorn.service file  
```sudo nano /etc/systemd/system/gunicorn.service```
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
[Service]
User=djangoadmin
Group=www-data
WorkingDirectory=/home/djangoadmin/pyapps/realestate_project
ExecStart=/home/djangoadmin/pyapps/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          realestate.wsgi:application
[Install]
WantedBy=multi-user.target
```
  
#### Start gunicorn socket  
```
sudo systemctl start gunicorn.socket  
```
  
#### Enable gunicorn socket  
```
sudo systemctl enable gunicorn.socket  
sudo systemctl status gunicorn.socket  
```
  
#### Check the existence of gunicorn.sock  
```file /run/gunicorn.sock```  
  
#### Create nginx file for our project  
```sudo nano /etc/nginx/sites-available/realestate_project```  
```
server {
    listen 80;
    server_name YOUR_IP_ADDRESS;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/djangoadmin/pyapps/realestate_project;
    }
    location /media/ {
        root /home/djangoadmin/pyapps/realestate_project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
  
#### Enable the file by linking to the sites-enabled dir  
```sudo ln -s /etc/nginx/sites-available/realestate_project /etc/nginx/sites-enabled```  
  
#### Test NGINX config  
```
sudo nginx -t  
```

#### Restart nginx  
```
sudo systemctl restart nginx  
```
  
#### Remove port 8000 from firewall and open up our firewall to allow normal traffic on port 80  
```
sudo ufw delete allow 8000  
sudo ufw allow 'Nginx Full'  
```
  
#### up the max upload size to be able to create listings with images in nginx.conf file  
```sudo nano /etc/nginx/nginx.conf```
```client_max_body_size 20M;``` to the http area  
  
#### Reload NGINX  
```sudo systemctl restart nginx```  
  
#### Test website  
  
#### Domain Setup  
on www.namecheap.com - advancedns - add arecord  
host - @ip  
cname record - host www, target - realestate.co  
check check box  
delete others  
  
#### Add domain to allowed hosts in settings.py  
'realestate.co', 'www.realestate.co'  
  
#### Edit /etc/nginx/sites-available/realestate_project to add domain name  
```sudo vi /etc/nginx/sites-available/realestate_project```  
```
server {
    listen: 80;
    server_name xxx.xxx.xxx.xxx realestate.co www.realestate.co;
}
```
  
#### Reload nginx  
```sudo systemctl restart nginx```  
  
#### Reload gunicorn  
```sudo systemctl restart gunicorn```  