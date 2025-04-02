#!/bin/bash

# Get attacker IP (most frequent IP)
attacker_ip=$(grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')

# Get User-Agent for that IP
grep "$attacker_ip" logs.txt | grep -o "User-Agent:.*" | sort | uniq -c | sort -nr | head -n 1 | sed 's/.*User-Agent: //' | sed 's/".*//'