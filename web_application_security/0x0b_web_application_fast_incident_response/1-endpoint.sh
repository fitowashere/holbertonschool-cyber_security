#!/bin/bash

# Extract URLs from the log file, count occurrences, and find the most frequently requested endpoint
grep -o 'GET \S*' logs.txt | cut -d ' ' -f 2 | cut -d '?' -f 1 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'\
