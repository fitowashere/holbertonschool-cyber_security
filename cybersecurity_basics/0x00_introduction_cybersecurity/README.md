# Cybersecurity Basics

## Description

This project serves as an introduction to cybersecurity fundamentals, focusing on system information retrieval and basic bash scripting. Through these exercises, you'll learn essential command-line tools and scripting techniques commonly used in cybersecurity.

## Project Structure

```
holbertonschool-cyber_security/
├── cybersecurity_basics/
│   └── 0x00_introduction_cybersecurity/
│       ├── 0-release.sh
│       ├── 1-gen_password.sh
│       ├── 2-sha256_validator.sh
│       ├── 3-ssh_keygen.sh
│       ├── 4-root_process.sh
│       └── README.md
```

## Tasks

0. System Distribution Information
    - File: 0-release.sh
    Write a bash script that displays the system's Distribution ID in a concise single-line output.
    Requirements:

    - Script must be exactly one line long (not counting the shebang line)
    - Must not use awk
    - Should use specific flags with lsb_release (-si or -is)
    - Output should display only the Distribution ID (e.g., "Kali")

### Example:
```
┌──(user㉿hbtn-lab)-[…/cybersecurity_basics/0x00_cybersecurity_basics]
└─$ ./0-release.sh
Kali
```
1. Password Generator
    - File: 1-gen_password.sh
    Create a Bash script that generates a strong random password.
    Requirements:

    - Script should be less than 3 lines long
    - Accept password length as an argument
    - Use /dev/urandom
    - Use [:alnum:] as character classes
    - Output may vary for each execution

### Example:
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./1-gen_password.sh 20
MkPpprPyC3i6navUB3Lj
```
2. SHA256 File Validator
    - File: 2-sha256_validator.sh
    Create a Bash script that validates the integrity of a file using SHA256.
    Requirements:

    - Script should be less than 3 lines long
    - Can use echo command
    - Should validate file integrity using SHA256 
    - Accept filename and hash as arguments

### Example:
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./2-sha256_validator.sh test_file e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
test_file: OK
```
3. RSA SSH Key Generator
    - File: 3-ssh_keygen.sh
    Create a Bash script that generates an RSA SSH key pair.
    ### Requirements:

    - Key size should be 4096 bits
    - Should use OpenSSH
    - Should accept key file path as an argument
    - Uses the -N "" flag for empty passphrase

### Example:
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./3-ssh_keygen.sh
Generating public/private rsa key pair...
Your identification has been saved in ~/.ssh/id_rsa
Your public key has been saved in ~/.ssh/id_rsa.pub
```

4. Process Monitor
    - File: 4-root_process.sh
    Create a Bash script that monitors all processes started by a specified user.
   ### Requirements:

    - Script should accept user as first argument
    - Must use ps aux command
    - Use grep -v to exclude processes with VSZ and RSS values of 0
    - Output may vary depending on active processes

### Example:
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./4-root_process.sh root
root           1  0.0  0.0  21172 12376 ?        Ss   07:38   0:01 /sbin/init splash
root         598  0.0  0.1  66380 19908 ?        Ss   07:39   0:00 /lib/systemd/systemd-journald
[...]
```

## Environment

- Kali Linux (Virtual Machine)
- Bash shell
- Git for version control
- OpenSSH

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/[your-username]/holbertonschool-cyber_security.git
    ```

2. Navigate to the project directory:
    ```
    cd holbertonschool-cyber_security/cybersecurity_basics/0x00_introduction_cybersecurity
    ```

3. Make scripts executable:
    ```
    chmod +x *.sh
    ```

## Resources

- Linux command line basics
- Bash scripting fundamentals
- System information retrieval commands
- Text processing in bash
- Understanding /dev/urandom and secure password generation
- Using tr command for character translation and deletion
- File integrity checking with SHA256
- Understanding cryptographic hash functions
- SSH key generation and management
- Public key cryptography basics
- Process monitoring and management in Linux
- Understanding Linux process states and attributes