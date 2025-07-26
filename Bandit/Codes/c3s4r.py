#!/usr/bin/env python3

def c3s4r(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Enter the text: ")
    
    while True:
        mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if mode in ['e', 'd']:
            break
        print("Please enter 'e' to encrypt or 'd' to decrypt.")
        
    while True:
        try:
            displacement = int(input("Enter the displacement number: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    if mode == 'd':
        displacement = -displacement

    result = c3s4r(text, displacement)
    print("Resulting text:", result)

if __name__ == "__main__":
    main()
