hoberton# Memory Heap Scanner and Replacer

A Python script that finds and replaces a string in the heap of a running process.

## Description

This script scans the heap memory of a running process to find a specific string and replaces it with another string. It's designed to work on Linux systems by utilizing the `/proc` filesystem.

Key features:
- Searches only in the heap segment of a process's memory
- Automatically handles string padding/truncation to maintain memory integrity
- Silent operation (only prints in case of errors)
- Support for empty replacement strings

## Requirements

- Python 3
- Linux operating system (relies on the `/proc` filesystem)
- Root privileges (to access process memory)

## Usage

```
sudo python3 read_write_heap.py pid search_string replace_string
```

### Arguments:

- `pid`: Process ID of the target process
- `search_string`: ASCII string to search for in the heap
- `replace_string`: ASCII string to replace it with

### Example:

```
sudo python3 read_write_heap.py 1234 "Holberton" "NewString"
```

## How It Works

1. The script parses the `/proc/<pid>/maps` file to find the heap memory region
2. It reads the entire heap memory using `/proc/<pid>/mem`
3. It searches for the target string in the heap memory
4. When found, it calculates the exact memory address and writes the replacement string

## Notes

- If the replacement string is shorter than the search string, it will be padded with null bytes
- If the replacement string is longer than the search string, it will be truncated
- The script requires root privileges to access another process's memory
- The search string cannot be empty, but the replacement string can be

## Error Handling

The script will exit with status code 1 and print an error message in the following cases:
- Incorrect number of arguments
- Invalid PID
- Empty search string
- Inability to open or read the memory maps
- Heap not found in memory maps
- Target string not found in the heap
- Inability to write to process memory