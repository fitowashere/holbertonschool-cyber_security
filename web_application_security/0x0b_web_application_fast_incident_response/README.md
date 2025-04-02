# Web Application Fast Incident Response

This directory contains scripts for responding to security incidents in web applications, particularly for analyzing log files to identify and gather information about potential attacks.

## Scripts

### 0-attack_ip.sh
Identifies the IP address responsible for the most requests in a log file, which is likely the source of a Denial of Service (DoS) attack.

#### Usage
```
./0-attack_ip.sh
```

#### Functionality
* Extracts IP addresses from the log file (logs.txt)
* Counts the occurrences of each IP address
* Identifies and prints the IP address with the highest number of requests

### 1-endpoint.sh
Finds the endpoint (URL) that received the most requests, indicating it was likely the target of the attack.

#### Usage
```
./1-endpoint.sh
```

#### Functionality
* Extracts the requested URLs from the log file
* Counts the occurrences of each endpoint
* Identifies and prints the most frequently requested endpoint

### 2-count_attack.sh
Determines how many requests the attacker has sent, where the attacker is identified as the IP address with the highest number of requests.

#### Usage
```
./2-count_attack.sh
```

#### Functionality
* Identifies the IP address with the most requests (assumed to be the attacker)
* Counts the total number of requests made by that IP address

### 3-library.sh
Identifies which tool or library the attacker used by analyzing the User-Agent strings.

#### Usage
```
./3-library.sh
```

#### Functionality
* Filters the log for requests made by the attacker (most frequent IP)
* Extracts and counts the User-Agent strings
* Identifies the tool/library used by the attacker

## Requirements
* All scripts are written in Bash
* The first line of all files is exactly `#!/bin/bash`
* All files are executable
* Scripts follow the specified constraints (no backticks, &&, ||, or ;)
* Scripts work with the logs.txt file in the current directory