# Host Discovery with Nmap

This project explores network host discovery using various Nmap scanning techniques. We implement different methods operating across multiple layers of the OSI model: ARP at Layer 2, ICMP at Layer 3, and TCP/UDP at Layer 4. Each technique offers unique advantages and suits different network scenarios. Additionally, the project includes a practical CTF challenge focusing on UDP service enumeration.

## Script Overview

### 1. ARP Scanning (0-arp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PR $1
```

ARP scanning works at the Data Link Layer (Layer 2), sending ARP requests to discover hosts on a local network. The command flags serve specific purposes:
- `-sn`: Disables port scanning, focusing purely on host discovery 
- `-PR`: Activates ARP scan mode for sending ARP requests
- `$1`: Represents the subnet argument provided by the user

### 2. ICMP Echo Scanning (1-icmp_echo_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PE $1
```

ICMP Echo scanning employs the traditional ping mechanism at the Network Layer (Layer 3). The script uses these flags:
- `-sn`: Performs host discovery without port scanning
- `-PE`: Enables ICMP Echo scanning mode
- `$1`: Takes the subnet argument for scanning

### 3. ICMP Timestamp Scanning (2-icmp_timestamp_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PP $1
```

Operating at Layer 3, ICMP Timestamp scanning provides an alternative to Echo requests by using timestamp messages. The script includes:
- `-sn`: Restricts scanning to host discovery
- `-PP`: Activates ICMP Timestamp scanning
- `$1`: Accepts the target subnet as an argument

### 4. ICMP Address Mask Scanning (3-icmp_address_mask_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PM $1
```

Another Layer 3 technique, ICMP Address Mask scanning uses mask requests to discover hosts. The script employs:
- `-sn`: Limits the scan to host discovery
- `-PM`: Enables ICMP Address Mask scanning
- `$1`: Receives the subnet parameter

### 5. TCP SYN Ping Scanning (4-tcp_syn_ping.sh)
```bash
#!/bin/bash
sudo nmap -sn -PS22,80,443 $1
```

Moving to Layer 4, TCP SYN Ping scanning sends SYN packets to common service ports. The flags indicate:
- `-sn`: Disables port scanning for focused host discovery
- `-PS22,80,443`: Performs TCP SYN Ping scanning on ports 22 (SSH), 80 (HTTP), and 443 (HTTPS)
- `$1`: Takes the subnet argument

### 6. TCP ACK Ping Scanning (5-tcp_ack_ping.sh)
```bash
#!/bin/bash
sudo nmap -sn -PA22,80,443 $1
```

Another Layer 4 approach, TCP ACK Ping scanning sends ACK packets to detect hosts. The command uses:
- `-sn`: Ensures scan focuses on host discovery
- `-PA22,80,443`: Activates TCP ACK Ping scanning on specified ports
- `$1`: Represents the target subnet

### 7. UDP Ping Scanning (6-udp_ping_scan.sh)
```bash
#!/bin/bash
sudo nmap -sn -PU53,161,162 $1
```

UDP Ping scanning offers a connectionless approach at Layer 4. The command flags indicate:
- `-sn`: Restricts to host discovery
- `-PU53,161,162`: Activates UDP Ping scanning on common UDP service ports
- `$1`: Takes the subnet argument

### 8. CTF Challenge: UDP Service Version Detection
This practical challenge requires identifying a flag hidden in UDP service version information:
```bash
sudo nmap -sUV -p200-300 cybernetsec0x04
```

The scan combines several important elements:
- `-sU`: Enables UDP scanning
- `-V`: Activates version detection
- `-p200-300`: Specifies the port range
- Target specific host: cybernetsec0x04

## Understanding the Scanning Methods

### ARP Scanning
Operating at Layer 2, ARP scanning excels in local network discovery:
- Fastest method for local network scanning
- Reveals MAC addresses of responding hosts
- Minimal network overhead
- Limited to local subnet operation

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
This Layer 3 method uses traditional ping requests:
- Works across network boundaries
- Widely supported by network devices
- May be blocked by firewalls
- Provides reliable host discovery when allowed

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:02 CDT
Nmap scan report for 6.19.100.2
Host is up (0.14s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.03 seconds
```

### ICMP Timestamp Scanning
Also at Layer 3, this method uses timestamp requests:
- Alternative when Echo requests are blocked
- May bypass certain firewall rules
- Provides timing information
- Generally good response rates

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:17 CDT
Nmap scan report for 6.19.100.2
Host is up (0.16s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 19.93 seconds
```

### ICMP Address Mask Scanning
This Layer 3 technique uses mask requests:
- Less common ICMP message type
- May reveal network configuration
- Often receives fewer responses
- Useful in specific environments

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 254 IP address (0 hosts up) scanned in 53.01 seconds
```

### TCP SYN Ping Scanning
At Layer 4, this method sends SYN packets:
- Effective when ICMP is blocked
- Works well with common services
- Provides service availability hints
- Balanced stealth and effectiveness

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 14:40 CDT
Nmap scan report for 6.19.100.2
Host is up (0.12s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 22.42 seconds
```

### TCP ACK Ping Scanning
Another Layer 4 technique using ACK packets:
- More stealthy than SYN ping
- Bypasses stateless firewalls
- Works across various OS types
- Effective when other methods fail

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-10 15:15 CDT
Nmap done: 256 IP addresses (0 hosts up) scanned in 154.50 seconds
```

### UDP Ping Scanning
The connectionless Layer 4 approach:
- Useful when TCP scanning is blocked
- Targets common UDP services
- Relies on ICMP error messages
- Complementary to TCP methods

Example output:
```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 15:10 CDT
Nmap scan report for 6.19.100.2
Host is up (0.13s latency).
Nmap done: 256 IP addresses (1 host up) scanned in 23.39 seconds
```

## UDP Service Version Detection for CTF
This specialized technique combines discovery with service enumeration:
- Performs detailed version detection
- Uses protocol-specific probes
- Requires patience due to UDP nature
- May reveal hidden information in service details

## Usage

For any script:

1. Make it executable:
```bash
chmod +x script_name.sh
```

2. Run with target subnet:
```bash
./script_name.sh 192.168.1.0/24
```

## Prerequisites

1. System Requirements:
   - Linux-based operating system
   - Nmap installed
   - Root/sudo privileges

2. Network Requirements:
   - Permission to scan target network
   - Appropriate network access
   - Understanding of network security implications

3. Knowledge Requirements:
   - Basic networking concepts
   - Understanding of different protocols
   - Familiarity with command-line operations

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
  - `6-udp_ping_scan.sh`: UDP Ping scanning script
  - `100-flag.txt`: CTF challenge flag
  - `README.md`: Documentation file

## CTF Challenge Tips

For successful flag capture:

1. Preparation:
   - Ensure root/sudo access
   - Verify network connectivity
   - Review UDP scanning concepts

2. Scanning Strategy:
   - Focus on ports 200-300
   - Be patient with UDP scanning
   - Watch for unusual version strings

3. Analysis:
   - Examine all service information carefully
   - Look for non-standard responses
   - Consider using additional Nmap scripts if needed

Note: These scripts and techniques are intended for educational purposes and should only be used on networks where you have explicit permission to perform scanning activities. The CTF challenge is designed to teach practical UDP service enumeration skills in a controlled environment.