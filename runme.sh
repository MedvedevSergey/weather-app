#!/usr/bin/env bash

BLUE='\033[1;34m'
NC='\033[0m'

sudo apt-get install python3-venv

activate () {
  echo -e ${BLUE}Activate virtual environment ${NC}
  . ~/venv_weather_app/bin/activate
}

/usr/bin/python3 -m venv ~/'venv_weather_app';
activate

echo -e ${BLUE}Upgrade pip${NC}
pip install --upgrade pip

echo -e ${BLUE}Install packeges from requirements.txt${NC}
pip install -r ~/weather_app/requirements.txt

echo -e ${BLUE}Migrate database${NC}
./manage.py migrate

echo -e ${BLUE}Collectstatic${NC}
cd ~/weather_app
./manage.py collectstatic --noinput

./manage.py runserver

