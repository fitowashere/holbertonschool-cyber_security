#!/bin/bash
echo "SELinux status:                 $(getenforce 2>/dev/null | tr '[:upper:]' '[:lower:]' || echo "disabled")"
