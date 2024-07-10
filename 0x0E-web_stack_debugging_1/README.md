# 0x0E. Web Stack Debugging #1

## Project Overview
The Webstack debugging series trains you in the art of debugging web stacks. This project focuses on debugging an Nginx installation within a Docker container to ensure it listens on port 80 and can serve a page.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Requirements](#requirements)
  - [General](#general)
- [Directory Structure](#directory-structure)
- [Tasks](#tasks)
- [Author](#author)


## Technologies
- Docker
- Ubuntu 20.04 LTS
- Bash

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does
- `wget` is not allowed

## Directory Structure
```
0x0E-web_stack_debugging_1/
├── README.md
├── 0-nginx_likes_port_80
└── 1-debugging_made_short
```

## Tasks

| Task Number | File Name              | Description                                                                                   |
|-------------|------------------------|-----------------------------------------------------------------------------------------------|
| 0           | 0-nginx_likes_port_80  | Debug the Nginx installation to ensure it is listening on port 80 and serving the default page |
| 1           | 1-debugging_made_short | Shorten the debugging script to 5 lines while ensuring Nginx listens on port 80                |

## Task Details

### Task 0: Nginx likes port 80
**File:** 0-nginx_likes_port_80

Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Install necessary tools, start and destroy as many containers as needed to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

### Task 1: Make it sweet and short
**File:** 1-debugging_made_short

Make your fix from task #0 short and sweet. Your Bash script must be 5 lines long or less, with a new line at the end of the file, respecting usual Bash script requirements. Avoid using `;`, `&&`, or `wget`, and do not reference your previous answer file.

## Author :black_nib:
* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
