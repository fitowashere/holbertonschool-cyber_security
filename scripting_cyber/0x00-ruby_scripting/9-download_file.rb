#!/usr/bin/env ruby
require 'open-uri'
require 'uri'
require 'fileutils'

# Check if the correct number of arguments is provided
if ARGV.length != 2
  puts "Usage: #{File.basename(__FILE__)} URL LOCAL_FILE_PATH"
  exit 1
end

# Get the URL and local file path from command-line arguments
url = ARGV[0]
local_path = ARGV[1]

begin
  # Check if the URL is valid
  uri = URI.parse(url)

  # Create the directory path if it doesn't exist
  FileUtils.mkdir_p(File.dirname(local_path))

  puts "Downloading file from #{url}..."

  # Download the file and save it to the specified path
  URI.open(url) do |remote_file|
    File.open(local_path, 'wb') do |local_file|
      local_file.write(remote_file.read)
    end
  end

  puts "File downloaded and saved to #{local_path}."

rescue URI::InvalidURIError
  puts "Invalid URL: #{url}"
  exit 1
rescue OpenURI::HTTPError => e
  puts "HTTP Error: #{e.message}"
  exit 1
rescue => e
  puts "Error: #{e.message}"
  exit 1
end
