# Web Application Forensics

This repository contains scripts for analyzing and investigating web application security incidents through log analysis.

## Project Overview

The objective of this project is to develop scripts that analyze logs from web application attacks. These logs contain crucial information that can help us understand the nature of the attacks, identify the attackers, and uncover the vulnerabilities exploited. By scrutinizing these logs, we can gather actionable intelligence to strengthen our web application's security posture.

## Tasks

### 0. Attacker Service

**Objective:** Identify which service the attackers used to gain access to the system.

**File:** `0-service.sh`

This script analyzes the authentication logs to determine which service was used by attackers to gain access to the system. Based on the log analysis, it identifies and outputs the service name (e.g., "ssh").

### 1. Operation System

**Objective:** Determine the operating system version of the targeted system.

**File:** `1-operating.sh`

This script extracts the operating system version information from the system's dmesg log file, providing detailed information about the kernel version and OS distribution.

### 2. Account Compromised

**Objective:** Identify the name of the compromised user account.

**File:** `2-accounts.sh`

The script analyzes authentication logs to find accounts that show patterns of compromise, such as multiple failed login attempts followed by a successful login. It outputs the name of the compromised account (e.g., "root").

### 3. Sum Attack

**Objective:** Count the number of distinct attackers that gained access to the system.

**File:** `3-ips.sh`

This script counts unique IP addresses that successfully gained access to the system by analyzing successful login attempts in the authentication logs. Each IP address is considered a distinct attacker.

### 4. Mitigation Firewalls

**Objective:** Determine how many rules have been added to the firewall.

**File:** `4-firewall.sh`

The script examines logs for entries related to firewall rule additions, specifically looking for iptables rules added to the INPUT chain.

### 5. Users Accounts

**Objective:** Identify multiple accounts that were created on the target system.

**File:** `5-users.sh`

This script finds new user accounts created during the attack by looking for "useradd" entries in the authentication logs. It outputs a comma-separated list of usernames.

## Usage

Each script can be run directly from the command line:

```bash
./0-service.sh
./1-operating.sh
./2-accounts.sh
./3-ips.sh
./4-firewall.sh
./5-users.sh
```

The scripts expect the relevant log files to be in the current directory. For most scripts, this is `auth.log`, while the operating system detection script works with `dmesg`.

## Example Outputs

- Service detection: `ssh`
- OS Version: `Linux version 2.6.24-26-server (buildd@crested) (gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)) #1 SMP Tue Dec 1 18:26:43 UTC 2009 (Ubuntu 2.6.24-26.64-server)`
- Compromised account: `root`
- Number of attackers: `18`
- Number of firewall rules: `6`
- Created user accounts: `Aphelios,Debian-exim,Fido,Jax,Nidalee,Senna,dhg,messagebus,mysql,packet,sshd`

## Requirements

- Bash shell
- Common Unix tools (grep, awk, sort, uniq, etc.)
- Access to the relevant log files (auth.log, dmesg)
