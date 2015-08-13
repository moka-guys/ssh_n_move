# python 2.7
#
# this is the windows version of ssh_n_move as pxssh does not exist for windows
#
# required modules: paramiko and pycrypto
#
# the later can apparently be a pain to install and so instead of installing
# python, have installed anaconda, then run:
# conda install paramiko
# conda install pycrytpo (although this should be installed automatically)
#
# todo: find a secure method for storing the password
# todo: log successful mv
# todo: (somewhat out of scope for this script) install syncback on secondary
# machine and set up to run as a backup

import paramiko

# ssh client
ssh = paramiko.SSHClient()
# auto accept host key without prompting and requiring response from a user
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# connect to server
ssh.connect('host', username='user', password='password')
# send move command
stdin, stdout, stderr = ssh.exec_command('mv /path1/* /path2')
# close connection
ssh.close()
