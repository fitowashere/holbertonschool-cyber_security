#!/usr/bin/env ruby

# Function that prints each command-line argument
def print_arguments
    # Check if any arguments were provided
    if ARGV.empty?
      puts "No arguments provided."
    else
      # Print each argument with its index
      ARGV.each_with_index do |arg, index|
        puts "#{index + 1}. #{arg}"
      end
    end
end
