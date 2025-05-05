#!/usr/bin/env ruby
require 'json'

# Function that reads content from a JSON file and counts the userId
def count_user_ids(path)
  # Read the file
  file_content = File.read(path)

  # Parse JSON
  data = JSON.parse(file_content)

  # Initialize a hash to store userId counts
  user_counts = Hash.new(0)

  # Count the occurrences of each userId
  data.each do |item|
    user_id = item["userId"]
    user_counts[user_id] += 1
  end

  # Print the counts
  user_counts.sort.each do |id, count|
    puts "#{id}: #{count}"
  end
end
