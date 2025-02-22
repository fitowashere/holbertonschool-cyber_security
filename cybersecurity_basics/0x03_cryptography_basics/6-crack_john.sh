#!/bin/bash
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" && john --show --format=raw-sha256 "$1" 2>/dev/null | grep ":" | cut -d ":" -f 2 > 6-password.txt
