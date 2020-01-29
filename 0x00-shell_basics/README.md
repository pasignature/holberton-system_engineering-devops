#Shell Basics

Script to print current working directory

#! /bin/sh
echo "$(cd "$(dirname "$1")"; pwd)/$(basename "$1")"

Explanation:

    This script get relative path as argument "$1"
    Then we get dirname part of that path (you can pass either dir or file to this script): dirname "$1"
    Then we cd "$(dirname "$1") into this relative dir and get absolute path for it by running pwd shell command
    After that we append basename to absolute path: $(basename "$1")
    As final step we echo it
