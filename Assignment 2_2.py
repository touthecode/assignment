#The first step is to make sure all encrypted characters are part of the Alphabet
def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ' '
    return padded_key
#The second step is the core step when it comes to deciphering plaintext into ciphertext with both lower and uppercase separate
def _encrypt_char(plaintext_char, keyword_char):
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
        if plaintext_char.isupper():
            first_alphabet_letter = 'A'

        old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
        key_char_position = ord(keyword_char.lower()) - ord('a')
        new_char_position = (old_char_position + key_char_position) % 26
        return chr(new_char_position + ord(first_alphabet_letter))
    return plaintext_char

#This sets ciphertext to the product of the Vigenère Cipher from the message(plaintext) and key(keyword)
def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_char(plaintext_char, key_char)
    return ciphertext

#The final step inputs the variables from the input coming from the user
plaintext = input('Enter a message: ')
key = input('Enter a key: ')
ciphertext = encrypt(plaintext, key)
print(f'Ciphertext: {ciphertext}')