hi# Web Application Security - Module 0x00

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