# Linux Server Configuration

### Full Stack Web Development ND


## Get your server

Start a new Ubuntu Linux server instance on Amazon Lightsail. Follow [this](https://classroom.udacity.com/nanodegrees/nd004/parts/ab002e9a-b26c-43a4-8460-dc4c4b11c379/modules/357367901175462/lessons/3573679011239847/concepts/c4cbd3f2-9adb-45d4-8eaf-b5fc89cc606e) tutorial.


## Secure your server

1. sudo apt-get update
2. sudo apt-get upgrade
3. vi /etc/ssh/sshd_config - change port to 2200
4. sudo service ssh restart
5. sudo ufw status
6. sudo ufw default deny incoming
7. sudo ufw default allow outgoing
8. sudo ufw allow ssh to set the ufw firewall to allow SSH

9. Run sudo ufw allow 2200/tcp to allow all tcp connections for port 2200 so that SSH will work

10. Run sudo ufw allow www to set the ufw firewall to allow a basic HTTP server

11. Run sudo ufw allow 123/udp to set the ufw firewall to allow NTP

12. Run sudo ufw deny 22 to deny port 22 (deny this port since it is not being used for anything; it is the default port for SSH, but this virtual machine has now been configured so that SSH uses port 2200)


## SSH to instance from your system

1. Download private key Account page
2. sudo chown root:root LightsailDefaultPrivateKey-ap-southeast-1.pem
3. ssh -i LightsailDefaultPrivateKey-ap-southeast-1.pem -p 2200 ubuntu@52.77.222.212


## Give grader access

1. sudo adduser grader
2. Enter in a new UNIX password (twice) when prompted
3. Fill out information for the new grader user
4. sudo vim /etc/sudoers.d/grader
5. add the following line: grader ALL=(ALL) NOPASSWD:ALL


## Key for grader

1. Go to cmd of your local machine
2. ssh-keygen
3. Generating public/private rsa key pair.
Enter file in which to save the key (/home/nishtha/.ssh/id_rsa): /home/nishtha/.ssh/grader_key
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/nishtha/.ssh/grader_key.
Your public key has been saved in /home/nishtha/.ssh/grader_key.pub.
The key fingerprint is:
SHA256:nVxVJ8GGbuMSPqA752ABLmfoSwoSUuxJxz/j3vFU7gA nishtha@nishtha-Inspiron-5567
The key's randomart image is:
+---[RSA 2048]----+
|             o+oo|
| . .        ..o..|
|  + +      ...   |
| + = o  .o.o+    |
|o = + =.Eo++..   |
|.o + ..+ .+o.    |
|o o   +.. oo.    |
|oo . ooo.+ o     |
|. .   .+o . .    |
+----[SHA256]-----+
3. Go to cmd of virtual machine
4. cd /home/grader
5. sudo mkdir .ssh
6. touch .ssh/authorized_keys
7. copy contents from of grader_key.pub generated on your local machine to authorized_keys file
8. sudo service ssh restart
9. Go to your local machine
10. sudo ssh -i ~/.ssh/grader_key -p 2200 grader@52.77.222.212
 

## Configure timezone
1. sudo dpkg-reconfigure tzdata
2. Select None of Above
3. Select UTC


## Deploy project
1. sudo apt-get install apache2
2. sudo apt-get install libapache2-mod-wsgi python-dev
3. sudo a2enmod wsgi
4. Set up postgresql and create catalog
* sudo apt-get install postgresql
* sudo su - postgres
* Connect to psql (the terminal for interacting with PostgreSQL) by running psql
* Create the catalog user by running CREATE ROLE catalog WITH LOGIN;
* Next, give the catalog user the ability to create databases: ALTER ROLE catalog CREATEDB;
* Finally, give the catalog user a password by running \password catalog
* Exit psql by running \q
* Switch back to the ubuntu user by running exit
5. Create a Linux user called catalog and a new PostgreSQL database
* sudo adduser catalog
* sudo visudo
* add catalog ALL=(ALL:ALL) ALL
* createdb catalog
* Switch back to ubuntu
6. Install github
7. clone ItemCatalog project
8. Create new client_secrets.json accordingly and replace it
9. Virtual Environment
* sudo apt-get install python-pip
* sudo apt-get install python-virtualenv
* . venv/bin/activate
* pip install httplib2, requests, --upgrade oauth2client, sqlalchemy, flask, libpq-dev, psycopg2
* check by running the code
* deactivate
10. Virtual host
* create restaurant.conf in /etc/apache2/sites-available/
* sudo a2ensite restaurant.conf
* sudo service apache2 reload
11. wsgi file
* write restaurant.wsgi file in your project folder
* sudo service apache2 restart
12. Disable default apache site - a2dissite 000-default.conf
13. Change project owner to www-data
14. Run the project
* python database_setup.py
* python lotsofmenu.py
15. Open http://52.77.222.212.xip.io/ in your browser.


## Information for reviewer
* IP address: http://52.77.222.212
*  port: 2200
* URL to hosted web application: http://52.77.222.212.xip.io/
* SSH key location: http://52.77.222.212.xip.io/
* Credentials for ssh: grader, root123
