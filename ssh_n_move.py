# python 2.7
#
# script in draft as a windows compatible one was required and pxssh doesn't exist for windows
# therefore script is function but not finished

import pxssh

try:
    s = pxssh.pxssh()
    s.login("host", "user", "password")
    s.sendline('mv /path1/* /path2')   # run a command
    s.prompt()             # match the prompt
    print s.before          # print everything before the prompt.
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
