# Project Overview
This project focuses on setting up a load balancer for redundancy and scalability using HAproxy and configuring web servers behind it.

## Technologies
- Ubuntu 16.04 LTS
- HAproxy
- Nginx
- Puppet

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All scripts must be executable
- Scripts must pass Shellcheck (version 0.3.7) without errors
- Scripts should start with `#!/usr/bin/env bash`
- README.md file at the root of the project folder

### Directory Structure

```
alx-system_engineering-devops/
├── 0-custom_http_response_header
├── 1-install_load_balancer
└── 2-puppet_custom_http_response_header.pp
```

## Tasks

| Task Number | File Name                                   | Description |
|-------------|---------------------------------------------|-------------|
| 0           | 0-custom_http_response_header                | Configure Nginx to add a custom header `X-Served-By` on web-01 and web-02 |
| 1           | 1-install_load_balancer                      | Install and configure HAproxy on lb-01 to load balance traffic between web-01 and web-02 |
| 2           | 2-puppet_custom_http_response_header.pp      | Use Puppet to automate adding the custom HTTP header `X-Served-By` on web-01 and web-02 |

## Author

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
