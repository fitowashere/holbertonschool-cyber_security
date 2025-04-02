#!/bin/bash

# First identify the attacker IP (IP with most requests)
attacker_ip=$(grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')

# Filter logs for the attacker IP and extract User-Agent
grep "$attacker_ip" logs.txt | grep -o "User-Agent: [^\"]*" | cut -d' ' -f2- | sort | uniq -c | sort -nr | head -n 1 | awk '{for(i=2;i<=NF;i++) printf "%s%s", $i, (i<NF ? " " : "\n")}'