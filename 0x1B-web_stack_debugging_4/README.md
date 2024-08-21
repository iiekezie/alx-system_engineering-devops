# Web Stack Debugging #4

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
This project involves debugging and improving the performance of a web server setup using Nginx. The goal is to identify and resolve issues related to failed HTTP requests and optimize the server configuration for better performance. Additionally, system-level configurations are adjusted to handle specific use cases.

## Technologies
- Ubuntu 14.04 LTS
- Nginx
- ApacheBench
- Puppet

## Requirements

### General
- All files are interpreted on Ubuntu 14.04 LTS.
- Files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without errors.
- Puppet manifests must run without errors.
- The first line of Puppet manifests must be a comment explaining the purpose.
- Puppet manifest files must have the `.pp` extension.
- Files are checked with Puppet v3.4.

## Directory Structure
```plaintext
.
├── 0-the_sky_is_the_limit_not.pp
├── 1-user_limit.pp
└── README.md
```

## Tasks

| Task Number | File Name                   | Description                                                                                   |
|-------------|-----------------------------|-----------------------------------------------------------------------------------------------|
| 0           | `0-the_sky_is_the_limit_not.pp` | Debug the Nginx server to handle more HTTP requests successfully.                              |
| 1           | `1-user_limit.pp`           | Modify OS configuration to allow the `holberton` user to log in and open files without errors. |



## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
