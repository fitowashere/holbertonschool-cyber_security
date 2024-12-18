# Active Reconnaissance

## Description
This project focuses on the fundamental principles of network security and active reconnaissance. Through a series of tasks, you'll learn how to perform basic network scanning, port detection, and vulnerability assessment in a controlled environment.

## Prerequisites
- Basic understanding of networking concepts
- Familiarity with Linux command line
- VPN access
- Nmap installed on your system
- Wappalyzer browser extension
- SQLmap installed on your system
- Gobuster installed on your system

## Project Structure
```
holbertonschool-cyber_security/
└── network_security/
    └── 0x02_active_reconnaissance/
        ├── README.md
        ├── 0-ports.txt
        ├── 1-webserver.txt
        ├── 2-injectable.txt
        ├── 3-database.txt
        ├── 4-tables.txt
        ├── 5-hidden_dir.txt
        ├── 100-flag.txt
        ├── 101-flag.txt
        └── 102-flag.txt
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
echo "/orders" > 2-injectable.txt
```

### Format Rules
- Include leading slash
- Don't include domain name
- Don't include parameters
- Don't include trailing slashes

## Task 4: SQL Injection Enumeration
### Objective
Use SQLmap to discover the database name and count the number of tables it contains.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Tool: SQLmap
- Output Files: 
  - Database name in `3-database.txt`
  - Table count in `4-tables.txt`

### Steps
1. Use SQLmap to find database name:
```bash
sqlmap -u "http://active.hbtn/products" --dbs --random-agent --batch
```

2. Once database is found, enumerate tables:
```bash
sqlmap -u "http://active.hbtn/products" -D <database_name> --tables --random-agent --batch
```

3. Save the findings:
```bash
# Save database name
echo "<database_name>" > 3-database.txt

# Save number of tables
echo "<number_of_tables>" > 4-tables.txt
```

### Useful SQLmap Options
- `--dbs`: List available databases
- `-D`: Specify target database
- `--tables`: Enumerate tables
- `--batch`: Never ask for user input
- `--random-agent`: Use random User-Agent
- `--level=5 --risk=3`: More thorough testing
- `--tamper=space2comment`: Bypass WAF
- `--forms`: Test form parameters for injection

### Output Format
For database name:
```
database_name
```

For table count:
```
number
```

### Note
- Make sure to use the injectable endpoint found in Task 3
- Both output files should contain only the requested information without extra spaces or characters
- Do not include quotes or other formatting in the output files

## Task 5: Directory Enumeration
### Objective
Find the hidden admin panel login page using directory enumeration techniques.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Tool: gobuster
- Output Format: Admin panel path in `5-hidden_dir.txt`

### Steps
1. Run gobuster with specified options:
```bash
gobuster dir \
  -u http://active.hbtn \
  -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt \
  -b 302
```

2. Identify admin panel path from results

3. Save the found path:
```bash
echo "/admin_path" > 5-hidden_dir.txt
```

### Command Options
- `dir`: Directory enumeration mode
- `-u`: Target URL
- `-w`: Wordlist path
- `-b 302`: Ignore 302 status codes

### Output Format Rules
- Include leading slash
- Don't include domain name
- Don't include trailing slashes
- Don't include parameters

### Example
If admin panel is at `http://active.hbtn/admin_panel`, save as:
```bash
echo "/admin_panel" > 5-hidden_dir.txt
```

### Tips
- Watch for common admin paths:
  - /admin
  - /administrator
  - /adminpanel
  - /backend
  - /control
  - /cp
  - /manage

## Task 6: Admin Panel Flag Discovery
### Objective
Find the third flag hidden in the admin panel.

### Requirements
- Target Machine: `cyber_netsec_0x02`
- Endpoint: `http://active.hbtn`
- Location: Admin panel (found in Task 6)
- Output Format: Flag value in `102-flag.txt`

### Steps
1. Navigate to the admin panel URL found in Task 6
2. Check these locations:
   - Page source code
   - HTML comments
   - Response headers
   - Form fields
   - Hidden inputs
   - Error messages
   - JavaScript files

3. Save the flag when found:
```bash
echo "FLAG_VALUE" > 102-flag.txt
```

### Areas to Check
- Page source (Ctrl+U)
- Developer Tools:
  - Network tab
  - Console tab
  - Elements tab
  - Application tab
- Response headers
- Login error messages
- Hidden form fields

### Note
- The flag is "exposed clearly" in the admin panel
- Look for obvious flags before trying complex exploitation
- Make sure to check both client-side and server-side responses

## Tips
- Always ensure you have proper authorization before scanning
- Use appropriate nmap flags based on your needs
- Document all findings accurately
- Follow the exact output format specified
- Make sure Wappalyzer is properly installed and enabled in your browser
- When saving flags or paths, ensure there are no extra spaces or characters
- Be mindful of web application security testing best practices
- Verify all findings before submitting

## License
This project is part of the Holberton School curriculum.