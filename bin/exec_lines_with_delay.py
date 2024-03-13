#!/usr/bin/env python3
# Try to make it executable without typing "python3 xxx.py ...", just "xxx.py ..."

#import subprocess
import time
import argparse
#import re
import os

def execute_commands_from_file(filename, delay):
    with open(filename, 'r') as file:
        for line in file:
            # Only works with os.system; as using subprocess.run messes up with the different arguments provided in my case
            os.system(line.strip())
            # Wait for the specified delay before executing the next command
            time.sleep(delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute commands from a file with a delay between each command.')
    parser.add_argument('filename', type=str, help='The file containing the commands to execute.')
    parser.add_argument('-d', '--delay', type=int, default=10, help='The delay in seconds between each command execution. Default is 10 seconds.')
    args = parser.parse_args()

    execute_commands_from_file(args.filename, args.delay)
