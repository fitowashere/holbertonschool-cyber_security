#!/bin/bash
grep "sshd" auth.log | awk '{for (i=1; i<=NF; i++) count[$i]++} END {for (word in count) print count[word], word | "sort -nr"}'
