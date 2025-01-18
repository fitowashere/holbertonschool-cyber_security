#!/bin/bash

# Get the first argument passed to the script
password="$1"

# Remove the {xor} prefix from the string
password="${password#'{xor}'}"

# Decode the Base64 encoded string
decoded_password=$(echo -n "$password" | openssl enc -base64 -d)

# Initialize variable to store XOR operation result
output=""

# Loop through each character of the string
for ((i = 0; i < ${#decoded_password}; i++)); do
    # Get character at current position
    char="${decoded_password:$i:1}"
    
    # Convert character to ASCII code and perform XOR with 95
    xor_result=$(( $(printf "%d" "'$char") ^ 95 ))
    
    # Add result to output variable
    output+=$(printf "\\$(printf '%03o' $xor_result)")
done

# Display the result
echo "$output"
