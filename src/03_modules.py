"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
args = sys.argv
for arg in args:
    print(arg)

# Print out the OS platform you're using:
platform = sys.platform
print(platform)

# Print out the version of Python you're using:
py_version = 'Python ' + sys.version[:5]
print(py_version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
curr_pid = os.getpid()
print(curr_pid)

# Print the current working directory (cwd):
cwd = os.getcwd()
print(cwd)

# Print out your machine's login name
login_name = os.getlogin()
print(login_name)
