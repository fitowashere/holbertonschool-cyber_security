#!/bin/bash

# Scan logs for service information and count occurrences
grep -o "pam_unix([^:]*" /var/log/auth.log | sort | uniq -c | sort -nr
