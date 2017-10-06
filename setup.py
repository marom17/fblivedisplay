
from distutils.core import setup
import py2exe

setup(name="FB Live Display",
      version ="0.6.0",
      description="Display information about studio status and music",
      data_files=[".\\livedisplay.conf",".\\newSong.xml"],
      windows=[{
          "script": 'startLiveDisplay.py',
          "dest_base": 'LiveDisplay',
          "copyright": "(c) 2017 Romain Maillard"
          }])
#setup(windows=['startLiveDisplay.py'])
'''
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
includefiles = ['newSong.xml','livedisplay.conf']

setup(  name = "FB Live Display",
        version = "0.6.0",
        description = "Display information about studio status and music",
        author = "Romain Maillard",
        options = {"build_exe": {'include_files':includefiles}},
        executables = [Executable("startLiveDisplay.py", base="Win32GUI",targetName="LiveDisplay.exe")])
'''