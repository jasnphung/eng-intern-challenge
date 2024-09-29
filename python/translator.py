"""
Company: Shopify
Assessment: Eng Intern Challenge Fall - Winter 2025
Applicant: Jason Phung
Purpose: Translate English alphabet to Braille and vice versa, applicable for letters a through z, capital letters, numbers, and spaces
How to run: python translator.py "input_string"
"""

# Imports
import sys

# English alphabet to Braille mapping
alphabet_to_braille_map = {
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",

    '.': "..OO.O",
    ',': "..O...",
    '?': "..O.OO",
    '!': "..OOO.",
    '-': "....OO", 
    '/': ".O..O.",
    '<': ".O.O.O",
    # '>': "O..OO.",
    # '>' has been commented out due to it having the same braille as 'o',
    # both having "O..OO." (additionally, the requirements are for letters
    # a through z, capital letters, numbers, and spaces
    '(': "O.O..O",
    ')': ".O.OO.",
    
    ' ': "......"
}

# Numbers to Braille mapping
number_to_braille_map = {
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
}

# Braille to English alphabet mapping
braille_to_alphabet_map = {v: k for k, v in alphabet_to_braille_map.items()}

# Braille to English alphabet mapping
braille_to_number_map = {v: k for k, v in number_to_braille_map.items()}

# Function to check if the input is Braille
def is_braille(input_string):
    # Checks if the input string size is valid and if all characters in the string are braille only
    if (len(input_string) > 0 and len(input_string) % 6 != 0) or not(all(char in {'.', 'O'} for char in input_string)):
        return False
    
    return True

# Function to translate English alphabet to Braille
def translate_to_braille(input_string):
    # Resulting translated string
    result = ""

    # Flags for following numbers
    number_next = False

    for char in input_string:
        # Checks for capitalized letter
        if char.isupper():
            result += ".....O" + alphabet_to_braille_map[char.lower()]
            number_next = False
        # Checks for number, (adds number follows symbol)
        elif char.isdecimal() and not number_next:
            result += ".O.OOO" + number_to_braille_map[char]
            number_next = True
        # Checks for number (doesn't add number follows symbol)
        elif char.isdecimal() and number_next:
            result += number_to_braille_map[char]
        # Checks for space and resets number flag
        elif char == " ":
            result += alphabet_to_braille_map[char]
            number_next = False
        # Tries translation for any other symbol (e.g. lowercase letters)
        else:
            try:
                result += alphabet_to_braille_map[char]
            except KeyError:
                result += "??????"
    
    return result

# Function to translate Braille to English alphabet
def translate_to_alphabet(input_string):
    # Resulting translated string
    result = ""

    # Flags for following capitals and numbers
    capital_next = False
    number_next = False

    for i in range(0, len(input_string), 6):
        segment = input_string[i:i+6]

        # Checks for capital follows symbol
        if segment == ".....O":
            capital_next = True
            continue
        # Checks for number follows symbol
        elif segment == ".O.OOO":
            number_next = True
            continue
        # Checks for space
        elif segment == "......" and number_next:
            result += " "
            number_next = False
            continue

        # Refers to alphabet mapping and capitalizes it if the preceding segment was a capital follows symbol
        if capital_next:
            result += braille_to_alphabet_map[segment].upper()
            capital_next = False
            number_next = False
        # Refers to number mapping if there was a preceding number follows symbol
        elif number_next:
            result += braille_to_number_map[segment]
        # Refers to the alphabet mapping and tries to translate it
        else:
            try:
                result += braille_to_alphabet_map[segment]
                number_next = False
            except KeyError:
                result += "??????"

    return result

# Input translation and output from command line arguments
input_string = sys.argv[1]

if is_braille(input_string):
    print(translate_to_alphabet(input_string))
else:
    print(translate_to_braille(input_string))