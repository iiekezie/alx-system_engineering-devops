# 0x17. Web Stack Debugging #3

## Project Overview

This project involves debugging a Wordpress site running on a LAMP stack (Linux, Apache, MySQL, PHP) using `strace` and automating the fix using Puppet. The goal is to identify and fix the 500 Internal Server Error and create a Puppet manifest to ensure the issue is resolved.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies](#technologies)
3. [Requirements](#requirements)
4. [Directory Structure](#directory-structure)
5. [Tasks](#tasks)
6. [C Scripts](#c-scripts)
7. [Author](#author)

## Technologies

- Ubuntu 14.04 LTS
- Apache/2.4.7 (Ubuntu)
- PHP 5.5.9-1ubuntu4.21
- Puppet v3.4
- Strace

## Requirements

### General

- All files are interpreted on Ubuntu 14.04 LTS.
- All files end with a new line.
- `README.md` file at the root of the project is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error.
- The first line of Puppet manifests must be a comment explaining the purpose of the manifest.
- Puppet manifests files must end with the `.pp` extension.
- Files will be checked with Puppet v3.4.

## Directory Structure

```bash
.
├── README.md
├── 0-strace_is_your_friend.pp
└── ...
```

## Tasks

| Task Number | File Name                    | Description                                                                 |
|-------------|------------------------------|-----------------------------------------------------------------------------|
| 0           | 0-strace_is_your_friend.pp   | Debugs the Wordpress LAMP stack using strace and automates the fix via Puppet |

### Task Breakdown

#### Task 0: Strace is your friend

- **File:** `0-strace_is_your_friend.pp`
- **Description:** Use `strace` to find the cause of a 500 Internal Server Error from Apache. Fix the issue and automate it using Puppet.

Example:

```bash
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
root@e514b399d69d:~# curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
```

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
