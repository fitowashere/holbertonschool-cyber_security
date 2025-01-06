# Web Application Security - Module 0x00

## Project Overview

This module focuses on exploiting four types of vulnerabilities commonly found in web applications. We'll be working with a customer support dashboard that was rapidly developed using AI assistance, making it an interesting target for security testing.

### Background Story

A developer created a customer support dashboard in just 3 days using ChatGPT 4, claiming it to be "hack proof". This project will guide you through testing that claim by exploring various security vulnerabilities.

## Prerequisites

Before starting this project, ensure you have:

- Kali Linux installed (or access to a security testing sandbox)
- Network access (via OpenVPN or sandbox environment)
- Firefox web browser (recommended)
- Terminal access with `curl` and `sqlmap` installed

## Environment Setup

### Target Information
- Target Endpoint: `http://web0x00.hbtn/login`
- Target IP: `10.42.153.177`

### Configuring Local Environment

1. Add the target domain to your hosts file:
```bash
# Open hosts file
sudo nano /etc/hosts

# Add the following line
10.42.153.177    web0x00.hbtn

# Alternative one-liner
echo "10.42.153.177    web0x00.hbtn" | sudo tee -a /etc/hosts
```

2. Verify your setup:
```bash
# Check hosts file entry
cat /etc/hosts | grep web0x00

# Test DNS resolution
ping web0x00.hbtn -c 4

# Test HTTP connectivity
curl http://web0x00.hbtn
```

### Troubleshooting Connectivity

If you encounter connection issues:

1. Verify VPN connection if required
2. Check target IP reachability:
```bash
ping 10.42.153.177
```

3. Try connecting directly to IP:
```bash
curl http://10.42.153.177
```

4. Check for services on common ports:
```bash
nmap -p 80,443,8080,8000 10.42.153.177
```

## Expected Server Response

When properly configured, you should receive a redirect response from the server:
```html
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/home">/home</a>. If not, click the link.
```

## Vulnerabilities and Exploits

### 1. Host Header Injection

The first vulnerability we'll explore is Host Header Injection. This security flaw occurs when a web application implicitly trusts the HTTP Host header without proper validation. Understanding this vulnerability is crucial as it can lead to serious security implications including phishing attacks and security control bypasses.

#### The Host Header's Role
When you browse the internet, every HTTP request includes a Host header that tells web servers which domain you're trying to reach. This header is essential for virtual hosting, where multiple websites share the same IP address. Under normal circumstances, your browser automatically sets this header to match the domain name you typed in the address bar.

#### The Vulnerability Explained
Our target application has a vulnerability in its password reset functionality. When generating the "Try to sign in again" link in the reset password page, the application directly uses the value from the Host header without validation. This trust in user-controllable input creates a security hole that we can exploit.

#### Exploit Script
We've created a simple but effective exploit script (`1-host_header_injection.sh`):
```bash
#!/bin/bash
curl -X POST "$2" -H "HOST: $1" -d "$3"
```

Script components:
- First argument (`$1`): The malicious host we want to inject
- Second argument (`$2`): Target URL (http://web0x00.hbtn/reset_password)
- Third argument (`$3`): Form data (e.g., email=test@test.hbtn)

Usage example:
```bash
./1-host_header_injection.sh new_host http://web0x00.hbtn/reset_password "email=test@test.hbtn"
```

#### Security Impact
This vulnerability can be exploited for:
- Phishing attacks by redirecting users to malicious domains
- Bypassing security controls that rely on domain validation
- Session hijacking in certain configurations
- Web cache poisoning attacks

#### Secure Implementation
A properly secured application should:
- Validate the Host header against a whitelist of allowed domains
- Not use user-controllable input for generating critical application links
- Implement strict header parsing and validation
- Use absolute URLs instead of relative ones for critical functionalities

## Project Structure

The exercises will guide you through:
1. Initial reconnaissance
2. Identifying vulnerabilities
3. Exploiting discovered vulnerabilities
4. Documentation of findings

## Repository Information

- GitHub repository: `holbertonschool-cyber_security`
- Directory: `web_application_security/0x00_web_fundamentals`
- Main documentation: `README.md`

## Note

This is a controlled testing environment. All security testing should be performed only on the provided target within the lab environment. Do not attempt to use these techniques on systems without explicit permission.