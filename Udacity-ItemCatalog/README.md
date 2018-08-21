# Item Catalog Application - Udacity

### Full Stack Web Development ND


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* Python 2 (sudo apt-get install python)
* Vagrant (You can download from https://www.vagrantup.com/ according to your OS)
* VirtualBox (You can download from https://www.virtualbox.org/ according to your OS)
* apt-get -qqy update
* DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade
* apt-get -qqy install postgresql python-psycopg2
* apt-get -qqy install python-sqlalchemy
* apt-get -qqy install python-pip
* pip install --upgrade pip
* pip install werkzeug==0.8.3
* pip install flask==0.9
* pip install Flask-Login==0.1.3
* pip install oauth2client
* pip install requests
* pip install httplib2


### Running

1. Unzip the folder
2. cd to location where vagrant is present
3. vagrant up
4. vagrant ssh
5. cd /vagrant
6. python database_setup.py
7. python project.py

## Note
* You will need to generate client_secrets.json for your google account from the link https://console.developers.google.com/apis and replace the client ID generate in templates/login.html



