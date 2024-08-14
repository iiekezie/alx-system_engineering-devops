# 0x17. Web Stack Debugging #3

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
This project is part of the ALX SE program, focusing on debugging a web stack. You will be working on a WordPress website that runs on a LAMP stack. The goal is to identify and fix an issue that causes a 500 error and then automate the fix using Puppet.

## Technologies
- Ubuntu 14.04 LTS
- Apache/2.4.7 (Ubuntu)
- PHP/5.5.9
- Puppet v3.4
- Strace for debugging

## Requirements
### General
- All files must be interpreted on **Ubuntu 14.04 LTS**
- Files must end with a new line
- You must create a `README.md` file at the root of the project folder
- Puppet manifests must pass **puppet-lint version 2.1.1** without errors
- Puppet manifests must run without error and have a comment explaining their purpose at the top
- Puppet manifest filenames must end with the extension `.pp`

### Install puppet-lint
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

---

## Directory Structure
```plaintext
0x17-web_stack_debugging_3/
├── 0-strace_is_your_friend.pp
└── README.md
```

---

## Tasks

| Task # | File Name                    | Description                                                                 |
|--------|------------------------------|-----------------------------------------------------------------------------|
| 1      | `0-strace_is_your_friend.pp`  | Debug a 500 error caused by Apache using Strace and fix it using Puppet      |

---

## Prototype

### Task 1: Strace is your friend

- **Objective**: Use `strace` to debug why Apache is returning a 500 error, fix the issue, and automate the solution using Puppet.
- **Tools**: `strace`, `curl`, `puppet`.
- **Solution**: A Puppet script that fixes the error and ensures Apache serves the WordPress site properly.

Example Output:
```bash
root@server:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
...
root@server:~# puppet apply 0-strace_is_your_friend.pp
...
root@server:~# curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
...
root@server:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
```

---

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
