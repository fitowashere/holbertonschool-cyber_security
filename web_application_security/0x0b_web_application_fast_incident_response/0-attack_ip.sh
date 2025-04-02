#!/bin/bash

# Check if the log file exists
if [ ! -f $1 ]
then
    echo "Error: Log file not found."
    exit 1
fi

# Extract IP addresses from the log file, count occurrences, and find the most frequent one
grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' $1 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
