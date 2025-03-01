# Linux Security: Protocols & Servers

This repository contains scripts for security assessment, hardening, and testing of various network protocols and services on Linux servers.

## Project Overview

The scripts in this repository help identify security vulnerabilities, implement hardening measures, and test security configurations for common Linux network services like SSH, SMTP, HTTP, and more.

## Scripts

### 0. Analyze iptables Rules
- **File**: `0-iptables.sh`
- **Description**: Displays all current `iptables` rules in a readable format with line numbers.
- **Usage**: `sudo ./0-iptables.sh`

### 1. Audit SSH Configuration
- **File**: `1-audit.sh`
- **Description**: Checks for and reports non-standard SSH configuration settings in `/etc/ssh/sshd_config`.
- **Usage**: `sudo ./1-audit.sh`

### 2. Harden Linux Server
- **File**: `2-harden.sh`
- **Description**: Lists all world-writable directories and sets their permissions to a more secure level.
- **Usage**: `sudo ./2-harden.sh`

### 3. Identify Common Vulnerabilities
- **File**: `3-identify.sh`
- **Description**: Checks for unpatched common vulnerabilities using the `lynis` audit tool.
- **Usage**: `sudo ./3-identify.sh`

### 4. Check for NFS Vulnerabilities
- **File**: `4-nfs.sh`
- **Description**: Scans for NFS shares that are accessible by anyone on the network.
- **Usage**: `sudo ./4-nfs.sh <target-ip>`

### 5. Audit SNMP Configuration
- **File**: `5-snmp.sh`
- **Description**: Finds SNMP configurations that allow public access.
- **Usage**: `sudo ./5-snmp.sh`

### 6. Examine SMTP Server Settings
- **File**: `6-smtp.sh`
- **Description**: Checks the SMTP server configuration for lack of STARTTLS or other security features.
- **Usage**: `sudo ./6-smtp.sh`

### 7. Simulate DoS Attack on HTTP Server
- **File**: `7-dos.sh`
- **Description**: Simulates a basic Denial of Service attack on an HTTP server using `hping3`.
- **Usage**: `sudo ./7-dos.sh <target-ip>`
- **Note**: For educational purposes only. Only use on systems you own or have permission to test.

### 8. Check for Weak SSL/TLS Ciphers
- **File**: `8-cipher.sh`
- **Description**: Tests an SSL/TLS server's ciphers and reports any weak ciphers using `nmap`.
- **Usage**: `sudo ./8-cipher.sh <target-ip>`

### 9. Implement Basic Firewall Rules
- **File**: `9-firewall.sh`
- **Description**: Sets up basic iptables firewall rules that block all incoming traffic except SSH.
- **Usage**: `sudo ./9-firewall.sh`

## Requirements

- Most scripts require root privileges (`sudo`)
- The following tools should be installed:
  - iptables
  - grep
  - find
  - lynis
  - showmount (NFS utils)
  - hping3
  - nmap

## Important Notes

- These scripts are designed for educational and security assessment purposes
- Always obtain proper authorization before running security tests on any system
- The scripts are intentionally simple (most are exactly 2 lines) for educational clarity
- In production environments, more comprehensive security measures would be recommended