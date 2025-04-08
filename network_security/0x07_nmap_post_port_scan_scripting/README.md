# Nmap Post Port Scan Scripting

This repository contains a collection of bash scripts that leverage the Nmap Scripting Engine (NSE) for advanced network scanning and vulnerability detection.

## What is the Nmap Scripting Engine (NSE)?

The Nmap Scripting Engine (NSE) is an advanced feature of the open-source network scanning tool Nmap. It automates network scanning and exploitation tasks through scripting, saving time and enhancing capabilities.

## Scripts in this Repository

### 0-nmap_default.sh
Runs Nmap with default NSE scripts to gather basic information about a target host.
```bash
./0-nmap_default.sh <target_host>
```

### 1-nmap_vulners.sh
Scans ports 80 and 443 on a target host using the vulners script to identify vulnerabilities.
```bash
./1-nmap_vulners.sh <target_host>
```

### 2-vuln_scan.sh
Checks for the Apache Struts 2 vulnerability (CVE-2017-5638) and saves results to a file.
```bash
./2-vuln_scan.sh <target_host>
```

### 3-comprehensive_scan.sh
Performs a comprehensive security analysis using multiple NSE scripts sequentially.
```bash
./3-comprehensive_scan.sh <target_host>
```

### 4-vulnerability_scan.sh
Detects vulnerabilities across various services using wildcards for broader coverage.
```bash
./4-vulnerability_scan.sh <target_host>
```

### 5-service_enumeration.sh
Conducts comprehensive network reconnaissance with service version detection, OS detection, and more.
```bash
./5-service_enumeration.sh <target_host>
```

## Usage Notes

- All scripts require a target host as an argument
- Most scripts should be run with sudo privileges
- Results may vary depending on the network environment and target configuration
- Always ensure you have proper authorization before scanning any network or system

## Why NSE Scripts Matter

Using NSE scripts enhances network scanning by:
- Automating complex tasks
- Providing deeper insights into network services
- Identifying security vulnerabilities
- Enabling customized scanning workflows

By mastering NSE scripts, security professionals can dramatically improve their network assessment capabilities.
