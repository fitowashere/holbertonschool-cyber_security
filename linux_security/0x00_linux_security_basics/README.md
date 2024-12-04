# Linux Security Basics

## Description
This project focuses on fundamental Linux security concepts and practices. Through various scripts and exercises, we explore different aspects of system security, user management, and access monitoring.

## Project Structure
```
holbertonschool-cyber_security/
└── linux_security/
    └── 0x00_linux_security_basics/
        ├── 0-login.sh
        └── README.md
```

## Tasks

### 0. What secrets hold
A script that displays the last 5 login sessions for users with their corresponding dates.

#### Script: `0-login.sh`
- **Usage**: `sudo ./0-login.sh`
- **Features**:
  - Displays the last 5 login sessions
  - Shows full timestamps
  - Requires root privileges
- **Output Example**:
  ```
  root     tty1         Thu Oct 12 10:08:24 2023   still logged in
  root     ttyS0        Thu Oct 12 10:08:23 2023   still logged in
  reboot   system boot  Thu Oct 12 10:08:10 2023   still running
  root     tty1         Tue Oct 10 15:08:21 2023 - down   (19:26)
  root     ttyS0        Tue Oct 10 15:08:21 2023 - down   (19:26)
  ```

## Requirements
- Linux operating system
- Root or sudo privileges
- Bash shell

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/[username]/holbertonschool-cyber_security.git
   ```
2. Navigate to the project directory:
   ```bash
   cd holbertonschool-cyber_security/linux_security/0x00_linux_security_basics
   ```
3. Make the script executable:
   ```bash
   chmod +x 0-login.sh
   ```

## Usage
Run the script with sudo privileges:
```bash
sudo ./0-login.sh
```
