#!/bin/bash
find / -type d -perm -o+w -print -exec chmod o-w {} \; 2>/dev/null
