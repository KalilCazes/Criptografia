#!/usr/bin/env python3.6

#lendo a frase cifrada
fh=open("Trabalho1.txt", "r").read()

#inicializacao de variaveis
decoded=''
ascii=0
key=0

#No caso do portugues, sao 26 possibilidades
while key<26:
    for k in fh:
    #obtenho o valor da letra na tabela ascii
        ascii=ord(k)
        ascii+=key
        if ascii>90:
            ascii-=26
        decoded+=chr(ascii)
    print(f"Chave usada:{key}")
    print(decoded)
    decoded=''
    key+=1
