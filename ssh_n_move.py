# python 2.7
#
# script in draft as a windows compatible one was required and pxssh doesn't exist for windows
# therefore script is function but not finished

import pxssh
# import getpass
try:
    s = pxssh.pxssh()
    # hostname = raw_input('hostname: ')
    # username = raw_input('username: ')
    # password = getpass.getpass('password: ')
    # s.login (hostname, username, password)
    s.login("athena.kcl.ac.uk", "ryank", "password")
    s.sendline('mv /gpfs/home/ryank/NGS_runs/testdir* /gpfs/home/ryank/NGS_runs/testdir2')   # run a command
    s.prompt()             # match the prompt
    print s.before          # print everything before the prompt.
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
