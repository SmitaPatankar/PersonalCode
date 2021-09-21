$ pip3 show Sphinx
---
Name: Sphinx
Version: 1.2.2
Location: /usr/local/lib/python3.4/site-packages
Requires: docutils, Jinja2, Pygments

$ pip3 show flask
---
Name: Flask
Version: 0.10.1
Location: /usr/local/lib/python3.4/site-packages
Requires: Werkzeug, Jinja2, itsdangerous

pyvenv
python -m venv
virtualenv

which python3
python3 --version

python3 -c 'import pytz'

$ pyvenv /tmp/myproject
$ cd /tmp/myproject
$ ls
bin     include     lib     pyvenv.cfg

$ source bin/activate
(myproject)$

(myproject)$ which python3
/tmp/myproject/bin/python3
(myproject)$ ls -l /tmp/myproject/bin/python3
... -> /tmp/myproject/bin/python3.4
(myproject)$ ls -l /tmp/myproject/bin/python3.4
... -> /usr/local/bin/python3.4

venv has pip and setuptools only

(myproject)$ python3 -c 'import pytz'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named 'pytz'

(myproject)$ pip3 install pytz

(myproject)$ python3 -c 'import pytz'
(myproject)$

(myproject)$ deactivate
$ which python3
/usr/local/bin/python3

(myproject)$ pip3 freeze > requirements.txt
(myproject)$ cat requirements.txt
numpy==1.8.2
pytz==2014.4
requests==2.3.0


$ pyvenv /tmp/otherproject
$ cd /tmp/otherproject
$ source bin/activate
(otherproject)$

(otherproject)$ pip3 list
pip (1.5.6)
setuptools (2.1)

(otherproject)$ pip3 install -r /tmp/myproject/requirements.txt

(otherproject)$ pip list
numpy (1.8.2)
pip (1.5.6)
pytz (2014.4)
requests (2.3.0)
setuptools (2.1)