#!/bin/bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/nul
sudo apt-get update -y

sudo apt-get install jenkins -y

sed -i 's|Environment="JAVA_OPTS=-Djava.awt.headless=true"|Environment="JAVA_OPTS=-Djava.awt.headless=true -Djava.net.preferIPv4Stack=true -Djava.net.preferIPv4Addresses=true"|' /lib/systemd/system/jenkins.service
sed -i 's|#Environment="JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64"|Environment="JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64"|' /lib/systemd/system/jenkins.service
      
sudo systemctl daemon-reload
sudo systemctl enable jenkins
sudo systemctl start jenkins

sudo cat /var/lib/jenkins/secrets/initialAdminPassword > /vagrant/pass.txt