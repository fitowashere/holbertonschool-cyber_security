#!/usr/bin/python3
"""
Script to find and replace a string in the heap of a running process
Usage: read_write_heap.py pid search_string replace_string
"""

import sys
import os


def print_usage_and_exit():
    """Print usage information and exit with status code 1"""
    print("Usage: {} pid search_string replace_string".format(sys.argv[0]))
    sys.exit(1)


def parse_maps_file(pid):
    """
    Parse the /proc/{pid}/maps file to find the heap address range
    Returns tuple of (start_address, end_address) for the heap
    """
    try:
        maps_filename = "/proc/{}/maps".format(pid)
        print("[*] maps: {}".format(maps_filename))

        with open(maps_filename, 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Print detailed information about the heap
                    print("[*] Found [heap]:")

                    # Split the line into fields
                    fields = line.split()
                    addresses = fields[0]
                    permissions = fields[1]
                    offset = fields[2]
                    inode = fields[4]

                    print("\tpathname = [heap]")
                    print("\taddresses = {}".format(addresses))
                    print("\tpermissions = {}".format(permissions))
                    print("\toffset = {}".format(offset))
                    print("\tinode = {}".format(inode))

                    # Extract start and end addresses
                    start_address, end_address = addresses.split('-')
                    start_address = int(start_address, 16)
                    end_address = int(end_address, 16)

                    return (start_address, end_address)
    except IOError as e:
        print("Error: Can't open {} - {}".format(maps_filename, e))
        sys.exit(1)

    print("Error: No heap found in the maps file")
    sys.exit(1)


def read_memory(pid, start_address, end_address):
    """
    Read the memory of the process within the given address range
    Returns the memory content as bytes
    """
    try:
        mem_filename = "/proc/{}/mem".format(pid)
        print("[*] mem: {}".format(mem_filename))

        with open(mem_filename, 'rb+') as mem_file:
            # Seek to the start address of the heap
            mem_file.seek(start_address)
            # Read the entire heap
            return mem_file.read(end_address - start_address)
    except IOError as e:
        print("Error: Can't open or read {} - {}".format(mem_filename, e))
        sys.exit(1)


def write_to_memory(pid, address, data):
    """
    Write data to the specified address in the process memory
    """
    try:
        mem_filename = "/proc/{}/mem".format(pid)
        with open(mem_filename, 'rb+') as mem_file:
            mem_file.seek(address)
            mem_file.write(data)
            print("[*] Writing '{}' at {}".format(
                data.decode('ASCII'), hex(address)))
            return True
    except IOError as e:
        print("Error: Can't write to {} - {}".format(mem_filename, e))
        sys.exit(1)


def main():
    """Main function to find and replace a string in the heap"""
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print_usage_and_exit()

    # Parse arguments
    try:
        pid = int(sys.argv[1])
    except ValueError:
        print("Error: PID must be an integer")
        print_usage_and_exit()

    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    # Validate strings
    if len(search_string) < 1 or len(replace_string) < 1:
        print("Error: Strings cannot be empty")
        print_usage_and_exit()

    # Check if the replace string is longer than the search string
    if len(replace_string) > len(search_string):
        print("Error: Replace string cannot be longer than search string")
        sys.exit(1)

    # Get heap address range
    start_address, end_address = parse_maps_file(pid)
    print("[*] Addr start [{}] | end [{}]".format(
        hex(start_address), hex(end_address)))

    # Read memory from the heap
    heap_memory = read_memory(pid, start_address, end_address)

    # Search for the string in the heap
    search_bytes = search_string.encode('ASCII')
    replace_bytes = replace_string.encode('ASCII')

    # Pad the replace bytes to match the length of search bytes
    replace_bytes_padded = replace_bytes + b'\0' * (len(
        search_bytes) - len(replace_bytes))

    # Find all occurrences of the search string
    position = heap_memory.find(search_bytes)
    if position == -1:
        print("Error: String '{}' not found in heap".format(search_string))
        sys.exit(1)

    # Calculate the actual address in the process memory
    target_address = start_address + position
    print("[*] Found '{}' at {}".format(search_string, position))

    # Write the replace string to the process memory
    write_to_memory(pid, target_address, replace_bytes_padded)


if __name__ == "__main__":
    main()
