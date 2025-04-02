#!/bin/bash

awk '{print $1}' logs.txt | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}' | xargs -I{} awk -v ip="{}" '$1 == ip {print $0}' logs.txt | awk -F'"' '{print $6}' | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2, $3}'