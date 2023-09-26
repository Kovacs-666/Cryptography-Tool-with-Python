def print_menu(dictionary):
    """
    The print takes in a dictionary that stores menu and the function will print the menu.
    """
    print(f'==========================')
    for key, value in dictionary.items():
        print(f'{key} = {value}')
    print(f'==========================')
    

def create_matrix(row_length, column_length):
    """
    The function expects two integers `row_length` and `column_length`
    as input and returns a matrix of dimension `row_length` x `column_length` 
    which contains space characters(`' '`)
    """
    outter_list = []
    for i in range(row_length):
        inner_list = []
        for j in range(column_length):
            inner_list.append(' ')
        outter_list.append(inner_list)
    return outter_list

def encode_to_matrix(message_string, column_length):
    """
    The function takes a string `message_string` and an integer
    `column_length` as integer and "writes" the message string
    on to a matrix that has `column_length` many columns.
    """
    if len(message_string)%column_length != 0:
        num_rows = int(len(message_string)/column_length)+1
    elif len(message_string)%column_length == 0:
        num_rows = int(len(message_string)/column_length)

    new_list = create_matrix(num_rows, column_length)

    k = 0
    for i in range(num_rows):
        for j in range(column_length):
            new_list[i][j] = message_string[k]
            k += 1
            if k == len(message_string):
                break
        if k == len(message_string):
            break
    return new_list

def encrypt_transposition(message, nColumns):
    """
    The function has two parameters: 'message' and 'nColumns'. For message,
    an string of plaintext is expected as the argument. nColumns parameter
    expects an integer which will be the key for encryption The function will return
    the encrypted message using Scytale Cipher.
    """

    #Get the dimension for the matrix

    message_len = len(message)
    nRows = 0
    if message_len % nColumns != 0:
        nRows = int(message_len / nColumns) + 1
    elif message_len % nColumns == 0:
        nRows = int(message_len / nColumns)

    #Create the empty matrix by calling create_matrix(row_length, column_length) function

    empty_matrix = create_matrix(nRows, nColumns)

    #Filling the message into the empty_matrix using function encode_to_matrix(message_string, column_length)

    empty_matrix = encode_to_matrix(message, nColumns)

    #Reading the processed empty_list to return encrypted message

    encrypted_message = ''
    for column_num in range(nColumns):
        for row_num in range(nRows):
            encrypted_message += empty_matrix[row_num][column_num]

    return encrypted_message
    
    
def decrypt_transposition(message, nColumns):
    """
    The function has two parameters: 'message' and 'nColumns'. For message,
    an string of encrypted message using Scytale Cipher is expected as the argument.
    nColumns parameter expects an integer which will be the key for decryption. The
    function will return the decrypted message.
    """

    #Get the dimension for the matrix

    message_len = len(message)
    nRows = int(message_len / nColumns)

    #Create the empty matrix by calling create_matrix(row_length, column_length) function

    empty_matrix = create_matrix(nRows, nColumns)

    #Fill the empty_matrix with the encrypted message

    count = 0
    for column_num in range(nColumns):
        for row_num in range(nRows):
            if count < message_len:
                empty_matrix[row_num][column_num] = message[count]
                count += 1
            elif count >= message_len:
                break

        if count >= message_len:
            break

    #Reading the processed empty_matrix in the correct order and concatenate each character into a new decrypted string.

    decrypted_message = '' 
    for row_num in range(nRows):
        for column_num in range(nColumns):
            decrypted_message += empty_matrix[row_num][column_num]

    #Remove the trailing whitespace and return the decrypted message

    while decrypted_message.endswith(' ') == True:
        decrypted_message = decrypted_message[0:-1]

    return decrypted_message

def extend_string(key_string, new_length):
    """
    The function takes a string parameter `key_string` and
    an integer parameter `new_length` and creates a new string
    that is formed by repeating key_string multiple times to
    match the length `new_length`.
    """
    reptime = new_length // len(key_string)
    extrastr = new_length % len(key_string)
    extend_str = f'{key_string * reptime}{key_string[0:extrastr]}'
    return extend_str

def extend_vigenere(message, secret):
    """
    The function takes in two string parameters: message and secret. For message,
    a plaintext message is expected. For secret, a key string is expected. Function will
    return a new secret string that will be used to encrypt or decrypt the message using
    Vigenère cipher which the length matches the length of the message
    """
    message_length = len(message)
    new_secret = ''
    # Using function extend_string(key_string, new_length) to get the new secret string
    new_secret = extend_string(secret, message_length)
    return new_secret

def get_alphabet_vigenere():
    """
    The function expects no parameters. It will return the string containing the alphabet,
    which is: uppercase English letters followed by 0123456789, followed by lowercase English letters.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    return alphabet

def encrypt_vigenere(message, secret):
    """
    The function takes in two string parameters. The message parameter expects a plaintext
    message that need to be encrypted. The secret expect a key string used to encrypt the message.
    The function retruns an encrypted message
    """
    alphabet = get_alphabet_vigenere()
    key = extend_vigenere(message, secret)
    encrypted_message = ''
    final_letter = ''
    count = 0
    for char in message:
        if char in alphabet:
            #find sum of the index of each letter and its key letter's index
            char_index_in_aplhabet = alphabet.index(char)
            char_index_in_message = count
            count += 1
            corres_secret_letter = key[char_index_in_message]
            key_letter_index_in_alphabet = alphabet.index(corres_secret_letter)
            sum_index = char_index_in_aplhabet + key_letter_index_in_alphabet
            #get the corresponding letter according to sum_index depending on the length of sum_index
            if sum_index < len(alphabet):
                final_letter = alphabet[sum_index]
            elif sum_index >= len(alphabet):
                final_index = sum_index % len(alphabet)
                final_letter = alphabet[final_index]
            #concatenate the encrypted letter to the encrypted_message
            encrypted_message += final_letter
        else:
            encrypted_message = -1
            break
    return encrypted_message


def decrypt_vigenere(message, secret):
    """
    The function takes in two string parameters. The message parameter expects a encrypted message
    that need to be decrypted. The secret expect a key string used to encrypt the message.
    The function retruns an decrypted message
    """
    alphabet = get_alphabet_vigenere()
    key = extend_vigenere(message, secret)
    decrypted_message = ''
    final_letter = ''
    count = 0
    
    #Find the index sum of the true letter and key letter depending of the index of key letter
    #in the alphabet for each cahracter in the message 
    for char in message:
        if char in alphabet:
            key_letter = key[count]
            count += 1
            index_key_letter = alphabet.index(key_letter)
            sum_index = alphabet.index(char)
            if sum_index >= index_key_letter:
                index_final_letter = sum_index - index_key_letter
                final_letter = alphabet[index_final_letter]
                decrypted_message += final_letter
            elif sum_index <= index_key_letter:
                real_sum = len(alphabet) + sum_index 
                index_final_letter = real_sum - index_key_letter
                final_letter = alphabet[index_final_letter]
                decrypted_message += final_letter
        else:
            decrypted_message = -1
            break
    return decrypted_message

























    
