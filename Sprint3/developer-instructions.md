# Developer Instructions of Augur

##[Augur on EC2](#augur-ec2)

*Note the first half these instructions are the ones that were provided for us at the start of the project with small details being changed. These include git cloning our group's repository and other useful things that we have learned throughout the semester 

branch | status
   --- | ---
master | [![Build Status](https://travis-ci.org/chaoss/augur.svg?branch=master)](https://travis-ci.org/chaoss/augur)
   dev | [![Build Status](https://travis-ci.org/chaoss/augur.svg?branch=dev)](https://travis-ci.org/chaoss/augur)

## About Augur

Augur is focused on prototyping open source software metrics. 

Functionally, Augur is a prototyped implementation of the Linux Foundation's [CHAOSS Project](http://chaoss.community) on [open source software metrics](https://github.com/chaoss/metrics). Technically, Augur is a [Flask web application](http://augurlabs.io), [Python library](http://augur.augurlabs.io/static/docs/) and [REST server](http://augur.augurlabs.io/static/api_docs/) that presents metrics on open source software development project health and sustainability. 


## Getting Started 
-------------------
### Vagrant
**The quickest way to get started working on Augur is by using [Vagrant](https://www.vagrantup.com/)** to spin up a virtual machine (VM) that comes with Augur already installed. We'll do all the work of setting up and installing dependencies, leaving you free to jump right into making something awesome. 

*Caveat: if you’re a super nerd who likes to have total control over your development environment, there’s a local installation link at the bottom of this page. For the rest of you, Vagrant is the way to go, especially if you've had trouble getting all the dependcies installed locally, are not comfortable installing them yourself, or are using an OS for which we don't currently support local installation. **We currently only support local installation for macOS and most flavors of Linux**.*

Windows installation instructions using Vagrant can be found [here](docs/python/source/windows-install.md).

Dependencies
------------

-   [Git
    client](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-   [Vagrant](https://www.vagrantup.com/)
-   [Virtualbox](https://www.virtualbox.org/)
-   [GitHub Access Token](https://github.com/settings/tokens) (no write
    access required)

1. Clone our Group's (16) repository and boot up the VM.

```bash
# on your local machine
git clone https://github.com/computationalmystic/augur-group16
cd augur
make vagrant
```

Note: you'll probably see a fair bit of errors during this provisioning process as Augur is getting installed. Don't worry about them, most of them are harmless. *Probably.*

2. Log in as `root` and navigate to `/vagrant/augur`. This folder is synced with your local clone of `augur`, meaning you'll be able to use your preferred local editor and just use the VM to run augur.  
```bash
# inside the vagrant VM
sudo su -
cd /vagrant/augur

# due to vagrant weirdness, we have to manually install the python packagew (this might take a while)
$AUGUR_PIP install --upgrade .
```

3. Augur.config.json 
   `augur.config.json` contains several elements that crucial for Augur. First, you need to add your GitHub API key under the `GitHub` section. Finally, you will need to provide log in credientals for the Facade and Ghtorrent databases.

4. Starting the backend and frontend servers
** There are 3 ways to start the servers. `make dev` will start the servers but they will stop will the terminal is closed or the user hits Command + C. `make dev-start`is similar to `make dev` however pressing Command + C will not stop the process. If you use `make dev-start`, you will need to use `make dev-stop` to kill the processes. You can also use `nohup make dev-start` to run launch the servers indefinitely to stop the servers use `make dev-stop`.

```bash
make dev
#Start                Stop
make dev-start       make dev-stop
nohup make dev-start make dev-stop
```

5. When you're done working in the VM, type `exit` twice: once to log out of `root`, and another to log out of the VM. Don't forget to shut down the VM with `vagrant halt`.

If you're interested in adding a new plugin, data source, or metric, check out the [backend development guide](http://augur.augurlabs.io/static/docs/dev-guide/3-backend.html). If new visualizations are more your speed, you'll want the [frontend development guide](http://augur.augurlabs.io/static/docs/dev-guide/4-frontend.html\).

### TL;DR

```bash
# on your local machine

# using your Git client: 
git clone https://github.com/chaoss/augur.git

# using Command Prompt
cd augur
vagrant up
vagrant ssh

# inside the vagrant VM
sudo su -
cd /vagrant/augur

# due to vagrant weirdness, we have to manually install the python packages
$AUGUR_PIP install --upgrade .

# add your GitHub personal access token to augur.config.json

# start the frontend and backend servers
make dev
# full steam ahead!
```

### Local Installation
To contribute to our code base routinely, we recommended that developers configure Augur on their local workstations. Start [here](http://augur.augurlabs.io/static/docs/dev-guide/1-overview.html) to get a primer on the project, or jump straight into our [local installation instructions](http://augur.augurlabs.io/static/docs/dev-guide/2-install.html) for developers.

## Guidelines
To contribute to Augur, please check out our [development guide](http://augur.augurlabs.io/static/docs/dev-guide/1-overview.html) and [notes on making contributions](CONTRIBUTING.md). Also, please note our [code of conduct](CODE_OF_CONDUCT.md). We want Augur to be a welcoming development community that is open to everyone. 

## Roadmap
Our technical, outreach, and academic goals [roadmap](https://github.com/chaoss/augur/wiki/Release-Schedule).

## License and Copyright
Copyright © 2018 University of Nebraska at Omaha, University of Missouri and CHAOSS Project at the Linux Foundation

Augur is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the file [LICENSE](LICENSE) for more details.

(This work has been funded through the Alfred P. Sloan Foundation)

## <a name="augur-ec2"></a>Using Augur on EC2

### EC2 Ports
Augur uses ports 3333 and 5000 so you're EC2 will need these inbound ports enabled. To do this, click on the security that your EC2 is using. Then click on the Inbound Tab. Next create a Custom TCP Rule for both ports 3333 and 5000 allowing IP's from anywhere.

### Next you will need to install a few packages on your EC2


```bash
# on your EC2
curl -sL https://rpm.nodesource.com/setup_10.x | sudo -E bash -
sudo yum install -y nodejs
curl https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh > Anaconda.sh
chmod +x Anaconda.sh
./Anaconda.sh -b
rm Anaconda.sh
```


