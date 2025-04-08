#!/bin/bash
# Count unique IP addresses that successfully gained access
grep "Accepted" auth.log | grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | sort -u | wc -l
