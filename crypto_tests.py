from crypto_functions import *

#test for function create_matrix(row_length, column_length)
assert create_matrix(2, 2) == [[' ', ' '], [' ', ' ']] # 2 rows, 2 columns
assert create_matrix(2, 3) == [[' ', ' ', ' '], [' ', ' ', ' ']] # 2 rows, 3 columns
assert create_matrix(7, 5) == [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
assert create_matrix(8, 2) == [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']]
assert create_matrix(0, 19) == []
assert create_matrix(5, 0) == [[], [], [], [], []]
assert create_matrix(0, 0) == []

#test for encode_to_matrix(message_string, column_length)
assert encode_to_matrix("CSWEIGHT TEACHES US PROGRAMMING", 5) == [['C', 'S', 'W', 'E', 'I'], ['G', 'H', 'T', ' ', 'T'], ['E', 'A', 'C', 'H', 'E'], ['S', ' ', 'U', 'S', ' '], ['P', 'R', 'O', 'G', 'R'], ['A', 'M', 'M', 'I', 'N'], ['G', ' ', ' ', ' ', ' ']]
assert encode_to_matrix("YELLOW SUBMARINE", 2) == [['Y', 'E'], ['L', 'L'], ['O', 'W'], [' ', 'S'], ['U', 'B'], ['M', 'A'], ['R', 'I'], ['N', 'E']]
assert encode_to_matrix("CHECK OUT THE HOOK WHILE MY DJ REVOLVES IT", 9) == [['C', 'H', 'E', 'C', 'K', ' ', 'O', 'U', 'T'], [' ', 'T', 'H', 'E', ' ', 'H', 'O', 'O', 'K'], [' ', 'W', 'H', 'I', 'L', 'E', ' ', 'M', 'Y'], [' ', 'D', 'J', ' ', 'R', 'E', 'V', 'O', 'L'], ['V', 'E', 'S', ' ', 'I', 'T', ' ', ' ', ' ']]
assert encode_to_matrix("I LIKE CRYPTOGRAPHY", 19) == [['I', ' ', 'L', 'I', 'K', 'E', ' ', 'C', 'R', 'Y', 'P', 'T', 'O', 'G', 'R', 'A', 'P', 'H', 'Y']]
assert encode_to_matrix("",1) == []


#test for function encrypt_transposition(message, nColumns)
assert encrypt_transposition("CSW EIGHT IS AMAZING!", 4) == "CET Z!SI AI WGIMN  HSAG "
assert encrypt_transposition("I WILL ACE THE FINAL PROJECT!", 8) == "ICIJ ENEW ACITLTLH !LEP   R AFO "
assert encrypt_transposition("YOU GOT THIS! YOU CAN DO IT!", 5) == "YOIONIOTSU TU ! D! T CO GHYA  "
assert encrypt_transposition("WEATHER IS QUITE NICE TODAY", 4) == "WHIU EDEESIN AAR TITYT QECO "
assert encrypt_transposition("a", 1) == "a"
assert encrypt_transposition("    ", 4) == "    "
assert encrypt_transposition("", 1) == ""

#test for function decrypt_transposition(message, nColumns)
assert decrypt_transposition("CET Z!SI AI WGIMN  HSAG ", 4) == "CSW EIGHT IS AMAZING!"
assert decrypt_transposition("ICIJ ENEW ACITLTLH !LEP   R AFO ", 8) == "I WILL ACE THE FINAL PROJECT!"
assert decrypt_transposition("YOIONIOTSU TU ! D! T CO GHYA  ", 5) == "YOU GOT THIS! YOU CAN DO IT!"
assert decrypt_transposition("EEEXLNCLT", 3) == "EXCELLENT"
assert decrypt_transposition("WHIU EDEESIN AAR TITYT QECO ", 4) == "WEATHER IS QUITE NICE TODAY"
assert decrypt_transposition("    ", 4) == ""
assert decrypt_transposition("4   ", 4) == "4"
assert decrypt_transposition(" ", 1) == ""
assert decrypt_transposition("a", 1) == "a"
assert decrypt_transposition("", 1) == ""

#test for function extend_string(key_string, new_length)
assert extend_string("CS8", 10) == "CS8CS8CS8C"
assert extend_string("CMPSC8", 18) == "CMPSC8CMPSC8CMPSC8"
assert extend_string("A very long sentence", 0) == ""
assert extend_string("Hello World!", 7) == "Hello W"
assert extend_string("Hello World!", 0) == ""

#test for function extend_vigenere(message, secret)
assert extend_vigenere('VICTORYISNEAR', 'ARC') == 'ARCARCARCARCA'
assert extend_vigenere('', 'ARC') == ''
assert extend_vigenere('CallMeIshmaelThe3rd', 'MOBYDICK') == 'MOBYDICKMOBYDICKMOB'
assert extend_vigenere('CryptographyIsSoCool', 'Bitcoin') == 'BitcoinBitcoinBitcoi'
assert extend_vigenere('a', 'Bitcoin') == 'B'
assert extend_vigenere('Bitcoin', 'B') == 'BBBBBBB'

#test for function extend_vigenere(message, secret)
assert get_alphabet_vigenere() == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'

#test for function encrypt_vigenere(message, secret)
assert encrypt_vigenere("", "NOWORDS") == ""
assert encrypt_vigenere("CallMeIshmaelThe3rd", "MOBYDICK") == "OomJPmKCtAbCo1jofFe"
assert encrypt_vigenere("CryptographyIsSoCool", "Bitcoin") == "D9r1h63sSiTmqfT6v0c3"
assert encrypt_vigenere("WE HOPE YOU LIKE THE PROJECT", "CSW8") == -1
assert encrypt_vigenere("@#!@$@$*&^%^&*^(^*(*$#%^$&%*^(", "CSW8") == -1

#test for function decrypt_vigenere(message, secret)
assert decrypt_vigenere("", "NOWORDS") == ""
assert decrypt_vigenere("OomJPmKCtAbCo1jofFe", "MOBYDICK") == "CallMeIshmaelThe3rd"
assert decrypt_vigenere("D9r1h63sSiTmqfT6v0c3", "Bitcoin") == "CryptographyIsSoCool"
assert decrypt_vigenere("K3mXWaUeG", "CS8") == "ILOVECSW8"



