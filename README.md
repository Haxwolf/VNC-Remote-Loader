# VNC-Remote-Loader
A Really Simple Mass Loader written in Python that Automatically connects to a vnc server and executes a download and execute or any oneliners on powershell.
# How Does it Work?
The Script is Really simple, it uses a txt file named `servers.txt` to get the ip,port and passwords of the vncs on which you need to drop your payload on.
# servers.txt format
The format for for the txt file is `IP:PORT-PASSWORD` for example `127.0.0.1:5900-1234`.
# Installation Guide
Just type `pip install -r requirements.txt` or start `install.bat`
