# Configuration management
Project done during **Full Stack Software Engineering studies** at **Holberton School**. It aims to learn about server configuration management using **Puppet**.

## Technologies
* Scripts written in Bash 4.3.11(1)
* Tested on Ubuntu 14.04 LTS
* Puppet 3.8

## Files

| Filename | Description |
| -------- | ----------- |
| `0-create_a_file.pp` | Create a file in `/tmp` |
| `1-install_a_package.pp` | Install `puppet-lint` |
| `2-execute_a_command.pp` | Create a manifest that kills a process named `killmenow` |


## Resources

Read or watch:

    Intro to Configuration Management
    Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
    Puppet’s Declarative Language: Modeling Instead of Scripting
    Puppet lint
    Puppet emacs mode

Requirements
General

    All your files will be interpreted on Ubuntu 14.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp

Note on Versioning

Your Ubuntu 14.04 VM should have Puppet 3.4 preinstalled.

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

The linked documentation is to Puppet 3.8 because the 3.4 documentation has been archived and is therefore more challenging to navigate. If you would like to upgrade anyway, click here (this will not affect how your code is checked). Puppet 5 Docs
Install puppet-lint

$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1

Andrew Godwin