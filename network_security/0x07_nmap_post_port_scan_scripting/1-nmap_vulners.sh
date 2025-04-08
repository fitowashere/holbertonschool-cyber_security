#!/bin/bash
nmap --script=vulners -sV -p 80,443 $1
