# Passive Reconnaissance Tools

This repository contains tools for passive reconnaissance, focusing on WHOIS information gathering and DNS record lookups.

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

### Code Explanation

```bash
#!/bin/bash
whois $1 | awk -F': ' '/^Registrant |^Admin |^Tech / {print $1 "," $2}' > "$1.csv"
```

## 1-a_record.sh

A bash script that retrieves the A records of a specified domain using the nslookup command.

### Features

- Retrieves A records for any domain
- Uses nslookup's default DNS server
- Shows both authoritative and non-authoritative answers

### Usage

```bash
./1-a_record.sh domain_name
```

Example:
```bash
./1-a_record.sh holbertonschool.com
```

### Sample Output

```
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   holbertonschool.com
Address: 75.2.70.75
Name:   holbertonschool.com
Address: 99.83.190.102
```

### Code Explanation

```bash
#!/bin/bash
nslookup -query=A $1
```

## 2-mx_record.sh

A bash script that retrieves the MX records of a specified domain using the nslookup command.

### Features

- Retrieves MX (Mail Exchanger) records for any domain
- Shows mail server priorities
- Uses nslookup's default DNS server

### Usage

```bash
./2-mx_record.sh domain_name
```

Example:
```bash
./2-mx_record.sh holbertonschool.com
```

### Sample Output

```
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
holbertonschool.com     mail exchanger = 1 aspmx.l.google.com.
holbertonschool.com     mail exchanger = 10 alt3.aspmx.l.google.com.
holbertonschool.com     mail exchanger = 10 alt4.aspmx.l.google.com.
holbertonschool.com     mail exchanger = 5 alt1.aspmx.l.google.com.
holbertonschool.com     mail exchanger = 5 alt2.aspmx.l.google.com.
```

### Code Explanation

```bash
#!/bin/bash
nslookup -query=MX $1
```

### Requirements

- Linux/Unix environment
- whois command installed
- nslookup command installed
- awk (GNU version)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Make the scripts executable:
```bash
chmod +x *.sh*
```