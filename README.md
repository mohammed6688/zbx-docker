Docker Zabbix Userparams
------------------------
Simple scripts and userparameter conf to use with zabbix agent and a Docker server. 

Introduction
------------

Docker Userparams is a simple set of scripts that supports docker container discovery
and attr introspection.

With this solution, you can start to monitor your docker containers on your Servers.

Aditionally, you can monitor your docker cluster nodes and services.

Requirements
------------

For now, the Zabbix User should have access to the docker socket.

To use docker swarm mode monitoring the target where the userparameters are installed need to be a **manager** of the cluster.


Installation - Standard 
-----------------------

To install this solution you'll need to do the following steps:

1. Download the latest version of the binaries into the "/usr/local/share/zabbix/externalscripts" folder using the command (or similar):

```
wget https://github.com/gcavalcante8808/zbx-docker/releases/download/0.2a/zbx-docker.tar -O /usr/local/share/zabbix/externalscripts/zbx-docker.tar 
```

2. Descompact the file and make each file executable:

```
cd /usr/local/share/zabbix/externalscripts/
tar xf /usr/local/share/zabbix/externalscripts/zbx-docker.tar
```

3. Install the UserParameters available at the 'userparameters'.

4. Install the templates available at the 'templates' folder.

5. Link the Templates 'Docker Server' against every machine that you want to monitor the docker Containers;

6. Link the Template 'Docker Swarm Manager' against a MANAGER of your cluster;

After some minutes (10 by default) new hosts will be created at the Docker Containers Group when using the 'Docker Server' Template.

For the 'Docker Swarm Manager' template the Nodes and Services will be created at the groups 'Docker Cluster Nodes' and 'Docker Nodes Services'.


Other Notes
-----------

 * If you are using the Windows 2016 Server with docker support, you can still use this solution; however, you'll need to install python and 
docker-py package and use the scripts instead..

 * You can change the address that will be used to query about containers and discover trough zabbix interface adding a parameter on the discovery or a 3rd parameter in the info, but per default zabbix will not allow unsecure caracters (like @, / and other needed on the URL). In this case, you can create a bash script that wraps the py modules and that passes the --addr parameter with the correct URL of your  API Endpoint.
