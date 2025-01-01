# Host Discovery with Nmap

This project demonstrates various network host discovery techniques using Nmap. We explore four distinct scanning methods: ARP scanning, ICMP Echo scanning, ICMP Timestamp scanning, and ICMP Address Mask scanning. Each approach leverages different network protocols and operates at different OSI model layers, providing unique advantages for specific scenarios.

## Script Overview

### 1. ARP Scanning (0-arp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PR $1
```

ARP scanning uses Address Resolution Protocol to discover hosts on local networks. The flags serve specific purposes:
- `-sn`: Disables port scanning, focusing purely on host discovery
- `-PR`: Activates ARP scan mode for sending ARP requests
- `$1`: Represents the subnet argument provided by the user

### 2. ICMP Echo Scanning (1-icmp_echo_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PE $1
```

ICMP Echo scanning employs the traditional ping mechanism. The script uses these flags:
- `-sn`: Performs host discovery without port scanning
- `-PE`: Enables ICMP Echo scanning mode
- `$1`: Takes the subnet argument for scanning

### 3. ICMP Timestamp Scanning (2-icmp_timestamp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PP $1
```

ICMP Timestamp scanning utilizes a different type of ICMP message. The script includes:
- `-sn`: Restricts scanning to host discovery
- `-PP`: Activates ICMP Timestamp scanning
- `$1`: Accepts the target subnet as an argument

### 4. ICMP Address Mask Scanning (3-icmp_address_mask_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PM $1
```

ICMP Address Mask scanning represents another ICMP variant. The script uses:
- `-sn`: Limits the scan to host discovery
- `-PM`: Enables ICMP Address Mask scanning
- `$1`: Receives the subnet parameter

## Understanding the Scanning Methods

### ARP Scanning
Operating at Layer 2 (Data Link Layer), ARP scanning works by sending ARP requests within a local network segment. This method:
- Provides the fastest scanning on local networks
- Reveals MAC addresses of responding hosts
- Works only within the same subnet
- Generates minimal network traffic
- Typically provides the most accurate results for local network mapping

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-22 05:02 CDT
Nmap scan report for 192.168.65.1
Host is up (0.00064s latency).
MAC Address: C6:91:0C:4B:4E:64 (Unknown)
Nmap scan report for 192.168.65.2
Host is up.
Nmap done: 256 IP addresses (2 hosts up) scanned in 2.03 seconds
```

### ICMP Echo Scanning
Working at Layer 3 (Network Layer), ICMP Echo scanning sends traditional ping requests. This method:
- Functions across different network segments
- Uses widely supported ICMP Echo messages
- May be blocked by firewalls
- Provides reliable host discovery when ICMP traffic is allowed
- Works similarly to standard ping but more efficiently

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:02 CDT
Nmap scan report for 6.19.100.2
Host is up (0.14s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.03 seconds
```

### ICMP Timestamp Scanning
Also operating at Layer 3, ICMP Timestamp scanning uses timestamp request messages. This technique:
- May bypass firewalls that block Echo requests
- Provides an alternative when standard ping is filtered
- Often receives different responses than Echo requests
- Can reveal hosts that don't respond to regular pings
- Usually takes slightly longer than Echo scanning

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:17 CDT
Nmap scan report for 6.19.100.2
Host is up (0.16s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.93 seconds
```

### ICMP Address Mask Scanning
This Layer 3 scanning method uses ICMP Address Mask requests. The technique:
- Employs a less common ICMP message type
- Might reveal subnet configuration details
- Often receives fewer responses than other methods
- Can bypass certain firewall rules
- Takes longer to complete than other scanning methods

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 254 IP address (0 hosts up) scanned in 53.01 seconds
```

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

Each script will request sudo privileges if needed and display discovered hosts in the specified subnet.

## Prerequisites

- Linux-based operating system
- Nmap installed on your system
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
  - `3-icmp_address_mask_scan.sh`: ICMP Address Mask scanning script
  - `README.md`: Documentation file

Note: These scripts are intended for educational purposes and should only be used on networks where you have explicit permission to perform scanning activities.