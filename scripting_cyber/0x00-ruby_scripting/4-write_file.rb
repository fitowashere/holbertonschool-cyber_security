#!/usr/bin/env ruby
require 'json'

# Function that merges JSON objects from one file into another
def merge_json_files(file1_path, file2_path)
  # Read and parse the first file
  file1_content = File.read(file1_path)
  data1 = JSON.parse(file1_content)

  # Read and parse the second file
  file2_content = File.read(file2_path)
  data2 = JSON.parse(file2_content)

  # Merge the data from file1 into file2
  merged_data = data2 + data1

  # Write the merged data back to file2
  File.write(file2_path, JSON.pretty_generate(merged_data))

  # Print the expected message
  puts "Merged JSON written to #{file2_path}"
end
