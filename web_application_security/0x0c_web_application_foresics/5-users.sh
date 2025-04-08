#!/bin/bash
grep "new user" auth.log | grep -oE "name=[a-zA-Z0-9_-]+" | cut -d= -f2 | sort | tr '\n' ',' | sed 's/,$//'
