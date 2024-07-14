# Attack is the Best Defense

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
4. [General](#general)
5. [Directory Structure](#directory-structure)
6. [Tasks](#tasks)
7. [C Scripts](#c-scripts)
8. [Author](#author)

## Project Overview
Security is a vast topic, and network security is an important part of it. A lot of very sensitive information goes over networks that are used by many people, and some people might have bad intentions. This project focuses on sniffing unencrypted traffic and getting information out of it.

## Technologies
- Ubuntu
- tcpdump
- Wireshark
- Docker
- Hydra

## Requirements
- Ubuntu Vagrant machine or any other Linux machine
- tcpdump
- Wireshark
- Docker

## General
- The project consists of advanced tasks that deal with network security.
- The focus is on sniffing unencrypted traffic and performing a dictionary attack using Docker.

## Directory Structure
```
.
├── attack_is_the_best_defense
│   ├── 0-sniffing
│   ├── 1-dictionary_attack
│   └── README.md
```

## Tasks

| Task Number | File Name             | Description                                                                                  |
|-------------|-----------------------|----------------------------------------------------------------------------------------------|
| 0           | 0-sniffing            | Execute a script locally and use tcpdump to sniff the network to find a password.            |
| 1           | 1-dictionary_attack   | Use Hydra and a password dictionary to brute force an SSH account running in a Docker container.|

## Prototype
```sh
# Start tcpdump to capture network traffic
sudo tcpdump -i any -w capture.pcap

# Run the authentication script
./user_authenticating_into_server

# Stop tcpdump
# (Do this manually by pressing Ctrl+C)

# Open the capture file in Wireshark
wireshark capture.pcap

# Decode base64 encoded credentials
echo "base64string" | base64 --decode
```

### Concepts
For this project, we expect you to look at these concepts:
- Network basics
- Docker


### Resources
Read or watch:
- Network sniffing
- ARP spoofing
- Connect to SendGrid’s SMTP relay using telnet
- What is Docker and why is it popular?
- Dictionary attack

### man or help:
- tcpdump
- hydra
- telnet
- docker

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>

