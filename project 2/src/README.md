# Step Project 2

## Task 1

Some changes were also made, namely:

- commented code lines were removed
- changed the port of the application itself from 80 to 3000
- set project for private (check use correctly GitHub cred)

[GitHub copied project](https://github.com/Oleksandr-Nikiha/forStep2)

## Task 2

[DockerHub profile](https://hub.docker.com/u/luckerdie)

## Task 3

Docker and Jenkins are installed in two separate scripts to reduce the size of the Vagrantfile and keep the code clean.

- [Install Docker](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/src/init_script/install_docker.sh)
- [Install Jenkins](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/src/init_script/install_jenkins.sh)
- [Vagrantfile](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/src/Vagrantfile)

## Task 4

1. Get your admin pass from pass.txt (Screen-1) - file and complete the initial installation
2. Installed plugins: GitHub, GitParameter, Docker Pipeline, Docker, Docker Commons `Jenkins Manage > Plugins > Available plugins`
3. Enable TCP port for inbound agents `Jenkins Manage > Security > Agents` select *random*
4. Create agent `Manage Jenkins > Nodes > New node` (Screen-2)
5. Open created agent and run command in *Worker server* (Screen-3) ```
 sudo su
 curl -sO http://[IP_JENKINS_SERVER]:8080/jnlpJars/agent.jar
 java -jar agent.jar -url http://[IP_JENKINS_SERVER]:8080/ -secret [SECRET_IN_OPEN_AGENT] -name "jenkins_worker" -workDir "\opt\build" ```

6. Set up credentials for DockerHub and GitHub `Manage Jenkins > Credentials > System > Global credentials (unrestricted) > Add Credentials`
    1. Use `Username and password` for DockerHub cred. (I created a token to avoid using my password)
    2. Use `Username and password` for GitHub cred. (I created a token to avoid using my cred)

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen1.png  "Screen1")

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen2.png  "Screen2")

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen3.png  "Screen3")

## Task 5

I created a pipeline using the following script.

[Jenkins pipeline groovy script](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/src/pipeline_script.groovy)

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen4_1.png  "Screen4_1")

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen4_2.png  "Screen4_2")

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen4_3.png  "Screen4_3")

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen4_4.png  "Screen4_4")

![alt](https://github.com/Oleksandr-Nikiha/Dan.IT/blob/main/STEP_PROJECT-2/screens/screen4_5.png  "Screen4_5")
