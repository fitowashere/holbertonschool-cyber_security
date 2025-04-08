#!/bin/bash
grep -E "firewall|iptables|ufw|pf|netfilter|RULE" auth.log | grep -iE "add|append|new|create" | wc -l
