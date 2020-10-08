# 0x1A. Application server

Foundations - System engineering & DevOps ― Web stack

For this project, students are expected to look at these concepts:

    Web Server
    Server
    Web stack debugging
	
	![alt server](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201008%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201008T222907Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=84f5b1bb8a37793cf9de2fbc97393a96a2a9eab625d971107a70722863702820)

Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.
Resources

Read or watch:

    Application server vs web server
    How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
    Running Gunicorn
    Be careful with the way Flask manages slash in route - strict_slashes
    Upstart documentation

Requirements
General

    A README.md file, at the root of the folder of the project, is mandatory
    Everything Python-related must be done using python3
    All config files must have comments

Bash Scripts

    All your files will be interpreted on Ubuntu 16.04 LTS
    All your files should end with a new line
    All your Bash script files must be executable
    Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing


---
### Authors
Andrew Godwin

