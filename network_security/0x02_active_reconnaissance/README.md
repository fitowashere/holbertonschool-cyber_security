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
        ├── 1-webserver.txt
        ├── 2-injectable.txt
        └── 100-flag.txt
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

## Task 2: Source Code Inspection
### Objective
Find the first flag hidden in the website's source code.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Output Format: Flag value in `100-flag.txt`

### Steps
1. Visit the target website in your browser
2. View the page source (Ctrl+U or right-click -> View Page Source)
3. Search for comments and hidden content
4. Save the found flag in the required format

### Areas to Check
- HTML comments (`<!-- -->`)
- Hidden input fields
- Meta tags
- Commented-out code sections
- Bottom of the page
- JavaScript code blocks

### Expected Output Format
```
FLAG_VALUE
```
Save the output to `100-flag.txt` without any extra spaces, quotes, or newlines.

## Task 3: Injectable Path Discovery
### Objective
Identify potentially vulnerable pages that accept parameters or form submissions.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Output Format: Path to vulnerable page in `2-injectable.txt`

### Steps
1. Browse through the website
2. Look for pages with:
   - URL parameters (e.g., `/page?id=1`)
   - Form submissions
   - Dynamic content
3. Save only the base pathname

### Common Vulnerable Paths
- `/search`
- `/profile`
- `/user`
- `/product`
- `/admin`
- `/api`

### Example
If vulnerable page is `http://active.hbtn/orders?id=1511515`, save as:
```bash
echo "/product" > 2-injectable.txt
```

### Format Rules
- Include leading slash
- Don't include domain name
- Don't include parameters
- Don't include trailing slashes

## Tips
- Always ensure you have proper authorization before scanning
- Use appropriate nmap flags based on your needs
- Document all findings accurately
- Follow the exact output format specified
- Make sure Wappalyzer is properly installed and enabled in your browser
- When saving flags or paths, ensure there are no extra spaces or characters

## License
This project is part of the Holberton School curriculum.