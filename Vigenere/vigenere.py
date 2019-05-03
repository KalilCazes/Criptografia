#!/usr/bin/env python3.6

encoded=open("Trabalho3.txt", "r").read()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

password_dictionary = open("dicionario.txt", "r")
password_dictionary = password_dictionary.read().splitlines()

def test_all_passwords():

    for password in password_dictionary:
        password = password.upper().strip()
        print(f"Chave usada:{password}")
        password = format_password(password,len(encoded))        
        decoded = test_password(encoded, password)
        print(decoded[:100])
        print("\n\n")

def test_password(encoded, password):

    decoded = ""
    
    for i in range(len(encoded)):
        encoded_i = LETTERS.find(encoded[i])
        password_i = LETTERS.find(password[i])
        decoded_char = LETTERS[(encoded_i - password_i)%26]
        decoded+=decoded_char

    return decoded

def format_password(password,length):

    new_password = ""
    for i in range(length):
        new_password += password[i%len(password)]
    return new_password


test_all_passwords()
    
