# Host Discovery with Nmap

This project contains bash scripts that demonstrate different techniques for discovering live hosts on a network using Nmap. We implement three fundamental network scanning approaches: ARP scanning, ICMP Echo scanning, and ICMP Timestamp scanning. Each method operates at different layers of the OSI model and has its own advantages and characteristics.

## Script Overview

### 1. ARP Scanning (0-arp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PR $1
```

The ARP scanning script uses Nmap to perform host discovery through ARP requests. The flags `-sn` disable port scanning, while `-PR` specifies ARP scan mode, sending ARP requests to discover hosts. The `$1` parameter represents the subnet you want to scan.

### 2. ICMP Echo Scanning (1-icmp_echo_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PE $1
```

The ICMP Echo scanning script uses the traditional ping-like approach. The `-PE` flag enables ICMP Echo scanning mode, sending ICMP Echo requests (ping) to discover hosts. Like the ARP scan, `-sn` ensures we only perform host discovery.

### 3. ICMP Timestamp Scanning (2-icmp_timestamp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PP $1
```

The ICMP Timestamp scanning script uses an alternative ICMP message type. The `-PP` flag enables ICMP Timestamp scanning mode, which sends ICMP Timestamp requests to potential hosts. This method can sometimes bypass firewalls that block traditional ping requests.

## Understanding the Scanning Methods

### ARP Scanning
ARP scanning operates at Layer 2 of the OSI model, using Address Resolution Protocol to discover hosts. When run on a local network, it sends ARP requests to all potential hosts in the specified subnet. This method provides MAC addresses for responding hosts but only works within the same subnet. It's typically the fastest method for local network scanning.

### ICMP Echo Scanning
ICMP Echo scanning works at Layer 3 of the OSI model, using the same principle as the familiar ping command. It sends ICMP Echo Request packets (Type 8) and waits for ICMP Echo Reply packets (Type 0). While this method works across network segments, it's often blocked by firewalls and security policies.

### ICMP Timestamp Scanning
ICMP Timestamp scanning also operates at Layer 3 but uses ICMP Timestamp Request packets (Type 13) instead of Echo requests. This method can be effective when Echo requests are blocked, as some firewalls may not explicitly filter Timestamp requests. It provides another way to discover hosts while potentially bypassing certain security controls.

## Usage

To use any of these scripts:

1. Make the script executable:
   ```bash
   chmod +x script_name.sh
   ```

2. Run the script with a subnet argument:
   ```bash
   ./script_name.sh 192.168.1.0/24
   ```

Each script will prompt for sudo privileges if needed and display discovered hosts in the specified subnet.

## Prerequisites

- Linux-based operating system
- Nmap installed on the system
- Root privileges or sudo access
- Basic understanding of networking concepts
- Permission to perform network scanning on the target network

## Repository Structure

- GitHub repository: `holbertonschool-cyber_security`
- Directory: `network_security/0x04_nmap_live_hosts_discovery`
- Files:
  - `0-arp_scan.sh`: ARP scanning script
  - `1-icmp_echo_scan.sh`: ICMP Echo scanning script
  - `2-icmp_timestamp_scan.sh`: ICMP Timestamp scanning script
  - `README.md`: Documentation file

Note: These scripts are intended for educational purposes and should only be used on networks where you have explicit permission to perform scanning activities.