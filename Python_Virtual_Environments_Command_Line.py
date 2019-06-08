# Python Virtual Environments
# venv — Creation of virtual environments.
# The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site
# directories.
# Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own
# independent set of installed Python packages in its site directories.
#

#
# Note:
# The pyvenv script has been deprecated as of Python 3.6 in favor of using python3 -m venv to help prevent any potential confusion as to which Python
# interpreter a virtual environment will be based on.
# 

#
# Creating virtual environments.
# Creation of virtual environments is done by executing the command venv;
# 

# python3 -m venv /path/to/new/virtual/environment

#
# The use of venv is now recommended for creating virtual environments.
#

# 
# On Windows, invoke the venv command as follows:
# 

# c:\>c:\Python35\python -m venv c:\path\to\myenv
 
#
# Alternatively, if you configured the PATH and PATHEXT variables for your Python installation:
# 

# c:\>python -m venv c:\path\to\myenv
