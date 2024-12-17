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

## 3-txt_record.sh

A bash script that retrieves the TXT records of a specified domain using the nslookup command.

### Features

- Retrieves TXT records for any domain
- Shows domain verification records, SPF records, and other text-based DNS records
- Automatically handles TCP mode for truncated responses

### Usage

```bash
./3-txt_record.sh domain_name
```

Example:
```bash
./3-txt_record.sh holbertonschool.com
```

### Sample Output

```
;; Truncated, retrying in TCP mode.
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
holbertonschool.com     text = "1C8BC5F558"
holbertonschool.com     text = "MS=BB8A869E4E8A47D208F560DE7D83F199D1BB8F4F"
holbertonschool.com     text = "apple-domain-verification=sqTGlUgV9vVTnBuB"
holbertonschool.com     text = "dropbox-domain-verification=pvxn88z3e06i"
holbertonschool.com     text = "google-site-verification=lnffgexG_GGal6Fa53z0Ve4dJY4z4GXAmy1I2_ldotk"
holbertonschool.com     text = "v=spf1 include:mailgun.org include:_spf.google.com ~all"
```

### Code Explanation

```bash
#!/bin/bash
nslookup -query=TXT $1
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