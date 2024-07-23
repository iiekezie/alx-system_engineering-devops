# 0x12. Web Stack Debugging #2

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
This project involves debugging web stack issues. The main focus is to ensure that services are running with proper permissions and configurations, particularly focusing on Nginx.

## Technologies
- Bash scripting
- Docker
- Nginx
- Ubuntu 20.04 LTS

## Requirements

### General
- All files will be interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck without any error.
- Bash scripts must run without error.
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining what the script is doing.

## Directory Structure
```
0x12-web_stack_debugging_2/
├── 0-iamsomeoneelse
├── 1-run_nginx_as_nginx
└── 100-fix_in_7_lines_or_less
```

## Tasks

| Task Number | File Name                  | Description                                                                                             |
|-------------|----------------------------|---------------------------------------------------------------------------------------------------------|
| 0           | 0-iamsomeoneelse           | Write a Bash script that accepts one argument and runs the `whoami` command under the user passed as an argument. |
| 1           | 1-run_nginx_as_nginx       | Write a Bash script to ensure Nginx is running as the `nginx` user and listening on port 8080.          |
| 2           | 100-fix_in_7_lines_or_less | Write a concise Bash script (7 lines or less) to accomplish the task from task 1.                       |

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
