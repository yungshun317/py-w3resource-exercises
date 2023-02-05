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
