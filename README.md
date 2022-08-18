# simple-botnet  
## Table of content  
* [About the project](#about-the-project)  
* [Technologies](#technologies)  
* [Features](#features)  
* [Setup](#setup)  
## About the project  
>a simple botnet client and server .  
## Technologies  
* **python3**  
## Features  
* the server can handle ***multiple*** connection  
* the server can  ***run command*** on the bot and receive output

## Setup
Require at least 2 host on the same LAN.  
```shell  
#download the project why not on the server machine  
$git clone git@github
#share the botclient.py file to the bot host
#you can also git clone the repo for every host
#repeat this operattion for all host require ssh enabled
$scp botserver.py <boothost1>@<boothost1ip>:/home/boothost1/
#now first in the server machine run botserver.py
#here i'll user kali linux as server
(kali@kali)-[~]-$python3 botserver.py
#than I run the client in the bot hosts
#I use slepp the time to switch to one host to another 
#and press enter 
(ubuntu@ubuntu)-[~]-$python3 botserver.py
(fedora@fedora)-[~]-$python3 botserver.py
```
