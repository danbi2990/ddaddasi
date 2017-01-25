import sys
import cx_Freeze
import os

# os.environ['TCL_LIBRARY'] = "C:\\Python35-32\\tcl\\tcl8.6"
# os.environ['TK_LIBRARY'] = "C:\\Python35-32\\tcl\\tk8.6"

os.environ['TCL_LIBRARY'] = "C:\\Tcl\\lib\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Tcl\\lib\\tk8.6"

build_exe_options = {"includes": ["tkinter"]}

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

cx_Freeze.setup(
    name = "ddaddasi",
    version = "1.0",
    description = "Get free from ddaddasi",
    # options = {"build_exe": {"packages":["tkinter"]}},
    executables = [cx_Freeze.Executable("ddaddasi.py", base=base)])


"""
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
And run it:

python setup.py bdist_msi
"""