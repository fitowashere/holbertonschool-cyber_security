# Active Reconnaissance

## Description
This project focuses on the fundamental principles of network security and active reconnaissance. Through a series of tasks, you'll learn how to perform basic network scanning, port detection, and vulnerability assessment in a controlled environment.

## Prerequisites
- Basic understanding of networking concepts
- Familiarity with Linux command line
- VPN access
- Nmap installed on your system
- Wappalyzer browser extension

## Project Structure
```
holbertonschool-cyber_security/
└── network_security/
    └── 0x02_active_reconnaissance/
        ├── README.md
        ├── 0-ports.txt
        └── 1-webserver.txt
```

## Task 0: Port Discovery
### Objective
Scan and identify open ports on the target machine using nmap.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Output Format: List of open ports in `0-ports.txt`

### Steps
1. Connect to the VPN server
2. Configure target domain in `/etc/hosts` if needed
3. Run nmap scan on the target
4. Document discovered ports in the required format

### Example Command
```bash
nmap -sV active.hbtn
```

### Expected Output Format
```
port1, port2
```
Save the output to `0-ports.txt`

## Task 1: Web Server Inspection
### Objective
Identify the web server and its version running on the target machine using Wappalyzer.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Tool: Wappalyzer browser extension
- Output Format: Webserver name and version in `1-webserver.txt`

### Steps
1. Configure `/etc/hosts` file:
```bash
sudo bash -c 'echo "<target_ip>    active.hbtn" >> /etc/hosts'
```
2. Visit the target website in your browser
3. Use Wappalyzer to identify the web server
4. Save the information in the required format

### Expected Output Format
```
<webservername> <webserverversion>
```
Save the output to `1-webserver.txt`

## Tips
- Always ensure you have proper authorization before scanning
- Use appropriate nmap flags based on your needs
- Document all findings accurately
- Follow the exact output format specified
- Make sure Wappalyzer is properly installed and enabled in your browser

## License
This project is part of the Holberton School curriculum.