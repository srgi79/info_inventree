# info_inventree
Helpers to easyly start with Inventree (Docker) on Debian

## DOCKER INSTALATION
~~~
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
~~~

## DOCKER CONFIG
~~~
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
~~~

## PORTAINER INSTALATION
~~~
sudo apt install apt-transport-https ca-certificates curl software-properties-common gnupg2 -y
docker volume create portainer_data
docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
~~~

## INVENTREE INSTALATION
~~~
wget https://raw.githubusercontent.com/inventree/InvenTree/master/contrib/container/docker-compose.yml
wget https://raw.githubusercontent.com/inventree/InvenTree/master/contrib/container/.env
wget https://raw.githubusercontent.com/inventree/InvenTree/master/contrib/container/Caddyfile
~~~
### Edit .env file
~~~
nano .env
~~~
### Edit .env file. Un-comment admin account details and change INVENTREE_SITE_URL
~~~
INVENTREE_SITE_URL="http://10.0.0.150"
~~~
### Initialize server
~~~
docker compose run --rm inventree-server invoke update
~~~
### Start all containers
~~~
docker compose up -d
~~~
### EXTRA: Get demo data
~~~
docker compose down
docker compose run --rm inventree-server invoke setup-test -i
~~~
### EXTRA: Delete data
~~~
docker compose down
docker compose run --rm inventree-server invoke delete-data
~~~


- Test python scripts
