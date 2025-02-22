#!/bin/bash
find $1 -type f -perm /4000 -ls 2>/dev/null
