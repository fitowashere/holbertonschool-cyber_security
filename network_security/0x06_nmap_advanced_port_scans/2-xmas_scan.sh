#!/bin/bash
sudo nmap -sX -p440-450 --open --packet-trace --reason "$1"
