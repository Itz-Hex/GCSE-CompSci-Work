import string

def encode_vigenere(plaintext, key):
    ciphertext = ""
    spaces = 0
    
    for i, char in enumerate(plaintext):
        if char == " ":
            ciphertext += " "
            spaces += 1
            continue
        i -= spaces
        key_value = key[i % len(key)] # for every character in the plaintext, get a letter from the key to match it
        print("KEY: " + key_value + str(i % len(key)) + " " +str(i))
        key_value = string.ascii_letters.index(key_value) # get that letter's position in the alphabet
        plaintext_char_index = string.ascii_letters.index(char)
        encrypted_char = string.ascii_letters[(plaintext_char_index + key_value) % 26]
        ciphertext += encrypted_char
        
    return ciphertext
