. Configuration Management

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [General](#general)
- [Directory Structure](#directory-structure)
- [Tasks](#tasks)
- [Author](#author)

## Project Overview

When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled, and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

1. When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
2. The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, PowerPoints, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1 hour, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously, writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

## Technologies

- Puppet
- Ubuntu 20.04 LTS

## Requirements

### General

- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`

### Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

To install Puppet:

```sh
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

To install `puppet-lint`:

```sh
$ gem install puppet-lint
```

## Directory Structure

```plaintext
0x0A-configuration_management/
├── 0-create_a_file.pp
├── 1-install_a_package.pp
└── 2-execute_a_command.pp
```

## Tasks

| Task Number | File Name              | Description                                      |
|-------------|-------------------------|--------------------------------------------------|
| 0           | 0-create_a_file.pp      | Create a file in /tmp with specified permissions |
| 1           | 1-install_a_package.pp  | Install Flask using pip3 with a specific version |
| 2           | 2-execute_a_command.pp  | Kill a process named killmenow using pkill       |

## Task Descriptions

### Task 0: Create a file

- **File:** `0-create_a_file.pp`
- **Description:** Using Puppet, create a file in `/tmp`.
  - File path is `/tmp/school`
  - File permission is `0744`
  - File owner is `www-data`
  - File group is `www-data`
  - File contains `I love Puppet`

### Task 1: Install a package

- **File:** `1-install_a_package.pp`
- **Description:** Using Puppet, install Flask from pip3.
  - Install Flask
  - Version must be `2.1.0`

### Task 2: Execute a command

- **File:** `2-execute_a_command.pp`
- **Description:** Using Puppet, create a manifest that kills a process named `killmenow`.
  - Must use the `exec` Puppet resource
  - Must use `pkill`

## Author :black_nib:

* **Ifeanyi I Ekezie** <[iiekezie](https://github.com/iiekezie)>
