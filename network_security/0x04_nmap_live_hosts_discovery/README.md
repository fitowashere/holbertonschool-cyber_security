# Host Discovery with Nmap

This project demonstrates various network host discovery techniques using Nmap. We explore six distinct scanning methods operating across different layers of the OSI model: ARP scanning at Layer 2, ICMP-based scans at Layer 3, and TCP-based scans at Layer 4. Each method provides unique advantages and is suited for different network scenarios.

## Script Overview

### 1. ARP Scanning (0-arp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PR $1
```

ARP scanning operates at the Data Link Layer, sending ARP requests to discover local network hosts. The command flags serve these purposes:
- `-sn`: Disables port scanning, focusing purely on host discovery 
- `-PR`: Activates ARP scan mode for sending ARP requests
- `$1`: Represents the subnet argument provided by the user

### 2. ICMP Echo Scanning (1-icmp_echo_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PE $1
```

ICMP Echo scanning employs the traditional ping mechanism at the Network Layer. The script uses these flags:
- `-sn`: Performs host discovery without port scanning
- `-PE`: Enables ICMP Echo scanning mode
- `$1`: Takes the subnet argument for scanning

### 3. ICMP Timestamp Scanning (2-icmp_timestamp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PP $1
```

ICMP Timestamp scanning utilizes timestamp requests at the Network Layer. The script includes:
- `-sn`: Restricts scanning to host discovery
- `-PP`: Activates ICMP Timestamp scanning
- `$1`: Accepts the target subnet as an argument

### 4. ICMP Address Mask Scanning (3-icmp_address_mask_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PM $1
```

ICMP Address Mask scanning uses mask requests at the Network Layer. The script employs:
- `-sn`: Limits the scan to host discovery
- `-PM`: Enables ICMP Address Mask scanning
- `$1`: Receives the subnet parameter

### 5. TCP SYN Ping Scanning (4-tcp_syn_ping.sh)
```bash
#!/bin/bash
sudo nmap -sn -PS22,80,443 $1
```

TCP SYN Ping scanning operates at the Transport Layer, sending SYN packets to common ports. The flags indicate:
- `-sn`: Disables port scanning for focused host discovery
- `-PS22,80,443`: Performs TCP SYN Ping scanning on ports 22, 80, and 443
- `$1`: Takes the subnet argument

### 6. TCP ACK Ping Scanning (5-tcp_ack_ping.sh)
```bash
#!/bin/bash
sudo nmap -sn -PA22,80,443 $1
```

TCP ACK Ping scanning uses ACK packets at the Transport Layer. The command uses:
- `-sn`: Ensures scan focuses on host discovery
- `-PA22,80,443`: Activates TCP ACK Ping scanning on specified ports
- `$1`: Represents the target subnet

## Understanding the Scanning Methods

### ARP Scanning
Operating at Layer 2, ARP scanning works by sending ARP requests within a local network segment. This method excels in local network discovery by:
- Providing rapid host detection within the same subnet
- Revealing MAC addresses of responding hosts
- Generating minimal network overhead
- Offering the highest accuracy for local network mapping

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
Working at Layer 3, ICMP Echo scanning sends traditional ping requests across network boundaries. This method provides:
- Cross-subnet scanning capabilities
- Wide compatibility with most network devices
- Simple yet effective host discovery
- Similar functionality to standard ping but with greater efficiency

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:02 CDT
Nmap scan report for 6.19.100.2
Host is up (0.14s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.03 seconds
```

### ICMP Timestamp Scanning
Also at Layer 3, this method sends timestamp requests which may bypass certain firewall rules. Benefits include:
- Alternative path when Echo requests are blocked
- Potential detection of hosts that filter standard pings
- Additional network mapping capabilities through timing information
- Generally good response rates from active hosts

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:17 CDT
Nmap scan report for 6.19.100.2
Host is up (0.16s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.93 seconds
```

### ICMP Address Mask Scanning
This Layer 3 method uses mask requests to discover hosts and potentially gather subnet information. Key characteristics include:
- Less common ICMP message type that might bypass filters
- Potential to reveal network configuration details
- Often receives fewer responses than other ICMP methods
- Useful in specific network environments

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 254 IP address (0 hosts up) scanned in 53.01 seconds
```

### TCP SYN Ping Scanning
Operating at Layer 4, this method sends SYN packets to commonly used ports. The technique offers:
- Effectiveness when ICMP is blocked
- Higher success rates with servers running common services
- Additional insight into potential service availability
- Good balance between stealth and effectiveness

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:40 CDT
Nmap scan report for 6.19.100.2
Host is up (0.12s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 22.42 seconds
```

### TCP ACK Ping Scanning
This Layer 4 technique uses ACK packets to detect hosts, offering several advantages:
- Enhanced stealth compared to SYN ping
- Better success at bypassing stateless firewalls
- Reliable operation across various operating systems
- Effectiveness when other scanning methods fail

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 256 IP addresses (0 hosts up) scanned in 154.50 seconds
```

## Usage

For any of these scripts:

1. Make the script executable:
   ```bash
   chmod +x script_name.sh
   ```

2. Run with a subnet argument:
   ```bash
   ./script_name.sh 192.168.1.0/24
   ```

## Prerequisites

- Linux-based operating system
- Nmap installed on your system
- Root privileges or sudo access
- Basic understanding of networking concepts and protocols
- Permission to perform network scanning on the target network

## Repository Structure

- GitHub repository: `holbertonschool-cyber_security`
- Directory: `network_security/0x04_nmap_live_hosts_discovery`
- Files:
  - `0-arp_scan.sh`: ARP scanning script
  - `1-icmp_echo_scan.sh`: ICMP Echo scanning script
  - `2-icmp_timestamp_scan.sh`: ICMP Timestamp scanning script
  - `3-icmp_address_mask_scan.sh`: ICMP Address Mask scanning script
  - `4-tcp_syn_ping.sh`: TCP SYN Ping scanning script
  - `5-tcp_ack_ping.sh`: TCP ACK Ping scanning script
  - `README.md`: Documentation file

Note: These scripts are intended for educational purposes and should only be used on networks where you have explicit permission to perform scanning activities.