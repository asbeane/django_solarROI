#!/usr/bin/env bash

# Update
sudo apt-get update
sudo apt-get -y update

# install Apache
sudo apt-get install -y apache2

# install python if not installed
sudo apt-get install -y python
sudo apt-get install python
sudo apt-get install -y python3
sudo apt-get install python3


# install pip specifically
sudo apt-get install python-pip
sudo apt-get install -y python-pip
sudo python /home/vagrant/project/get-pip.py

# install sql lite, just in case
sudo apt-get install sqlite
sudo apt-get install -y sqlite

# install pip and/or easy_install 
sudo apt-get install -y python setuptools
sudo apt-get install python setuptools

# install django...
sudo pip install Django
sudo -y pip install Django

# install django admin
sudo pip install djago-admin-tools

# start project
django-admin startproject solarROI

# syncdb
sudo python /home/vagrant/solarROI/manage.py syncdb
send "no"

# move synced files
cp /home/vagrant/project/solarROI/settings.py solarROI/solarROI/
cp /home/vagrant/project/solarROI/models.py solarROI/solarROI/
cp /home/vagrant/project/solarROI/forms.py solarROI/solarROI/
cp /home/vagrant/project/solarROI/urls.py solarROI/solarROI/
cp /home/vagrant/project/solarROI/views.py solarROI/solarROI/
cp -r /home/vagrant/project/solarROI/templates solarROI/solarROI/templates
cp -r /home/vagrant/project/solarROI/templates solarROI/templates

# run manage.py to make migrations
sudo python /home/vagrant/solarROI/manage.py makemigrations

# migrate
sudo python /home/vagrant/solarROI/manage.py migrate

# run manage.py to make migrations
sudo python /home/vagrant/solarROI/manage.py makemigrations

# sync db
sudo python /home/vagrant/solarROI/manage.py syncdb


# hopefully run server
sudo python /home/vagrant/solarROI/manage.py runserver 0.0.0.0:8000

# install emacs
sudo apt-get install -y emacs

if ! [ -L /var/www ]; then
  rm -rf /var/www
  ln -fs /vagrant /var/www
fi
