#!/bin/bash

# First find attacker IP
attacker_ip=$(grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' logs.txt | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')

# Extract the most common User-Agent used by this IP
grep "$attacker_ip" logs.txt | grep -o "User-Agent:.*" | head -1 | sed 's/.*User-Agent: //' | sed 's/"$//'