## Basic Concepts  
  
#### What is an API?
An API is a program that takes in some data and gives back some other data, usually after processing it, so that our programs can use them.  
They are not meant for people to look at.  
eg: twitter, shopify, Imgur, OpenExchangeRates  
API works with resources eg: stores, items etc that can be created, retrieved, updated and deleted.
  
#### What is REST API?  
It is a type of web service that matches a specific structure.  
It is an interface between your program and other programs that call your api.  
  
#### What are endpoints?  
URLs are called endpoints in api.  
  
#### What is a request?  
It is what a browser does.  
Some computer on the internet is receiving it.  
That computer has something like a flask app in it, which receives the request, understands it and returns response.  
eg: home page, some other page, specific user's page etc  
  
#### What is HTTP?  
It is a protocol i.e. it is a way of creating interactions and allowing interactions between two internet connected elements like computers.  
  
#### What is a web server?  
It is a hardware like computer.  
It is a software for accepting incoming web requests.  
eg: google has many web servers  
  
#### How does a web interaction occur?   
When we access https://www.google.com/ from browser, we are sending something to one of the many google web servers and it responds.  
It is a Get HTTP 1.1 request on host www.google.com.  
--> GET is a verb that tells the server what is expected.  
--> / is path of what we want.  
--> HTTP 1.1 or 2 are protocols.  
Many responses are possible.  
--> Error is thrown if path is not found.  
--> Error is thrown if HTTP is not supported eg: by smtp or ftp server.    
--> Valid HTML code is returned.  
--> Text is returned.  
--> Nothing is returned.    
  
#### What are the different HTTP verbs? (from server's perspective)  
GET /item/1 - retrieve - default  
POST /item - receive data and use it - {"name": "chair", "price":"10"}  
PUT /item - make sure something is there - create/update - {"name": "chair", "price": "12"}  
DELETE /item/1 - remove something  
HEAD, OPTIONS etc  
  
#### What are REST principles?  
It uses same get put post delete principles.  
Its a way of thinking how a web server responds to requests.  
It doesnt respond with data but with resources.  
Each resource is able to interact with the pertinent request.  
eg: /item/chair is a resource on which we can use any verb like get resource, create resource, update resource, delete resource  
eg: GET /items is like ItemList resource  
REST is stateless i.e. one request does not depend on other.   
It does not know created items, it has to go back in db and check for get call.  
Web app should send user data everytime so that server knows that a user is logged in.  
  
#### What is javascript?  
It runs on browser like web app and calls api to get response.  
  
#### How to test API?  
Using postman.  
You can add environment variables like url at a place and use them everywhere else as {url}.  
  
#### What is a header?  
Header of our request is the first thing that gets analyzed by the server.  
eg: Content-Type application/json (server expects json in body) like {"name": "another store"}  
  
#### What is PIP?  
It accesses central library system of python and whichever module is enabled to work with central library management system in python.  
  
#### What is virtual environment?  
It is like installing python with no other libraries.  
  
#### How to install virtual environment?  
```pip install virtualenv```  
  
#### How to create virtual environment?  
```virtualenv venv --python=python3.5```  
  
#### How to activate virtual environment?  
```source venv/bin/activate``` (linux)  
```./venv/scripts/activate.bat``` (windows)  
  
#### How to deactivate virtual environment?  
```deactivate```  
  
#### What are the disadvantages of sqlite3?  
It does not enforce foreign key relationship.  
eg: We can create item without store with provided store id.  
  
#### What is SSH Key?  
It is a way of encrypting information.  
Whenever we generate ssh key, public key and private key are generated.  
Private key is used for encryption and public key for decryption.  
We share our public key with those services that we want to communicate with, so we dont have to put username pwd.  
  
#### How to generate SSH key?  
```ssh-keygen```  
```cat (public key with received path)``` eg: /Users/patankars/.ssh/id_rsa.pub  
  
#### What is git and github?  
Git helps move files between layers and allows us to commit and push.  
Github is just a server that hosts our git repos.  
  
#### What are git layers?  
Our files.  
Download and install git. (While installing check the checkbox for - associate .sh files to run with bash)  
Add files to staging (tell git to include these files in next commit).  
Commit files to local repo (snapshot).  
Push files to cloud (send them to git service like github).  
  
#### How to create github repo?  
Sign up to github.com.  
Create new repo with a name and description.  
Copy the repo's https url.  
  
#### How to push code to github?  
```mkdir code```  
```cd code```  
```git init```  
```git remote add origin (githubrepourl)```  
```touch app.py```  
```git add app.py```  
```(git rm --cached app.py)``` - to remove it from staging  
```git commit -m 'message'```  
```git push --set-upstream origin master``` - first time - next time just ```git push``` - provide username and password  
```(git status)```  
```(git pull)``` - to take changes done by others  
  
#### How to setup ssh communication with github?  
On git hub, go to your profile - edit - ssh keys - add new ssh key - give title - add ssh key.  
Next time you can say clone using ssh instead of https.  
```git remote remove origin```  
```git remote add origin (githubrepourl)```  
  
#### How to work with local git branch?  
```git branch (localbranch)```  
```git checkout (localbranch)```  
make changes  
```git add .```  
```git commit -m 'message'```  
```git push --set-upstream (localbranch)```  
test it  
```git checkout master```  
```git merge (localbranch)```  
```git push```  
```git branch -d (localbranch)```  
  
#### What is README.md markdown?   
(# title)  
(## subtitle)    
  
#### What is hosting?  
A server running our code and giving other people access to it via URL and IP.  
  
#### What is uWSGI?  
Way of serving flask app.  
uWSSGI will interact with our flask app and make it available to users.  
It helps multhithreading and restarting of failed threads.  
  
#### What is psycopg2?  
It is for sqlalchemy to communicate with postgres.  
  
#### what is nginx?  
It is reverse proxy.  
It is a gateway between our app and external users.  
It will accept requests and see what to do.  
Nginx communicates with uwsgi to enable multithreaded use of our app.  
It allows multiple flask apps to run on server and redirects to diff apps based on parameters.  
It is very fast.  
  
#### what is SSL?  
SSL sits on top of HTTP and secures all communications between client and server.  
Secure socket layer.  
If someone intercepts our traffic, they wont understand it.  
In HTTPS, S stands for SSL.  
  
#### what is IPv6?
Because IPv4 numbers are getting used up, we are slowly migrating to IPv6.  
  
#### What is DNS?  
DNS allows browser to enter string on address bar and that goes to an IP.  
Whenever a domain name is entered, it is first checked in the OS, if it exists in cache.  
Root DNS server hardcoded in internet provider's system.  
It will know .com server ip addresses.  
Then it goes to TLD(Top Level Domain) servers for example.com.  
Then it goes to the Authoritative server to get the actual IP.  
      
#### What is a port?  
It is area of computer where requests are received and responses are sent from.  
  
#### What is JSON?  
It is dictionary like string and is used to send data from one app to other.  
It uses double quotes.    

#### What are some common HTTP response codes?
404 - Not Found - When resource that we are trying to retrieve does not exist
401 - unauthorized - When token is not provided for a request
500 - Internal Server Error - When something unknown is wrong from server side
      
#### When to use class methods?  
When the method logic is not referring to any object i.e. self but referring to the entire class i.e. cls may be to return new objects.  
  
## Basic Flask Concepts    
  
#### What is Flask?  
It is a python library for creating web services.  
   
#### What is Flask-RESTful?  
It is an extension to flask.  
It's helpful for making restful apis  
  
#### What is Flask-JWT? How to use it?  
JSON Web Token  
For obfuscation of data so that no one understands our encoded message without decrypt key.  
User will send username and pwd.  
We will send user the JWT.  
Then the user can send its JWT along with any request.  
It shows us that they are authenticated.  
    
#### What is Flask-JWT-extended?  
It is used for token refresh.  
    
#### What is Flask-SQLAlchemy?  
Flask-SQLAlchemy is same but is made for easy use with flask.  
SQLAlchemy is ORM i.e. object relationship manager.  
  
#### How to install flask and other related libraries?  
```python -m pip install (library name)```   
Flask installs more libraries internally click, itsdangerous, Werkzeug, Jinja2 and MarkupSafe.  
  
#### What are Models and Resources in Flask App?  
Model is internal representation of an entity.  
Resource is external.  
    
## How to deploy flask App on linux server?  
  
#### login as root and install postgres  
--> ```ssh root@ip``` - enter username, password, say trusted Yes  
--> ```apt-get update``` (find if updates are there for existing packages)  
--> ```apt-get install postgresql postgresql-contrib``` - press Y (postgres user i.e. db owner is created, also a db with same name is created)  
  
#### create your own user on linux server  
--> ```adduser smita``` (creates group smita also) - enter password, name, details and press Y    
  
#### give all permissions to your own user  
--> ```visudo``` (edit sudoers file)  
--> ```smita ALL=(ALL:ALL) ALL``` - ctrl+o - ctrl+x  
  
#### give your own user the permission to ssh and remove root user's permission to ssh  
--> ```vi /etc/ssh/sshd_config``` - ```PermitRootLogin no``` - (at the end) ```AllowUsers smita```  
--> ```service sshd reload```  
  
#### login to linux server with your own user, switch to postgres db user and create your own db user  
```ssh smita@ip```  
```sudo su``` - enter password  
```sudo -i -u postgres```  
```createuser smita -P``` - enter password  
```createdb smita``` - exit - exit  
  
#### make db connection more secure so that sqlalchemy doesn't throw any security issues  
```sudo vi /etc/postgresql/9.5/main/pga_hba.conf```  (security conf)  
```local all all md5```  
  
#### install nginx  
```
sudo apt-get update  
sudo apt-get install nginx  
```
  
#### give nginx access through firewall, also allow ssh so that we don't get locked out  
```sudo ufw enable``` - press Y  
```sudo ufw allow 'Nginx HTTP'```  
```sudo ufw allow ssh```  
  
#### make nginx configurations  
```sudo vi /etc/nginx/sites-available/items-rest.conf```  
```
server{
    listen 80;  # default port when user access api is 80
    real_ip_header X-Forwarded-For;
    set_real_ip_from 127.0.0.1;
    server_name localhost;
    location {
        include uwsgi_params;
        uwsgi_pass unix:/var/wwww/html/items-rest/socket.sock;  # connection point between flask app and nginx
        uwsgi_modifier1 30;  # when to die if blocked}
    error_page 404 /404.html;
    location = /404.html{
        root /usr/share/nginx.html;}
    error_page 500 502 503 504 /50x.html;
    location = /50x.html{
        root /usr/share/nginx.html;}}
```
  
#### create soft link for nginx conf  
```sudo ln -s /etc/nginx/sites-available/items-rest.conf /etc/nginx/sites-enabled/```  
  
#### make our code(app) and log directory  
```sudo mkdir /var/www/html/items-rest```  
```sudo chown smita:smita /var/www/html/items-rest```  
```cd /var/www/html/items-rest```  
```git clone (our code) .```  
add ```secret_key``` to ```app.py```
```mkdir log```  
```sudo apt-get install python-pip python3-dev libpq-dev``` (for psycopg2)  
  
#### make and activate venv  
```pip install virtualenv```  
```virtualenv venv --python=python3.5``` (ubuntu comes with python3.5)  
```source venv/bin/activate```  
  
#### install required packages by our code  
```pip install -r requirements.txt```  
  
#### create a service  
```sudo vi /etc/systemd/system/uwsgi_items_rest.service```  
```
[Unit]
Description=uWSGI items rest
[Service]
Environment=DATABASE_URL=postgres://smita:1234@localhost:5432/smita
ExecStart=/var/www/html/items-rest/venv/bin/uwsgi --master --emperor /var/www/html/items-rest/venv/bin/uwsgi.ini  --die-on-term --uid smita  --gid smita --logto var/www/html/items-rest/log/emperor.log
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all
[Install]
WantedBy=multi-user.target
```
  
#### remove default nginx conf  
```
sudo rm /etc/nginx/sites-enabled/default  
sudo systemctl reload nginx  
sudo systemctl restart nginx  
```
  
#### start the service  
```sudo systemctl start uwsgi_items_rest```  
  
#### read logs  
```cat log/uwsgi.log```  
  
#### Register your domain name  
On www.namecheap.com, rest-api-course-trial.com. (Use whoisguard to prevent identoty being public.)  
  
#### Set DNS settings on CDN  
It will be secure and fast coz ppl accessing our site will actually be accessing the CDN.  
On cloudfare, signup and add website.  
  
#### change name server's on namecheap as per cloudfare  
  
#### Update cloudfare domain records    
A rest-api-course-trial.com 95.85.15.100 automatic ttl    
CNAME www.rest-api-course-trial.com rest-api-course-trial.com    
  
#### Generate ssl cert and key  
On cloudfare on chrome, generate ssl pem full strict cert and key  
  
#### Copy the ssl cert and key for our app  
```sudo mkdir /var/www/ssl```    
```sudo vi /var/www/ssl/rest-api-course-trial.com.pem``` - paste cert    
```sudo vi /var/www/ssl/rest-api-course-trial.com.key``` - paste key    
  
#### Configure the ssl cert and key for our app    
```sudo vi /etc/nginx/sites-enabled/items-rest.conf```    
```
listen 443 default_server;
server_name rest-api-course-trial.com;
ssl on;
ssl_certificate /var/www/ssl/rest-api-course-trial.com.pem;
ssl_certificate_key /var/www/ssl/rest-api-course-trial.com.key;
server{
    listen 80;
    server_name rest-api-course-trial.com;
    rewrite ~/(.*) https://rest-api-course-trial.com/$1 permanent;}
```
remove ```server_name localhost```    
  
#### Allow https on firewall  
```
sudo ufw allow https
sudo ufw reload
```
  
#### Restart nginx to reflect changes  
```
sudo systemctl reload nginx 
sudo systemctl restart nginx
```