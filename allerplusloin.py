import json
import hashlib

# créé un dictionnaire
passwords = []

# pour que l 'utilisateur puisse saisir son mot de passe
password = input("Entrez votre mot de passe !"'\n')

# Hacher le mot de passe
hashed_password = hashlib.sha256 (password.encode('utf-8')).hexdigest()

#ajouter le mot de passe haché au dictionnaire
passwords[password] = hashed_password

# enregistrer le dictionnaire dans un fichier
with open('passwords.json','w') as f:
    json.dump(passwords,f)

    def ajout_passwod(password):
        with open ('passwords.json','r') as f:
            passwords = json.load(f)
            
            password.append(passwords)

        with open ('passwords.json','w') as f:
                json.dump(passwords,f)

    def affiche_password():
        with open('paswords.json','r') as f:
            passwords = json.load
        for password in passwords:
            print(password,f)

ajout_passwod('test123')
affiche_password()
