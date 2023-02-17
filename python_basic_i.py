# Problem 46
import os, sys

print("Current File Name:", os.path.realpath(__file__))
print("Current File Name:", os.path.abspath(__file__))
print("Current File Name:", sys.argv[0])

# Problem 56
import fcntl, termios, struct

def terminal_size():
    th, tw, hp, wp = struct.unpack("HHHH", 
                                   fcntl.ioctl(0, termios.TIOCGWINSZ,
                                   struct.pack("HHHH", 0, 0, 0, 0)))
    return tw, th

print("Number of columns and rows:", terminal_size())

# Problem 76
import sys

print("This is the name/path of the script:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("Argument list:", str(sys.argv))

# Problem 107
import os.path, time

print("File:", __file__)
print("Access time:", time.ctime(os.path.getatime(__file__)))
print("Modified time:", time.ctime(os.path.getmtime(__file__)))
print("Change time:", time.ctime(os.path.getctime(__file__)))
print("Size:", os.path.getsize(__file__))

# Problem 108
# [1] `os.path` module & `os.getcwd()`
import os.path

print("Absolute file path:", os.path.abspath(__file__))

current_working_directory = os.getcwd()
print("Relative file path:", os.path.relpath("/home/yungshun/workspace/py/python-dsa", current_working_directory))

# [2] `os.path` module & `pathlib.Path.cwd()`
from pathlib import Path

print("Absolute file path:", os.path.abspath(__file__))

current_working_directory = Path.cwd()
print("Relative file path:", os.path.relpath("/home/yungshun/workspace/py/python-dsa", current_working_directory))
