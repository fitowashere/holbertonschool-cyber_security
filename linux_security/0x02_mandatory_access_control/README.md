# Mandatory Access Control in Linux

This repository contains scripts for working with Mandatory Access Control (MAC) systems in Linux, specifically SELinux and AppArmor. These scripts demonstrate various security configurations and management tasks.

## Project Description

Mandatory Access Control is a security approach where access to resources is governed by security policies that users cannot modify. In Linux, SELinux and AppArmor are the two most common MAC implementations. This project provides scripts to interact with these security frameworks, manage their configurations, and understand their features.

## Scripts

### 0. SELinux Mode Analysis
- **File**: `0-analyse_mode.sh`
- **Description**: Displays the current SELinux mode (enforcing, permissive, or disabled).

### 1. AppArmor Status
- **File**: `1-security_match.sh`
- **Description**: Displays the status of AppArmor security profiles on the system.

### 2. SELinux HTTP Ports
- **File**: `2-list_http.sh`
- **Description**: Lists all ports managed by SELinux that are related to HTTP services.

### 3. Adding SELinux HTTP Port
- **File**: `3-add_port.sh`
- **Description**: Adds TCP port 81 to the http_port_t SELinux type.

### 4. SELinux User Mappings
- **File**: `4-list_user.sh`
- **Description**: Lists all SELinux user mappings.

### 5. Adding SELinux User Mapping
- **File**: `5-add_selinux.sh`
- **Description**: Adds a new login mapping in SELinux, linking a Linux login name with the SELinux user identity `user_u`.

### 6. SELinux Booleans
- **File**: `6-list_booleans.sh`
- **Description**: Lists all SELinux booleans defined on the system.

### 7. SELinux Email Permission
- **File**: `7-set_sendmail.sh`
- **Description**: Sets the SELinux boolean `httpd_can_sendmail` to `on` permanently.

## Requirements

- All scripts are exactly 2 lines long
- All scripts start with `#!/bin/bash`
- All scripts end with a new line
- Scripts must be run with sudo

## Usage

To run any script:

```bash
chmod +x script_name.sh
sudo ./script_name.sh
```

For script 5 (adding a SELinux user mapping), provide a username as an argument:

```bash
sudo ./5-add_selinux.sh username
```

## Notes on MAC Systems

### SELinux
SELinux (Security-Enhanced Linux) is a MAC system that defines policies to control access to files, processes, and other system resources. It's integrated into the Linux kernel and commonly used in Red Hat-based distributions.

### AppArmor
AppArmor is another MAC system that restricts programs' capabilities with per-program profiles. It's path-based rather than label-based (like SELinux) and is commonly used in Ubuntu and other Debian-based distributions.