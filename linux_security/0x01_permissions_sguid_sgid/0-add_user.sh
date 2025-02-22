#!/bin/bash
useradd -m -s /bin/sh $1
echo "$1:$2" | chpasswd
