import string

def alphabet_position(letter):
    #receives a letter
    #make value passed a lowercase value
    low_letter = letter.lower()
    pos = string.ascii_lowercase.index(low_letter)
    #and returns the 0-based numerical position of that letter within the alphabet
    return(pos)


def rotate_character(char, rot):
    #get index value, then add rotation number
    old_value = alphabet_position(char)
    #append new value
    new_value = (old_value + rot) % 26

    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    #make new index value back into character
    if char in string.ascii_uppercase:
        new_char = upper[new_value]
    else:
        new_char = lower[new_value]

    return(new_char)

def encrypt(text, rot):
    message = ""
    for char in text:
        if char not in string.ascii_letters:
            message = message + char
        else:
            encrypted = rotate_character(char, rot)
            message = message + encrypted
    return(message)
