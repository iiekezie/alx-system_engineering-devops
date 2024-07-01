# Web Server Configuration Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
   - [General](#general)
4. [Directory Structure](#directory-structure)
5. [Tasks](#tasks)
6. [C Scripts](#c-scripts)
7. [Author](#author)

## Project Overview
In this project, you will configure a web server, automate tasks using Bash scripts, and manage DNS records. The goal is to set up a server that serves web pages, handles redirections, and displays custom error pages.

## Technologies
- Bash
- Nginx
- Puppet
- DNS

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- A README.md file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without errors
- First line of all Bash scripts should be `#!/usr/bin/env bash`
- Second line of all Bash scripts should be a comment explaining the script

## Directory Structure
```plaintext
0x0C-web_server/
├── 0-transfer_file
├── 1-install_nginx_web_server
├── 2-setup_a_domain_name
├── 3-redirection
├── 4-not_found_page_404
├── 7-puppet_install_nginx_web_server.pp
└── README.md
```

## Tasks
| Task Number | File Name                     | Description                                                                 |
|-------------|-------------------------------|-----------------------------------------------------------------------------|
| 0           | 0-transfer_file               | Script to transfer a file to the server using SCP                           |
| 1           | 1-install_nginx_web_server    | Script to install and configure Nginx web server                            |
| 2           | 2-setup_a_domain_name         | Setup a domain name and configure DNS records                               |
| 3           | 3-redirection                 | Configure Nginx to redirect to another page                                 |
| 4           | 4-not_found_page_404          | Configure a custom 404 error page                                           |
| 5           | 7-puppet_install_nginx_web_server.pp | Puppet manifest to install and configure Nginx server with redirection       |

## C Scripts
No C scripts are required for this project.

## Author

: black_nib: **Ifeanyi I Ekezie**  
GitHub: [iiekezie](https://github.com/iiekezie)

## Curriculum
SE Foundations  
Average: 109.06%  
0x0C. Web server  
DevOps  
SysAdmin  
Weight: 1  

Project timeline:  
- Start: Jul 1, 2024 6:00 AM
- End: Jul 3, 2024 6:00 AM

## Concept Overview
- **Child Process**: Understand the concept of parent and child processes in web servers.
- **Automating Tasks**: Use Bash scripts to automate the configuration of servers.
- **DNS and Web Servers**: Configure DNS records and understand the role of a web server.

## Learning Objectives
By the end of this project, you should be able to:
- Explain the main role of a web server.
- Describe the concept and use of child processes in web servers.
- List and explain the main HTTP requests.
- Understand DNS and its role in the internet.
- Configure and manage a web server using both Bash and Puppet.

## Resources
Read or watch:
- How the web works
- Nginx
- How to Configure Nginx
- Child process concept page
- Root and subdomain
- HTTP requests
- HTTP redirection
- Not found HTTP response code
- Logs files on Linux

For reference:
- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)