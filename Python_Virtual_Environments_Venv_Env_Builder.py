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
# The high-level virtual environment method makes use of a simple API which provides mechanisms for third-party virtual environment creators to customize
# environment creation according to their needs, the EnvBuilder class.
#
#
# class venv.EnvBuilder(system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=False, prompt=None):
#

#
# create(env_dir): 
# This method takes as required argument the path (absolute or relative to the current directory) of the target directory which is to contain the virtual
# environment.
# The create method will either create the environment in the specified directory, or raise an appropriate exception.
#

# 
# The create method of the EnvBuilder class illustrates the hooks available for subclass customization:
# 

def create(self, env_dir):
    """
    Create a virtualized Python environment in a directory.
    env_dir is the target directory to create an environment in.
    """

    env_dir = os.path.abspath(env_dir)
    context = self.ensure_directories(env_dir)

    self.create_configuration(context)

    self.setup_python(context)
    self.setup_scripts(context)

    self.post_setup(context)
