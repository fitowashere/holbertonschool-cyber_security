# Linux Security Basics

## Description
This project focuses on fundamental Linux security concepts and practices. Through various scripts and exercises, we explore different aspects of system security, user management, and access monitoring.

## Project Structure
```
holbertonschool-cyber_security/
└── linux_security/
    └── 0x00_linux_security_basics/
        ├── 0-login.sh
        ├── 1-active-connections.sh
        └── README.md
```

## Tasks

### 0. What secrets hold
A script that displays the last 5 login sessions for users with their corresponding dates.

#### Script: `0-login.sh`
```bash
#!/bin/bash
sudo last -F -5
```

- **Usage**: `sudo ./0-login.sh`
- **Features**:
  - Uses the `last` command to display login history
  - `-F` flag for full timestamps
  - `-5` flag to limit output to 5 entries
  - Requires root privileges
- **Output Example**:
  ```
  root     tty1         Thu Oct 12 10:08:24 2023   still logged in
  root     ttyS0        Thu Oct 12 10:08:23 2023   still logged in
  reboot   system boot  Thu Oct 12 10:08:10 2023   still running
  root     tty1         Tue Oct 10 15:08:21 2023 - down   (19:26)
  root     ttyS0        Tue Oct 10 15:08:21 2023 - down   (19:26)
  ```

### 1. Shows your Linux connections, not your social status!
A script that displays a list of network socket connections with specific requirements.

#### Script: `1-active-connections.sh`
```bash
#!/bin/bash
sudo ss -tanp
```

- **Usage**: `sudo ./1-active-connections.sh`
- **Features**:
  - Uses the `ss` command from iproute2 5.x
  - `-t`: Shows TCP sockets
  - `-a`: Shows all sockets (listening and non-listening)
  - `-n`: Displays numerical addresses (IP and ports)
  - `-p`: Shows process information
- **Output Example**:
  ```
  State   Recv-Q   Send-Q     Local Address:Port   Peer Address:Port   Process                                              
  LISTEN  0        128        0.0.0.0:22           0.0.0.0:*
  LISTEN  0        100        0.0.0.0:5000         0.0.0.0:*
  LISTEN  0        5          127.0.0.1:5901       0.0.0.0:*          users:(("Xtigervnc",pid=923,fd=9))
  ```

### 2. Firewall rules: Your network's first line of defense!
A script that allows only incoming connections with the TCP protocol through port 80.

#### Script: `2-incoming_connections.sh`
```bash
#!/bin/bash
sudo ufw allow 80/tcp
```

- **Usage**: `sudo ./2-incoming_connections.sh`
- **Features**:
  - Uses UFW (Uncomplicated Firewall)
  - Allows incoming TCP traffic on port 80
  - Requires root privileges
- **Output Example**:
  ```
  Rules updated
  Rules updated (v6)
  ```

### 3. Securing your network, one rule at a time!
A script that lists all rules in the security table of the firewall with verbose output.

#### Script: `3-firewall_rules.sh`
```bash
#!/bin/bash
sudo iptables -v -L
```

- **Usage**: `sudo ./3-firewall_rules.sh`
- **Features**:
  - Lists all firewall rules
  - Uses verbose mode for detailed output
  - Shows packet and byte counts
- **Output Example**:
  ```
  Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
   pkts bytes target     prot opt in     out     source               destination         

  Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
   pkts bytes target     prot opt in     out     source               destination         

  Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
   pkts bytes target     prot opt in     out     source               destination
  ```

### 4. See what's talking, and who's listening!
A script that lists services, their current state, and their corresponding ports.

#### Script: `4-network_services.sh`
```bash
#!/bin/bash
sudo netstat -tunlp
```

- **Usage**: `sudo ./4-network_services.sh`
- **Features**:
  - Shows TCP sockets (`-t`)
  - Shows UDP sockets (`-u`)
  - Shows numerical addresses (`-n`)
  - Shows only listening sockets (`-l`)
  - Shows PID and program name (`-p`)
- **Output Example**:
  ```
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
  tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      881/sshd: /usr/sbin 
  tcp        0      0 0.0.0.0:5000            0.0.0.0:*               LISTEN      913/python3
  udp        0      0 0.0.0.0:68              0.0.0.0:*                           525/dhclient
  ```

### 5. Where it talks, we all listen!
A script that initiates a system audit using Lynis to scan the machine for security configurations and possible improvements.

#### Script: `5-audit_system.sh`
```bash
#!/bin/bash
sudo lynis audit system
```

- **Usage**: `sudo ./5-audit_system.sh`
- **Features**:
  - Performs comprehensive system security audit
  - Checks system configuration
  - Identifies security issues
  - Provides recommendations
- **Output Example**:
  ```
  [ Lynis 3.0.8 ]

  ################################################################################
    Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
    welcome to redistribute it under the terms of the GNU General Public License.
    See the LICENSE file for details about using this software.
  ################################################################################

  [+] Initializing program
  ------------------------------------
    - Detecting OS...                                           [ DONE ]
    - Checking profiles...                                      [ DONE ]
  ```

### 6. Your eyes and ears on the network!
A script that captures and analyzes network traffic going through the system.

#### Script: `6-capture_analyze.sh`
```bash
#!/bin/bash
sudo tcpdump -c 5
```

- **Usage**: `sudo ./6-capture_analyze.sh`
- **Features**:
  - Uses tcpdump for packet capture
  - `-c 5`: Limits capture to 5 packets
  - Displays detailed packet information
- **Output Example**:
  ```
  tcpdump: data link type LINUXSLL2
  tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
  listening on any, link-type LINUX_SLL2 (Linux cooked v2), snapshot length 262144 bytes
  09:10:03.397281 eth0  In  IP ip-6-19-0-167.eu-central-1.compute.internal.36014 > ip-6-19-156-8.eu-central-1.compute.internal.5000: Flags [P.], seq 3466652703:3466652721, ack 3521647673, win 24559, options [nop,nop,TS val 17390194 ecr 4276499227], length 18
  [...]
  5 packets captured
  27 packets received by filter
  0 packets dropped by kernel
  ```

### 7. So fast, it'll make your router sweat!
A script that scans a subnetwork to discover live hosts using nmap.

#### Script: `7-scan.sh`
```bash
#!/bin/bash
sudo nmap "$1"
```

- **Usage**: `sudo ./7-scan.sh [target]`
- **Example**: `sudo ./7-scan.sh www.holbertonschool.com`
- **Features**:
  - Uses nmap for network scanning
  - Accepts target as command line argument
  - Performs TCP port scanning
  - Shows open ports and services
- **Output Example**:
  ```
  Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-19 15:46 UTC
  Nmap scan report for www.holbertonschool.com (34.249.200.254)
  Host is up (0.026s latency).
  Not shown: 998 filtered tcp ports (no-response)
  PORT    STATE SERVICE
  80/tcp  open  http
  443/tcp open  https
  ```

## Requirements
- Linux operating system
- Root or sudo privileges
- Bash shell
- iproute2 version 5.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/[username]/holbertonschool-cyber_security.git
   ```
2. Navigate to the project directory:
   ```bash
   cd holbertonschool-cyber_security/linux_security/0x00_linux_security_basics
   ```
3. Make the scripts executable:
   ```bash
   chmod +x 0-login.sh 1-active-connections.sh
   ```

## Usage
Run the scripts with sudo privileges:
```bash
sudo ./0-login.sh
sudo ./1-active-connections.sh
```

## License
This project is part of the Holberton School Cyber Security curriculum.