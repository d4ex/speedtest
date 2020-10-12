# Speedtest for raspberry pi

## Prerequisite
### Install docker
curl -sSL https://get.docker.com | sh

### Add permission to Pi User to run Docker Commands
sudo usermod -aG docker pi

### Install dependencies for docker-compose
* sudo apt-get install -y libffi-dev libssl-dev
* sudo apt-get install -y python3 python3-pip
* sudo apt-get remove python-configparser

### Install docker-compose
sudo pip3 -v install docker-compose

## Run speedtest
docker-compose -f docker-compose.yaml up -d
