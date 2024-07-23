# 0x13. Firewall

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [General](#general)
- [Directory Structure](#directory-structure)
- [Tasks](#tasks)
- [C Scripts](#c-scripts)
- [Author](#author)

## Project Overview
This project focuses on configuring firewalls to manage and secure network traffic. The tasks include setting up rules to block or allow specific traffic and configuring port forwarding.

## Technologies
- Ubuntu 20.04 LTS
- UFW (Uncomplicated Firewall)
- SSH
- Nginx

## Requirements
### General
- Configure `ufw` to manage firewall rules.
- Ensure specific TCP ports are open while others are blocked.
- Implement port forwarding for specific use cases.

## Directory Structure
```
0x13-firewall/
├── 0-block_all_incoming_traffic_but
└── 100-port_forwarding
```

## Tasks
| Task Number | File Name                      | Description                                                                            |
|-------------|---------------------------------|----------------------------------------------------------------------------------------|
| 0           | 0-block_all_incoming_traffic_but| Configure UFW to block all incoming traffic except SSH (22), HTTPS (443), and HTTP (80)|
| 1           | 100-port_forwarding             | Configure UFW to forward traffic from port 8080/TCP to port 80/TCP                      |

## C Scripts
- Not applicable for this project.

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>

