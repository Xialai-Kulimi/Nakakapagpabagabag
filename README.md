# Nakakapag README.md file

## Directory

* [Developer](https://github.com/Xialai-Kulimi/Nakakapagpabagabag#developer)
* [About](https://github.com/Xialai-Kulimi/Nakakapagpabagabag#about)
* [Protocol](https://github.com/Xialai-Kulimi/Nakakapagpabagabag#protocol)
* [Official Server Port List](https://github.com/Xialai-Kulimi/Nakakapagpabagabag#official-server-port-list)

## Developer

* Main: Kulimi  
email: xialai.kulimi@gmail.com  

## About

Hao, this project is called "Nakakapapabagabag" But some of them were mistyped as "Nakakabagpabagabag"But only "Nakakapagpabagabag" is right.To facilitate communication, it can be referred to as "Nakakapag" or "Nakaka".The above is just the name of the plan. The name of the software has not been finalized. Please use "Hact Wrevo" before completing it.On behalf of, the details of the entire project are as follows:"Create a game that is easy to share files, socialize, and have an open-world RPG element survival type."Currently, the programs are divided into two categories. "Server" and "Client" are placed in the "Server" and "Client" folders respectively.

## Protocol

As the client connects to the server. The client should provide his name, Safe code and time. I will show you how below.

    # While the client connects to the server, he should send a msg like below.
    username
    time
    sha256(username + password + time) # Safe Code

If the client wants to send a msg to the server, he should obey the format below.

    username
    gist
    msg
    time
    sha256(username + gist + msg + password + time) # Safe code
    
If the server wants to send a masg to the client. He should follow the format below.

    
    gist
    msg
    time
    sha256(gist + msg + password + time)
    


## Official Server Port List

update server : 60002  
vers check : server 60001  
login server : 60003  
main chat server:  60010 ~ 60110, 60210 ~ 60310  
main chat distribution server : 60005  

## Interface

Should powered by Tkinter. All of the animation can be show on with Tkinter.
