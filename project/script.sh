#!/bin/bash

sudo apt-get update
sudo apt-get install -y default-jdk git

export DB_HOST="192.168.50.10"
export DB_PORT="3306"
export DB_NAME="petclinic"
export DB_USER="priima"
export DB_PASS="123"
export APP_USER="appuser"
export APP_DIR="/home/$APP_USER"
export PROJECT_DIR="/vagrant/petclinic"
