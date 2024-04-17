#!/usr/bin/env python3

import time
import argparse
import os
import shlex

def execute_commands_from_file(filename, delay):
    with open(filename, 'r') as file:
        for line in file:
            # Parse the command line
            args = shlex.split(line.strip())
            
            # Check if '-o' is in the command line arguments
            if '-o' in args:
                # Get the index of '-o' and use it to find the output file
                output_file = args[args.index('-o') + 1]
                
                # Check if the output file already exists
                if os.path.isfile(output_file):
                    print(f"Skipping file {output_file} which already exists.")
                    continue
            
            # Execute the command
            os.system(line.strip())
            
            # Wait for the specified delay before executing the next command
            print(f"Pause of {delay} seconds...")
            time.sleep(delay)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Execute commands from a file with a delay between each command.')
    parser.add_argument('filename', type=str, help='The file containing the commands to execute.')
    parser.add_argument('-d', '--delay', type=int, default=10, help='The delay in seconds between each command execution. Default is 10 seconds.')
    args = parser.parse_args()

    execute_commands_from_file(args.filename, args.delay)
