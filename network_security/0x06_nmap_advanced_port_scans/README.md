# Nmap Advanced Port Scans

This repository contains a collection of bash scripts that demonstrate various advanced port scanning techniques using Nmap. These scripts are designed to explore different methods of network reconnaissance and security testing.

## Overview

Network scanning is a crucial aspect of cybersecurity, allowing professionals to identify potential vulnerabilities and assess the security posture of systems. This project focuses on stealth scanning techniques that can be useful for security assessments when standard scanning methods might be detected or blocked.

## Techniques Covered

### 1. NULL Scan (`0-null_scan.sh`)
- Sends TCP packets with no flags set
- Can bypass simple packet filters
- Useful for detecting open ports stealthily

### 2. FIN Scan (`1-fin_scan.sh`)
- Sends TCP packets with only the FIN flag set
- Uses packet fragmentation and reduced timing to enhance stealth
- Targets ports 80-85 with timing option 2 for reduced detectability

### 3. Xmas Scan (`2-xmas_scan.sh`)
- Utilizes TCP packets with FIN, PSH, and URG flags set
- Named for its "illuminated" packet headers resembling Christmas lights
- Shows all packets sent/received and reasons for port states

### 4. Maimon Scan (`3-maimon_scan.sh`)
- Sends TCP packets with both FIN and ACK flags set
- Named after its discoverer, Uriel Maimon
- Less common than other scan types, potentially evading detection

### 5. TCP ACK Scan (`4-ask_scan.sh`)
- Primary tool for determining firewall filtering rules
- Sends packets with only the ACK flag set
- Distinguishes between stateful and simple packet filters

### 6. TCP Window Scan (`5-window_scan.sh`)
- Analyzes the TCP window size in RST packets
- More sophisticated version of the ACK scan
- Can reveal information even when standard scanning is blocked

### 7. Custom Scan (`6-custom_scan.sh`)
- Sends packets with all TCP flags set (URG, ACK, PSH, RST, SYN, FIN)
- Creates highly unusual packet configurations
- Saves scan output to a file with no terminal output

## Usage

Each script follows a similar pattern of execution:

```bash
./script_name.sh [target_host] [additional_options]
```

For example:
```bash
./0-null_scan.sh www.example.com
./5-window_scan.sh www.example.com 20-30 25-28
```

## Requirements

- Nmap installed on your system
- Root privileges (all scripts use sudo)
- Bash shell

## Security Notice

These scanning techniques are provided for educational purposes and legitimate security testing only. Always ensure you have proper authorization before scanning any networks or systems that you do not own.

## License

This project is part of the Holberton School Cyber Security curriculum.
