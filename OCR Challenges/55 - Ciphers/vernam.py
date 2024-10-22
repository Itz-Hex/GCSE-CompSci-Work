import string

def to_binary(num):
    return '{0:05b}'.format(num)

def encode_vernam(plaintext, key):
    if len(plaintext) != len(key): # ensure plaintext and key are of equal length
        return "Plaintext and key must be of equal length."
    if " " in plaintext:
        return "Plaintext must not contain whitespaces."
    
    cipher_text = ""
    
    for i in range(len(plaintext)): # loop through each character in the plaintext/key
        plain_char = plaintext[i] # get plaintext char
        key_char = key[i] # get key char
        
        plain_char_index = string.ascii_letters.index(plain_char) + 1 # get the aphabetical index of the plain char
        key_char_index = string.ascii_letters.index(key_char) + 1 # get the alphabetical index of the key char
                
        plain_binary = to_binary(plain_char_index) # convert index to binary
        key_binary = to_binary(key_char_index) # convert index to binary
        
        result_binary = ""
        
        for i in range(5): # binary numbers will always be 5 long
            result_binary += str(int(bool(int(plain_binary[i])) != bool(int(key_binary[i])))) # perform XOR on each binary digit
            
        result_index = 0
        
        # convert result_binary to an integer
        for i,n in enumerate(result_binary):
            x = 16
            for _ in range(i):
                x /= 2
            result_index += int(n) * int(x)
            
        result_index = result_index % 25
        
        result_char = string.ascii_letters[result_index]
            
        cipher_text += result_char
        
    return cipher_text
    
print(encode_vernam("oak", "son"))

### TODO: Just getting 00000 as output, so the XOR logic isn't working for some reason. Fix this.