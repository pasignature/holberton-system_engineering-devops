# SSH
Project done during **Full Stack Software Engineering studies** at **Holberton School**. It aims to learn about what is a SSH, how to create an SSH RSA key pair and how to connect to a remote host using SSH.

## Technologies
* Scripts written in Bash 4.3.11(1)
* Tested on Ubuntu 14.04 LTS
* Puppet 3.8

## Files

| Filename | Description |
| -------- | ----------- |
| `0-use_a_private_key` | Uses `ssh` to connect to a server using a private key previously generated |
| `1-create_ssh_key_pair` | Creates an RSA key pair |
| `2-ssh_config` | SSH client configuration using a private key and refusing to authenticate using a password |
| `4-puppet_ssh_config.pp` | Sets up the client SSH configuration file to connect to a server without typing a password |




For this project, students are expected to look at this concept:

    Server

## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 16.04 LTS environment. You do not need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do not attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.
Resources

Read or watch:

    What is a (physical) server - text
    What is a (physical) server - video
    SSH essentials
    SSH Config File
    Public Key Authentication for SSH
    How Secure Shell Works
    SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

For reference:

    Understanding the SSH Encryption and Connection Process
    Secure Shell Wiki
    IETF RFC 4251 (Description of the SSH Protocol)
    Internet Engineering Task Force
    Request for Comments

man or help:

    ssh
    ssh-keygen
    env

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash

Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 16.04 LTS
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    All your Bash script files must be executable
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing

Andrew Godwin