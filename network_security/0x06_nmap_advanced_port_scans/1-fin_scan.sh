#!/bin/bash
sudo nmap -sF -f -T2 -p80-85 "$1"
