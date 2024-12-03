#!/bin/bash
ps -U "$1" -o user,pid,%cpu,%mem,vsz,rss,tty,stat,start,time,command | grep -v " 0 *0 " | grep -v "VSZ"