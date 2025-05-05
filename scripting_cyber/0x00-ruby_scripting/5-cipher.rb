#!/usr/bin/env ruby

# Class that implements Caesar cipher encryption and decryption
class CaesarCipher
    # Constructor that initializes the shift value
    def initialize(shift)
      @shift = shift
    end

    # Method to encrypt a message using Caesar cipher
    def encrypt(message)
      cipher(message, @shift)
    end

    # Method to decrypt a message using Caesar cipher
    def decrypt(message)
      cipher(message, -@shift)
    end

    private

    # Helper method that performs the actual cipher operation
    # Can only be called from within the same instance
    def cipher(message, shift)
      result = ""

      message.each_char do |char|
        if char.match(/[a-zA-Z]/)
          # Determine if the character is uppercase or lowercase
          is_upper = char.match(/[A-Z]/)
          # Get the base ASCII value (65 for 'A', 97 for 'a')
          base = is_upper ? 65 : 97
          # Apply Caesar cipher formula and convert back to character
          offset = (char.ord - base + shift) % 26
          result += (base + offset).chr
        else
          # For non-alphabetic characters, keep them unchanged
          result += char
        end
      end

      result
    end
end
