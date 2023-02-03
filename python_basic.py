import os, sys

print("Current File Name:", os.path.realpath(__file__))
print("Current File Name:", os.path.abspath(__file__))
print("Current File Name:", sys.argv[0])
