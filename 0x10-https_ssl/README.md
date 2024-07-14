# HTTPS SSL Configuration Project

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png"/>
</p>


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
This project focuses on configuring HTTPS and SSL for a web server using HAproxy, enhancing the security and efficiency of web traffic.

## Technologies
- **HAproxy**: Version 1.5 or higher
- **Certbot**: For SSL certificate generation
- **Bash**: For scripting and automation


## Resource

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)
- [How to Secure HAProxy with Let's Encrypt on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-secure-haproxy-with-let-s-encrypt-on-ubuntu-14-04)
- [HAProxy SSL Termination](https://www.haproxy.com/blog/haproxy-ssl-termination/)


## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted on Ubuntu 16.04 LTS
- Files should end with a new line
- A `README.md` file is mandatory
- Bash scripts must be executable and pass Shellcheck (version 0.3.7) without errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line should be a comment explaining the script

## Directory Structure
```
0x10-https_ssl/
├── 0-world_wide_web
├── 1-haproxy_ssl_termination
└── 100-redirect_http_to_https
```

## Tasks

| Task Number | File Name                    | Description |
|-------------|------------------------------|-------------|
| 0           | 0-world_wide_web             | Configure domain zone for subdomains and create a Bash script to display information about subdomains. |
| 1           | 1-haproxy_ssl_termination    | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for subdomain www. |
| 2           | 100-redirect_http_to_https   | Configure HAproxy to automatically redirect HTTP traffic to HTTPS, enforcing encrypted traffic. |

## C Scripts
- No C scripts are required for this project.

## Author
:black_nib: **Ifeanyi I Ekezie** [iiekezie](https://github.com/iiekezie)
