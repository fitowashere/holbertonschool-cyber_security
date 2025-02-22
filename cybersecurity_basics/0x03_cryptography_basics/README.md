# Cryptography Basics

This project contains various scripts for working with cryptographic hashes and password cracking tools.

## Project Structure

* Directory: `cybersecurity_basics/0x03_cryptography_basics`
* GitHub repository: `holbertonschool-cyber_security`

## Tasks

### 0. SHA1
* File: `0-sha1.sh`
* Description: Script that hashes a password using SHA-1 algorithm
* Usage: `./0-sha1.sh "password"`
* Output is stored in `0_hash.txt`

### 1. SHA256
* File: `1-sha256.sh`
* Description: Script that hashes a password using SHA-256 algorithm
* Usage: `./1-sha256.sh "password"`
* Output is stored in `1_hash.txt`

### 2. MD5
* File: `2-md5.sh`
* Description: Script that hashes a password using MD5 algorithm
* Usage: `./2-md5.sh "password"`
* Output is stored in `2_hash.txt`

### 3. Secure Password Hash
* File: `3-password_hash.sh`
* Description: Script that combines a password with a random 16-character value and generates SHA-512 hash using OpenSSL
* Usage: `./3-password_hash.sh "password"`
* Output is stored in `3_hash.txt`

### 4. Wordlist Mode
* Files: `4-wordlist_john.sh, 4-password.txt`
* Description: Script that uses John the Ripper with RockYou wordlist to crack passwords
* Usage: `./4-wordlist_john.sh hash.txt`
* Cracked passwords are stored in `4-password.txt`

### 5. Windows Authentication Cracking
* Files: `5-windows_john.sh, 5-password.txt`
* Description: Script that cracks Windows NT hashes using John the Ripper
* Usage: `./5-windows_john.sh hash.txt`
* Cracked password is stored in `5-password.txt`

### 6. John Cracking
* Files: `6-crack_john.sh, 6-password.txt`
* Description: Script that cracks SHA-256 hashes using John the Ripper
* Usage: `./6-crack_john.sh crack.txt`
* Cracked password is stored in `6-password.txt`

### 7. Hashcat Straight Attack
* Files: `7-crack_hashcat.sh, 7-password.txt`
* Description: Script that cracks passwords using Hashcat in straight attack mode
* Usage: `./7-crack_hashcat.sh hash.txt`
* Cracked password is stored in `7-password.txt`

### 8. Hashcat Combination
* File: `8-combination_hashcat.sh`
* Description: Script that combines two wordlists
* Usage: `./8-combination_hashcat.sh wordlist1.txt wordlist2.txt`
* Outputs combined wordlist to stdout

### 9. Hashcat Combination Attack
* Files: `9-attack_hashcat.sh, 9-password.txt`
* Description: Script that uses Hashcat's combination attack mode with two wordlists
* Usage: `./9-attack_hashcat.sh hash.txt`
* Cracked password is stored in `9-password.txt`

## Requirements

* All scripts must be exactly 2 lines long
* Scripts must be executable
* Following tools need to be installed:
  * John the Ripper
  * Hashcat
  * OpenSSL
* RockYou wordlist should be available at `/usr/share/wordlists/rockyou.txt`

