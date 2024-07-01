# ALX System Engineering DevOps - SSH Project

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
In this project, we will learn how to use SSH to connect to remote servers using RSA keys, create SSH key pairs, configure SSH client files, and use Puppet to automate SSH client configurations.

## Technologies
- Ubuntu 20.04 LTS
- SSH
- Bash Scripts
- Puppet

## Requirements
### General
- Allowed editors: vi, vim, emacs
- Files will be interpreted on Ubuntu 20.04 LTS
- Files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line should be a comment explaining what the script does

## Directory Structure
```
alx-system_engineering-devops
└── 0x0B-ssh
    ├── 0-use_a_private_key
    ├── 1-create_ssh_key_pair
    ├── 2-ssh_config
    ├── 3-let_me_in
    └── 100-puppet_ssh_config.pp
```

## Tasks

| Task Number | File Name               | Description                                                                                      |
|-------------|-------------------------|--------------------------------------------------------------------------------------------------|
| 0           | 0-use_a_private_key     | Bash script to connect to a server using a private key                                           |
| 1           | 1-create_ssh_key_pair   | Bash script to create an RSA key pair                                                            |
| 2           | 2-ssh_config            | SSH client configuration file                                                                    |
| 3           | 3-let_me_in             | Add a public key to the server for SSH access                                                    |
| 4           | 100-puppet_ssh_config.pp| Puppet script to configure SSH client to use a private key and refuse password authentication     |

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>

---

Background Context
Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.

---

Resources
Read or watch:
- What is a (physical) server - text
- What is a (physical) server - video
- SSH essentials
- SSH Config File
- Public Key Authentication for SSH
- How Secure Shell Works
- SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

For reference:
- Understanding the SSH Encryption and Connection Process
- Secure Shell Wiki
- IETF RFC 4251 (Description of the SSH Protocol)
- Internet Engineering Task Force
- Request for Comments

man or help:
- ssh
- ssh-keygen
- env

---

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

### Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

---

### Your servers
| Name           | Username | IP              | State    |
|----------------|----------|-----------------|----------|
| 520587-web-01  | ubuntu   | 34.239.207.230  | running  |

---

### Tasks

#### 0. Use a private key
Write a Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:
- Only use ssh single-character flags
- You cannot use `-l`
- You do not need to handle the case of a private key protected by a passphrase

Example:
```sh
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
```

Repo:
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `0-use_a_private_key`

#### 1. Create an SSH key pair
Write a Bash script that creates an RSA key pair.

Requirements:
- Name of the created private key must be `school`
- Number of bits in the created key to be created `4096`
- The created key must be protected by the passphrase `betty`

Example:
```sh
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$
```

Repo:
- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0B-ssh`
- File: `1-create_ssh_key_pair`

#### 2. Client configuration file
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:
- Your SSH client configuration must be configured to use the private key `~/.ssh/school`
- Your SSH client configuration must be configured to refuse to authenticate using a password

Example:
```sh
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to 98.98.98.98 port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/school type -1
debug1: identity file /home/sylvain/.ssh/school-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_8.1
debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server->client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client->server aes128-ctr hmac-sha1-etm@openssh.com none