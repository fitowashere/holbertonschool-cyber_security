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
        with open(maps_filename, 'r') as maps_file:
            for line in maps_file:
                if "[heap]" in line:
                    # Extract addresses from line that looks like:
                    # address_start-address_end permissions offset ...
                    addresses = line.split()[0]
                    start_address, end_address = addresses.split('-')
                    # Convert from hex string to int
                    return (int(start_address, 16), int(end_address, 16))
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

    # Get heap address range
    start_address, end_address = parse_maps_file(pid)
    print("[*] Heap found at: 0x{:x} - 0x{:x}".format(
        start_address, end_address))

    # Read memory from the heap
    heap_memory = read_memory(pid, start_address, end_address)

    # Search for the string in the heap
    search_bytes = search_string.encode('ASCII')
    replace_bytes = replace_string.encode('ASCII')

    # We want to directly use the replace bytes without modification
    # No padding with null bytes, no length check
    replace_bytes_padded = replace_bytes

    # Find all occurrences of the search string
    position = heap_memory.find(search_bytes)
    if position == -1:
        print("Error: String '{}' not found in heap".format(search_string))
        sys.exit(1)

    # Calculate the actual address in the process memory
    target_address = start_address + position
    print("[*] Found '{}' at 0x{:x}".format(
        search_string, target_address))

    # Write the replace string to the process memory
    if write_to_memory(pid, target_address, replace_bytes_padded):
        print("[*] Successfully replaced '{}' with '{}'".format(
            search_string, replace_string))


if __name__ == "__main__":
    main()
