from crypto_functions import *

the_menu = {'E':'Encrypt a message', 'D':'Decrypt a message',
            'S':'Save encryption to file', 'R':'Retrieve decryption from file',
            'Q':'Quit this program'}

the_cipher_menu = {'T':'Scytale Cipher', 'V':'Vigenere Cipher'}

opt = None

while True:
    print_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu: # check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q': # quit the program
        print("Goodbye!")
        break # exit the main `while` loop

    if opt == 'E':# Encrypt a message
        print("::: Which cipher to use?")
        print_menu(the_cipher_menu)
        cipher = input("> ").upper()
        if cipher == 'T':
            message = input('::: Message > ') # get the input as a string
            nColumns = input('::: Key > ') # get the input as a string
            # if the string is not a valid integer, output a warning
            if nColumns.isdigit() == False:
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue # back to the main menu
            elif nColumns[0] ==0:
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue
            elif int(nColumns) <= 0:
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue
            else:
                nColumns = int(nColumns)
                # Call the function `encrypt_transposition` to encrypt the message
                result = encrypt_transposition(message, nColumns)
                # Print the message after obtaining the encrypted result
                print(f"Encryption using the {the_cipher_menu[cipher]}:") 
                print(result)
        elif cipher == 'V':
            message = input('::: Message > ') # TODO: get the input as a string
            secret = input('::: Secret > ') # TODO: get the input as a string
            validity = None
            # validate the input of message: if the character of message is not in the alphabet, output a warning and return to the menu
            for char in message:
                if char not in get_alphabet_vigenere():
                    print(f"WARNING: '{message}' contains invalid character '{char}' that is out of the alphabet and digits.\n")
                    validity = False
                    break
            if validity == False:
                continue
            
            # validate the input of secret: if the character of secret is not in the alphabet, output a warning and return to the menu
            for char in secret:
                if char not in get_alphabet_vigenere():
                    print(f"WARNING: '{secret}' contains invalid character '{char}' that is out of the alphabet and digits.\n")
                    validity = False
                    break
            if validity == False:
                continue
            # if the secret is not a valid string, output a warning
            if secret == '':
                print(f"WARNING: '{secret}' is an invalid secret.\n")
                continue
            else:
                # Call the function `encrypt_vigenere` to encrypt the message
                result = encrypt_vigenere(message, secret)
                # Print the message after obtaining the encrypted result
                print(f"Encryption using the {the_cipher_menu[cipher]}:") 
                print(result)
        else:
            print(f"WARNING: {opt} is an invalid cipher.\n")
            continue # back to the main menu

    if opt == 'D':# decrypt a message
        print("::: Which cipher to use?")
        print_menu(the_cipher_menu)
        cipher = input("> ").upper()
        if cipher == 'T':
            message = input('::: Ciphertext > ') # get the input as a string
            nColumns = input('::: Key > ') # get the input as a string
            if nColumns.isdigit() == False:
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue # back to the main menu
            elif nColumns[0] == 0:
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue
            elif int(nColumns) <= 0:
                print(f"WARNING: '{nColumns}' is an invalid integer.\n")
                continue
            else:
                nColumns = int(nColumns)
                # Call the function `decrypt_transposition` to decrypt the message
                result = decrypt_transposition(message, nColumns)
                # Print the message after obtaining the decrypted result
                print(f"Decrypted message using the {the_cipher_menu[cipher]}:") 
                print(result)
        elif cipher == 'V':
            message = input('::: Ciphertext > ') # get the input as a string
            secret = input('::: Secret > ') # get the input as a string
            # if the secret is not a valid string, output a warning
            if secret == '':
                print(f"WARNING: '{secret}' is an invalid secret.\n")
                continue
            # the message and secret is out of alphabet, output a warning
            elif decrypt_vigenere(message, secret) == -1:
                print(f"WARNING: '{message}' or '{secret}' contains a character that is out of alphabet.\n")
                continue
            else:
                # Call the function `encrypt_vigenere` to encrypt the message
                result = decrypt_vigenere(message, secret)
                # Print the message after obtaining the encrypted result
                print(f"Decrypted message using the {the_cipher_menu[cipher]}:") 
                print(result)
        else:
            print(f"WARNING: {opt} is an invalid cipher.\n")
            continue # back to the main menu
        
    # Pause before going back to the main menu
    input("::: Press Enter to return to main menu")

# the message to display before quitting the program
print("Your secrets are safe with me.")













