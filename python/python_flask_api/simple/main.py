# pip uninstall jwt
# pip uninstall pyjwt
# pip install pyjwt==1.7.0

import datetime
import jwt
import uuid

from functools import wraps

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = "thisissecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D:\\MY REPO\\flask_demo\\todo.db"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = User.query.filter_by(public_id=data["public_id"]).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(current_user, *args, *kwargs)
    return decorated


@app.route("/user", methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})
    return jsonify(
        {
            "users":
                [
                    {
                        "public_id": user.public_id,
                        "name": user.name,
                        "password": user.password,
                        "admin": user.admin
                    }
                    for user in User.query.all()
                ]
        }
    )


@app.route("/user/<public_id>", methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})
    return jsonify(
        {
            "user":
                {
                    "public_id": user.public_id,
                    "name": user.name,
                    "password": user.password,
                    "admin": user.admin
                }
        }
    )


@app.route("/user", methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")
    new_user = User(public_id=str(uuid.uuid4()), name=data["name"], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "New user created!"})


@app.route("/user/<public_id>", methods=['PUT'])
@token_required
def promote_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})
    user.admin = True
    db.session.commit()
    return jsonify({"message": "User has been promoted!"})


@app.route("/user/<public_id>", methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    if not current_user.admin:
        return jsonify({"message": "Cannot perform that function!"})
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        return jsonify({"message": "No user found!"})
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User has been deleted!"})


@app.route('/login', methods=["GET"])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify", 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response("Could not verify", 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({"public_id": user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({"token": token.decode('UTF-8')})
    return make_response("Could not verify", 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})


if __name__ == "__main__":
    app.run(debug=True)

# console
# from flask_demo.main import db
# db.create_all()
# close

# terminal
# PYTHON db_operations_pandas_sqlalchemy.py

# terminal
# PYTHON test_pytest.py

# deploy
"""
apt-get update
apt install apache2
apache2 -version
ufw app list
ufw allow 'Apache'
systemctl status apache2
apt-get install libapache-mod-wsgi PYTHON-dev
cd /var/www
mkdir webApp
cd webApp
apt-get install PYTHON-pip
pip install flask
pip install flask_sqlalchemy
sudo vi /etc/apache2/sites-available/webApp.conf

<VirtualHost *:80>
		ServerName ip
		ServerAdmin email@mywebsite.com
		WSGIScriptAlias / /var/www/webApp/webapp.wsgi
		<Directory /var/www/webApp/webApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/webApp/webApp/static
		<Directory /var/www/webApp/webApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

sudo a2ensite webApp

systemctl reload apache2

sudo vi webapp.wsgi

#!/usr/bin/PYTHON
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/webApp/")
from webApp import app as application
application.secret_key = 'Add your secret key'

cd ..

sudo service apache2 restart
"""
