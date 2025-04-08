#!/bin/bash
# Look for various patterns that might indicate firewall rule additions
cat auth.log | grep -E '(firewall|iptables|ufw|DROP|ACCEPT|REJECT|filter|chain)' | grep -iE '(add|new|creat|insert|append)' | grep -v 'invalid\|failed\|failure\|error\|denied' | wc -l
