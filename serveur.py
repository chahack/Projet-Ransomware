#! /usr/bin/python3

from cryptography.fernet import Fernet
import socket

#Générer la clé 
cle = Fernet.generate_key()
print("Clé : ", cle)

#Socket serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
s.bind(("", 1234))
s.listen()
cliaddr, addrlen = s.accept()
print(addrlen, " connecté")

#Code pour déchiffrer
code = cliaddr.recv(2048).decode()
if code == "cle" :
	cliaddr.send(cle)
	
"""
Amélioration possible : 
	- Chiffrement asymétrique de la clé (symétrique) pour réutiliser cette dite clé pour plusieurs attaques
"""
