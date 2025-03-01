#!/bin/bash
sestatus | grep -i "SELinux status:" | sed 's/SELinux status:\s*/SELinux status:                 /'
