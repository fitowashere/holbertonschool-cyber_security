#!/bin/bash

# Extract IP addresses from logs.txt, count occurrences, and find the most frequent one
grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
