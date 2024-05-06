# Project Overview

This project focuses on processes and signals in Linux, aiming to enhance understanding of concepts like PIDs, signals, process management, and shell scripting. It consists of several tasks that involve writing Bash scripts and a C program to perform various operations related to processes and signals.

## Technologies

- Bash
- C

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.7.0) without any error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does

### Task-specific Requirements

- Each task has its own requirements outlined in its description

## Directory Structure

```
0x05-processes_and_signals/
│
├── 0-what-is-my-pid
├── 1-list_your_processes
├── 2-show_your_bash_pid
├── 3-show_your_bash_pid_made_easy
├── 4-to_infinity_and_beyond
├── 5-dont_stop_me_now
├── 6-stop_me_if_you_can
├── 7-highlander
├── 8-beheaded_process
├── 100-process_and_pid_file
├── 101-manage_my_process
├── 102-zombie.c
│
└── README.md
```

## Tasks

| Task Number | File Name                      | Description                                 | Prototype                                 |
|-------------|--------------------------------|---------------------------------------------|-------------------------------------------|
| 0           | 0-what-is-my-pid               | Displays its own PID                        | `./0-what-is-my-pid`                      |
| 1           | 1-list_your_processes          | Displays a list of currently running processes | `./1-list_your_processes`               |
| 2           | 2-show_your_bash_pid          | Displays lines containing the word "bash"   | `./2-show_your_bash_pid`                  |
| 3           | 3-show_your_bash_pid_made_easy| Displays PID and process name of bash processes | `./3-show_your_bash_pid_made_easy`   |
| 4           | 4-to_infinity_and_beyond      | Displays "To infinity and beyond" indefinitely | `./4-to_infinity_and_beyond`             |
| 5           | 5-dont_stop_me_now            | Stops 4-to_infinity_and_beyond process      | `./5-dont_stop_me_now`                    |
| 6           | 6-stop_me_if_you_can          | Stops 4-to_infinity_and_beyond process without using kill or killall | `./6-stop_me_if_you_can`        |
| 7           | 7-highlander                  | Displays "To infinity and beyond" with signal handling | `./7-highlander`                      |
| 8           | 8-beheaded_process            | Kills the process 7-highlander              | `./8-beheaded_process`                   |
| 100           | 100-process_and_pid_file      | Displays messages and handles signals with PID file management | `sudo ./100-process_and_pid_file` |
| 101         | 101-manage_my_process         | Bash (init) script managing process        | `sudo ./101-manage_my_process [start/stop/restart]` |
| 102          | 102-zombie.c                  | C program creating zombie processes        | `gcc 102-zombie.c -o zombie`<br>`./zombie` |


## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
