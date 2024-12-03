# Cybersecurity Basics

## Description

This project serves as an introduction to cybersecurity fundamentals, focusing on system information retrieval and basic bash scripting. Through these exercises, you'll learn essential command-line tools and scripting techniques commonly used in cybersecurity.

## Project Structure

```holbertonschool-cyber_security/
├── cybersecurity_basics/
│   └── 0x00_introduction_cybersecurity/
│       ├── 0-release.sh
│       └── README.md
```

## Tasks

0. System Distribution Information
    - File: 0-release.sh
    Write a bash script that displays the system's Distribution ID in a concise single-line output.
    Requirements:

    - Script must be exactly one line long (not counting the shebang line)
    Must not use awk
    Output should display only the Distribution ID (e.g., "Kali")

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
    Accept password length as an argument
    Use /dev/urandom
    Use [:alnum:] as character classes
    Output may vary for each execution

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
    Can use echo command
    Should validate file integrity using SHA256 hash

### Example:
```
┌──(yosri㉿hbtn-lab)-[…/cybersecurity_basics/0x00_introduction_cybersecurity]
└─$ ./2-sha256_validator.sh test_file e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
test_file: OK
```
## Environment

- Kali Linux (Virtual Machine)
- Bash shell
- Git for version control

## Setup Instructions

1. Clone the repository:

    - git clone https://github.com/[your-username]/holbertonschool-cyber_security.git

2. Navigate to the project directory:

    - cd holbertonschool-cyber_security/cybersecurity_basics/0x00_introduction_cybersecurity

3. Make scripts executable:

    - chmod +x *.sh

## Testing SHA256 Validator

### To test the SHA256 validator:

1. Create a test file:

    - echo "Hello World" > test_file

2. Generate SHA256 hash:

    - sha256sum test_file

3. Validate the file:

    - ./2-sha256_validator.sh test_file <generated_hash>