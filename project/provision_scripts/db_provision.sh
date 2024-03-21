#!/bin/bash

# Install MySQL and dependencies
sudo apt-get update
sudo apt-get install -y mysql-server

# Customize MySQL to accept connections only from Vagrant private network subnet
sudo sed -i "s/^bind-address/#bind-address/" /etc/mysql/mysql.conf.d/mysqld.cnf
sudo systemctl restart mysql

# Set up environment variables
export DB_USER="priima"
export DB_PASS="123"
export DB_NAME="petclinic"

# Create MySQL user and database
sudo mysql -u root -e "CREATE USER '$DB_USER'@'%' IDENTIFIED BY '$DB_PASS';"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'%';"
sudo mysql -u root -e "FLUSH PRIVILEGES;"
sudo mysql -u root -e "CREATE DATABASE $DB_NAME;"
