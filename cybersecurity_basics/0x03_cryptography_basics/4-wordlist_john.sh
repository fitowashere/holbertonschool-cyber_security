#!/bin/bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt "$1" && john --show --format=raw-md5 "$1" | grep ":" | cut -d ":" -f 2 > 4-password.txt
