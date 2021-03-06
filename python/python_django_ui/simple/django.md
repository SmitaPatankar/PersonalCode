```  
pip install django  
django-admin startproject {projectname}  
python manage.py createsuperuser  # user password  
python manage.py startapp {appname}  
```  
- install app in main settings  
- include app urls in main urls  
- map app views in app urls  
- create app models fields and overwrite string representation  
- customize app admin model and register app model and app admin model in app admin  
- copy app static css file in app static  
- create app includes html templates  
- create header app html template in app templates using css and js and db values and includes templates  
- create body app html template in app templates using css and js and db values and includes templates by extending header  
- accept request and return response, show messages, save db data, redirect in app views by rendering template and using request and model fields and auth forms and func  
```  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver  
```  
- add some db entries from admin page  
  
-----  
```  
python manage.py sqlmigrate main 0001  
```  
```  
python manage.py shell  
```  
  
```  
from main.models import Tutorial  
print(Tutorial.objects.all())  
from django.utils import timezone  
new_tutorial = Tutorial(tutorial_title="To be", tutorial_content="...or not to be", tutorial_published=timezone.now())  
new_tutorial.save()  
for t in Tutorial.objects.all():  
  print(t.tutorial_title)  
```  
  
-----  
  
```  
apt-get update  
apt-get install -y python3-pip  
python3 -m pip install --upgrade pip  
python3 -m pip install django  
mkdir /var/www/  
cd  /var/www  
  
wget urfiles  
apt-get install unzip  
unzip xx  
  
vi mysite/mysite/settings.py  
DEBUG=False  
ALLOWED_HOSTS = ['serverdnsname']  
STATIC_ROOT='/static/'  
MEDIA_URL='/media/'  
MEDIA_ROOT='/var/www/mysite/media/'  
  
python3 mysite/manage.py collectstatic  
  
cd mysite  
vi mysite/urls.py  
python3 mysite/manage.py startapp main  
vi main/urls.py  
  
# webserver->wsgi->django  
apt-get install -y apache2 libapache2-mod-wsgi.py3  
vi /etc/apache2/sites-available/mysite.conf  
  
<VirtualHost *:80>  
    ServerName DNSNAMEOFOURSERVER  
  
    ErrorLog ${APACHE_LOG_DIR}/mysite-error.log  
    CustomLog ${APACHE_LOG_DIR}/mysite-access.log combined  
  
    WSGIDaemonProcess mysite processes=2 threads=25 python-path=/var/www/mysite  
    WSGIProcessGroup mysite  
    WSGIScriptAlias / /var/www/mysite/mysite/wsgi.py  
  
    Alias /robots.txt /var/www/mysite/static/robots.txt  
    Alias /favicon.ico /var/www/mysite/static/favicon.ico  
    Alias /static/ /var/www/mysite/static/  
    Alias /static/ /var/www/mysite/media/  
  
    <Directory /var/www/mysite/mysite>  
        <Files wsgi.py>  
            Require all granted  
        </Files>  
    </Directory>  
  
    <Directory /var/www/mysite/static>  
        Require all granted  
    </Directory>  
  
    <Directory /var/www/mysite/media>  
        Require all granted  
    </Directory>  
</VirtualHost>  
  
a2ensite mysite  
systemctl reload apache2  
rm /etc/apache2/sites-available/000-default.conf  
vi /etc/apache2/sites-available/000-default.conf  
  
<VirtualHost *:80>  
    ServerName _  
    Redirect 404 /  
</VirtualHost>  
  
systemctl reload apache2  
```  
  
-----  
  
```  
cd ../  
chown www-data mysite/  
chown www-data mysite/db.sqlite3  
systemctl reload apache2  
  
letsencrypt.org  
  
apt-get update  
  
apt-get install git  
  
cd {projectdir}  
  
git clone https://github.com/letsencrypt/letsencrypt  
  
cd letsencrypt  
  
./letsencrypt-auto --help  
  
service nginx stop  
  
./letsencrypt-auto certonly --standalone -d psyber.io  
  
sudo vi /etc/nginx/sites-available/django  
comment port 80 listening  
listen 443 ssl;  
server_name psyber.io www.psyber.io;  
ssl_certificate /etc/letsencrypt/live/psyber.io/fullchain.pem;  
ssl_certificate_key /etc/letsencrypt/live/psyber.io/privkey.pem;  
server {listen 80;  
server_name psyber.io;  
return 301 https://$host$request_uri;  
}  
  
service nginx restart  
  
apache in doc  
  
pip install pillow  
  
ImageField  
upload_to  
null  
blank  
  
settings  
MEDIA_URL = '/media/'  
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')  
STATICFILES_DIRS =os.path.join(BASE_DIR, 'static')  
  
outer urls.py  
from django.conf import settings  
from django.conf.urls.static import static  
urlpatterns + static(settings.MEDIA_URL, document_root=settings.media_root)  
  
template  
<img src="{{  xx.header_image.url }}"/>  
```  
  
-----  
  
wsgi - common interface between web server(nginx/apache etc) and python app  
gunicorn is web server  
  
http req ->nginx->wsgi->gunicorn->django  
  