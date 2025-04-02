#!/bin/bash

# Extract IP addresses from logs.txt, find the most frequent one, and count its occurrences
attacker_ip=$(grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')
grep -o -E "$attacker_ip" logs.txt | wc -l
