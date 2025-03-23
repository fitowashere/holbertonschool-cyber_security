# IDOR Vulnerabilities in Web Applications - CyberBank Case Study

## Project Overview

This project demonstrates the exploitation of Insecure Direct Object References (IDOR) vulnerabilities in a simulated banking application called CyberBank. IDOR vulnerabilities occur when an application exposes internal implementation objects, such as database IDs, without proper authorization checks, allowing attackers to access unauthorized data or perform unauthorized actions.

## Repository Structure

- `web_application_security/0x06_idor/`
  - `0-flag.txt`: Flag from uncovering user IDs
  - `1-flag.txt`: Flag from enumerating account numbers and accessing balances
  - `2-flag.txt`: Flag from manipulating wire transfers

## Challenge Progression

### Task 0: Uncovering User IDs

**Objective**: Discover other users' IDs within the CyberBank application.

**Approach**:
1. Log into CyberBank and explore the dashboard
2. Analyze URL structures, page content, and API requests
3. Identify patterns in how user IDs are displayed or transmitted
4. Experiment with altering user ID values to access other users' information

### Task 1: Enumerating Account Numbers

**Objective**: Leverage discovered user IDs to enumerate account numbers and access account balances.

**Approach**:
1. Use discovered user IDs to explore account-related features
2. Identify the relationship between user IDs and account numbers
3. Craft requests to the `/accounts/` API endpoint
4. Modify account number parameters to access unauthorized account information

### Task 2: Manipulating Wire Transfers

**Objective**: Exploit wire transfer functionality to inflate account balance above $10,000.

**Approach**:
1. Analyze the wire transfer feature and its parameters
2. Test various parameter manipulations:
   - Source account modification
   - Negative amount transfers
   - Transaction processing logic flaws
   - Race conditions
3. Systematically exploit vulnerabilities to increase account balance
4. Capture the flag when balance exceeds $10,000

## Security Implications

The vulnerabilities demonstrated in this project highlight critical security flaws that could lead to:
- Unauthorized access to user information
- Account balance disclosure
- Financial fraud through transaction manipulation

## Ethical Considerations

This project was conducted in a controlled, simulated environment for educational purposes only. Applying these techniques to real-world applications without authorization is illegal and unethical.

## Mitigation Strategies

To prevent IDOR vulnerabilities:
1. Implement proper authorization checks for all object references
2. Use indirect reference maps instead of exposing internal objects directly
3. Validate user permissions for every request
4. Employ secure session management
5. Implement proper input validation and output encoding

## Tools Used

- Web browser developer tools
- HTTP request manipulation techniques
- API testing methodologies