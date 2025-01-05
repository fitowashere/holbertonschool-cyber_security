# Wireshark Network Scanning Detection Filters

This repository contains a collection of Wireshark filters designed to detect various types of network scanning techniques commonly used with tools like nmap and arp-scan.

## 0. IP Protocol Scan
**Filter:** `ip.proto == 1`

Detects packets from nmap's IP protocol scan (`nmap -sO <target>`). This filter captures ICMP packets used during the protocol scan.

## 1. TCP SYN Scan
**Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0 and tcp.window_size <= 1024`

Detects packets from nmap's TCP SYN scan (`nmap -sS <target>`). This filter identifies:
- SYN flag set
- ACK flag not set
- Window size less than or equal to 1024

## 2. TCP Connect Scan
**Filter:** `tcp.flags.syn == 1 && tcp.flags.ack == 0 && tcp.flags.reset == 1 and tcp.window_size > 1024`

Detects packets from nmap's TCP Connect scan (`nmap -sT <target>`). This filter captures:
- SYN flag set
- ACK flag not set
- RST flag set
- Window size greater than 1024

## 3. TCP FIN Scan
**Filter:** `tcp.flags.fin == 0x001`

Detects packets from nmap's TCP FIN scan (`nmap -sF <target>`). This filter ensures only the FIN flag is set using hex notation (0x001).

## 4. TCP Ping Sweeps
**Filter:** `(tcp.flags.syn == 1 && tcp.flags.ack == 0) || (tcp.flags.ack == 1 && tcp.flags.syn == 0)`

Detects packets from nmap's TCP ping sweep (`nmap -sn -PS/-PA <subnet>`). This filter captures both:
- TCP SYN ping packets
- TCP ACK ping packets

## 5. UDP Port Scan
**Filter:** `udp or (icmp.type == 3 and icmp.code == 3)`

Detects packets from nmap's UDP port scan (`nmap -sU <target>`). This filter captures:
- UDP packets
- ICMP Port Unreachable messages (type 3, code 3)

## 6. UDP Ping Sweeps
**Filter:** `udp.dstport == 7`

Detects packets from nmap's UDP ping sweep (`nmap -sn -PU <subnet>`). This filter specifically captures:
- UDP packets sent to port 7 (Echo port)
- More precise than capturing all UDP traffic

## 7. ICMP Ping Sweep
**Filter:** `icmp.type == 8`

Detects packets from nmap's ICMP ping sweep (`nmap -sn -PE <subnet>`). This filter captures:
- ICMP Echo request packets (type 8)
- Used for host discovery

## 8. ARP Scanning
**Filter:** `arp.dst.hw_mac == 00:00:00:00:00:00`

Detects packets from ARP scanning (`arp-scan -l`). This filter captures:
- ARP packets with destination MAC address set to all zeros
- Specific characteristic of the arp-scan tool

## Repository Structure
```
holbertonschool-cyber_security/
└── network_security/
    └── 0x05_wireshark_basics/
        ├── 0-ip_scan.txt
        ├── 1-tcp_syn.txt
        ├── 2-tcp_connect_scan.txt
        ├── 3-tcp_fin.txt
        ├── 4-tcp_ping_sweep.txt
        ├── 5-udp_port_scan.txt
        ├── 6-udp_ping_sweep.txt
        ├── 7-icmp_ping_sweep.txt
        └── 8-arp_scanning.txt
```

## Usage
1. Open Wireshark and start a new capture
2. Copy the desired filter into Wireshark's filter bar
3. Run the corresponding scan command
4. Observe the captured packets matching your filter

## Note
These filters are designed to detect specific scanning techniques. Be aware that:
- Some scans require root/sudo privileges
- Network scanning should only be performed on networks you have permission to test
- These filters may need adjustment based on specific network configurations or tool versions