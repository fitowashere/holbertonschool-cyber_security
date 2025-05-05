#!/usr/bin/env ruby
require 'digest'

# Check if the correct number of arguments is provided
if ARGV.length != 2
  puts "Usage: #{File.basename(__FILE__)} HASHED_PASSWORD DICTIONARY_FILE"
  exit 1
end

# Get the hashed password and dictionary file path from command-line arguments
hashed_password = ARGV[0]
dictionary_file = ARGV[1]

# Check if the dictionary file exists
unless File.exist?(dictionary_file)
  puts "Error: Dictionary file not found: #{dictionary_file}"
  exit 1
end

# Function to hash a password using SHA-256
def hash_password(password)
  Digest::SHA256.hexdigest(password)
end

# Read the dictionary file and attempt to crack the password
password_found = false

File.foreach(dictionary_file) do |word|
  # Remove any trailing whitespace
  word = word.strip

  # Hash the word from the dictionary
  hashed_word = hash_password(word)

  # Compare with the target hashed password
  if hashed_word == hashed_password
    puts "Password found: #{word}"
    password_found = true
    break
  end
end

# If no matching password is found
puts "Password not found in dictionary." unless password_found
