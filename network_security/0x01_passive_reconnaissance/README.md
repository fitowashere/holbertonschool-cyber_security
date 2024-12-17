# Passive Reconnaissance Tools

This repository contains tools for passive reconnaissance, focusing on WHOIS information gathering and formatting.

## 0-whois.sh

A bash script that extracts specific information from WHOIS lookups and formats it into CSV format.

### Features

- Extracts Registrant, Admin, and Tech information
- Outputs data in CSV format
- Uses efficient awk processing
- Creates output file named after the target domain

### Usage

```bash
./0-whois.sh domain_name
```

Example:
```bash
./0-whois.sh holbertonschool.com
```

### Output Format

The script creates a CSV file with the following information:
- Registrant Information (Name, Organization, Address, etc.)
- Admin Information (Name, Organization, Address, etc.)
- Tech Information (Name, Organization, Address, etc.)

### Sample Output

```csv
Registrant Name,Holberton Inc
Registrant Organization,Holberton Inc
Registrant Street,5670 Wilshire Blvd suite 1802
...
Tech Email,2c420b43d982c37b7621f2015f3e107b-37876677@contact.gandi.net
```

### Requirements

- Linux/Unix environment
- whois command installed
- awk (GNU version)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Make the script executable:
```bash
chmod +x 0-whois.sh
```

### Code Explanation

```bash
#!/bin/bash
whois $1 | awk -F': ' '/^Registrant |^Admin |^Tech / {print $1 "," $2}' > "$1.csv"
```

- Uses whois command to get domain information
- Processes output with awk using ': ' as field separator
- Matches lines starting with Registrant, Admin, or Tech
- Creates CSV format with field name and value
- Saves output to [domain].csv file
