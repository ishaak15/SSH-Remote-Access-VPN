# SSH-Remote-Access-VPN
A Remote access virtual private network using SSH. Having 3 main components, Remote LAN, Network Access Server and Client. The concept used was remote Port forwarding using SSH. Currently the application supports only a CLI interface, as the GUI config is still in work. 

<img src="Overlay.png" width="600" height="250"/>

Vagrant Containers were used to Set up the Remote LAN.

An AWS EC2 instance was used to setup the Network access server to listen to incoming connections. (Now been brought offline)

Client application to connect to the NAS and thereby the Remote LAN.
Install all the requirements in **Python3** using the following command:

    pip3 install -r requirements.txt

**Steps of Setup of the Entire VPN:**

Setup a LAN Network

    Prepare a Vagrant config file.
    Create a vagrant environment using the **vagrant init** command and edit the Vagrantfile to look similar to Vagrantfile_LDAPServer.
    The latest OS version will be downloaded from the Vagrant cloud.
    Vagrant box will be set up using the **vagrant up** command.

Set up Network Access Server<br>

    Set up an EC2 server
    Configure SSH Tunnel using the NAS_SSHDconf.txt file
    Setup Tunnel opening


Local Bridge Connection<br>

    Configure SSH on the Gateway ie the point of connection of the LAN with the NAS
    Setup SSH tunnel
    Allow NAS to receive connections


Authentication <br>

    Generate SSH Keys of the Gateway
    Copy SSH Key to a NAS
    Setup LDAP on the LAN Gateway


VPN Server Application<br>

    python3 ServerVPNTunnel.py 

VPN Client to connect to Network Access Server<br>

    python3 VPNClientapp.py

