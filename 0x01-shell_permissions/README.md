# Shell Permissions

0-iam_betty
A script that changes your user ID to betty.

1-who_am_i
A script that prints the effective userid of the current user i.e. Who you are logged in as.

2-groups
A script that prints all the groups the current user is part of.

3-new_owner
A script that changes the owner of the file hello to the user betty.

4-empty
A script that creates an empty file called hello.

5-execute
Ascript that adds execute permission to the owner of the file hello.

6-multiple_permissions
A script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

7-everybody
script that adds execution permission to the owner, the group owner and the other users, to the file hello.

8-James_Bond
A script that sets the permission to the file hello as follows:

    Owner: no permission at all
    Group: no permission at all
    Other users: all the permissions


9-John_Doe
A script that sets the mode of the file hello to this:
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

10-mirror_permissions
A script that sets the mode of the file hello the same as olleh’s mode.

11-directories_permissions
A script to add execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

12-directory_permissions
Script that creates a directory called dir_holberton with permissions 751 in the working directory.

13-change_group
A script that changes the group owner to holberton for the file hello.

14-change_owner_and_group
A script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

15-symbolic_link_permissions
A script that changes the owner and the group owner of the file _hello to betty and holberton respectively.

16-if_only
A script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
