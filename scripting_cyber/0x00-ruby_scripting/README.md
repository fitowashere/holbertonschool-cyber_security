# Ruby Scripting for Cybersecurity

This repository contains a collection of Ruby scripts for cybersecurity tasks and basic Ruby programming concepts. These scripts demonstrate fundamental Ruby skills and practical applications related to cybersecurity.

## General Requirements

* All scripts are tested on Kali Linux
* Editors allowed: vi, vim, emacs
* All files must:
  * Begin with the shebang line `#!/usr/bin/env ruby`
  * End with a new line
  * Be executable
* Code should follow the Betty style
* IP ranges should be substituted for `$1` without quotes
* No use of backticks, `&&`, `||`, or `;` is allowed

## Tasks

### 0. Hello World with Function
**File:** `0-hello_world_function.rb`

This task requires creating a Ruby script that defines a function named `say_hello` that accepts one string argument and prints "Hello, Holberton! from" followed by the string.

The function prototype is `say_hello(str)` and it should print the message to standard output.

### 1. Hello World with Class
**File:** `1-hello_world_class.rb`

This task requires creating a Ruby script that defines a `HelloWorld` class with:
* An initialize method that sets an instance variable called `message` holding the string "Hello, World!"
* A method called `print_hello` that displays the message

### 2. Prime Number Checker
**File:** `2-prime.rb`

This task involves writing a function that checks if a given number is prime. The function should:
* Be named `prime(number)`
* Use the built-in Ruby `Prime` class
* Return `true` if the number is prime and `false` otherwise

### 3. Reading from a File
**File:** `3-read_file.rb`

This task requires creating a function that reads content from a JSON file and counts the occurrences of each `userId`. The function:
* Should be named `count_user_ids(path)`
* Takes a file path as input
* Reads the JSON data from the file
* Counts how many times each userId appears
* Prints each userId followed by its count in ascending order

### 4. Writing to a File
**File:** `4-write_file.rb`

This task involves creating a function that merges JSON objects from one file into another. The function:
* Should be named `merge_json_files(file1_path, file2_path)`
* Takes two file paths as input
* Reads JSON data from both files
* Combines the data
* Writes the merged result back to the second file

### 5. Caesar Cipher
**File:** `5-cipher.rb`

This task requires implementing a `CaesarCipher` class for encryption and decryption of messages using the Caesar cipher technique. The class should have:
* An `initialize(shift)` constructor that sets the shift value
* An `encrypt(message)` method that returns the encrypted message
* A `decrypt(message)` method that returns the decrypted message
* A private `cipher(message, shift)` method that performs the actual encryption/decryption

### 6. Simple HTTP Request
**File:** `6-get.rb`

This task involves creating a function that performs an HTTP GET request and formats the response. The function:
* Should be named `get_request(url)`
* Takes a URL as input
* Makes an HTTP GET request to the specified URL
* Prints the response status code and body in a formatted way
* Should handle JSON responses appropriately

### 7. Command-Line Arguments
**File:** `7-args.rb`

This task requires creating a function that prints each command-line argument. The function:
* Should be named `print_arguments`
* If no arguments are provided, prints "No arguments provided."
* Otherwise, prints each argument with its index number

### 8. HTTP POST Request
**File:** `8-post.rb`

This task involves creating a function that makes an HTTP POST request with JSON body parameters. The function:
* Should be named `post_request(url, body_params)`
* Takes a URL and body parameters as input
* Makes an HTTP POST request to the specified URL with the provided parameters
* Prints the response status code and body in a formatted way

### 9. Downloading a File
**File:** `9-download_file.rb`

This task requires creating a script that downloads a file from a given URL and saves it locally. The script:
* Takes two command-line arguments: URL and local file path
* Downloads the file from the URL
* Saves it to the specified local path
* Provides appropriate error handling
* Displays usage information if incorrect arguments are provided

### 10. Password Cracker
**File:** `10-password_cracked.rb`

This task involves creating a script that performs a dictionary attack to crack a hashed password. The script:
* Takes two command-line arguments: a hashed password and a dictionary file path
* Reads words from the dictionary file
* Hashes each word using SHA-256
* Compares the hashes to the target hashed password
* Prints "Password found: [word]" if a match is found
* Prints "Password not found in dictionary." if no match is found

### 11. Basic CLI Application
**File:** `11-cli.rb`

This task requires creating a command-line interface (CLI) application using the `optparse` library. The application:
* Manages a list of tasks stored in a text file
* Provides options to add, list, and remove tasks
* Has a help option to display usage information
* Supports the following commands:
  * `-a, --add TASK`: Adds a new task
  * `-l, --list`: Lists all tasks
  * `-r, --remove INDEX`: Removes a task by index
  * `-h, --help`: Shows help information

## Repository Structure

* GitHub repository: `holbertonschool-cyber_security`
* Directory: `scripting_cyber/0x00-ruby_scripting`
* Files:
  * `0-hello_world_function.rb`
  * `1-hello_world_class.rb`
  * `2-prime.rb`
  * `3-read_file.rb`
  * `4-write_file.rb`
  * `5-cipher.rb`
  * `6-get.rb`
  * `7-args.rb`
  * `8-post.rb`
  * `9-download_file.rb`
  * `10-password_cracked.rb`
  * `11-cli.rb`
