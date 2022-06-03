# info_inventree
Helpers to easyly run Inventree on Raspberry Pi OS Lite x64

## INSTALATION
~~~
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install \
    python3 python3-dev python3-pip python3-invoke python3-venv \
    git gcc g++ gettext gnupg \
    poppler-utils libpango-1.0-0 libpangoft2-1.0-0 \
    libjpeg-dev webp pango1.0-tools \
    python3-pip libpango-1.0-0 libpangoft2-1.0-0 -y 
sudo reboot
~~~
### Check if python and pango are already installed
~~~
python3 --version
pango-view --version
~~~
### Create required folders
~~~
mkdir log static data
~~~
### Get files and python packages
~~~
git clone https://github.com/inventree/inventree src
python3 -m venv env
source ./env/bin/activate
pip3 install weasyprint psycopg2 pgcli
weasyprint --info
pip install -U -r src/requirements.txt
deactivate 
~~~

### Install PostgreSQL
~~~
sudo apt-get install postgresql postgresql-contrib libpq-dev -y
sudo service postgresql start
sudo service postgresql enable
sudo -u postgres psql
~~~
When PostgreSQL cli runs:
~~~
create database inventree;
create user user with encrypted password 'password';
grant all privileges on database inventree to user;
exit
~~~

### Configure Inventree configuration
~~~
cp /home/inventree/src/InvenTree/config_template.yaml /home/inventree/src/InvenTree/config.yaml
nano /home/inventree/src/InvenTree/config.yaml
~~~
Modify PostgreeSQL configuration:
~~~
ENGINE: postgresql
NAME: inventree
USER: user
PASSWORD: password
HOST: 'localhost'
PORT: '5432'
~~~

### Execute first run
~~~
cd ~
source ./env/bin/activate
cd src
invoke update
~~~
Create admin user
~~~
invoke superuser
invoke server -a 192.168.XXX.XXX:8000
~~~


## RUN AS A SERVICE IN RPI ##
- Modify **inventree.service** IP Adress
- Copy **inventree.service** in **/lib/systemd/system** folder
- Copy **inventree_worker.service** in **/lib/systemd/system** folder
- Reload systemd:
~~~
sudo systemctl daemon-reload
~~~
- Start services:
~~~
sudo systemctl start inventree.service 
~~~
~~~
sudo systemctl start inventree_worker.service 
~~~
- If they works, enable the services on boot:
~~~
sudo systemctl enable inventree.service 
~~~
~~~
sudo systemctl enable inventree_worker.service 
~~~
