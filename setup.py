from distutils.core import setup
import py2exe

setup(data_files=[".\\livedisplay.conf"],windows=['startLiveDisplay.py'])
#setup(windows=['startLiveDisplay.py'])