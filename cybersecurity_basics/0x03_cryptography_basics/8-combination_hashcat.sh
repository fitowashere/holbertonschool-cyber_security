#!/bin/bash
while read -r a; do while read -r b; do echo "$a$b"; done < "$2"; done < "$1"
