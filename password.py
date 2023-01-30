import hashlib
# Vérification du mot de passe
def verif_motdepasse(mdp):
    if len(mdp) < 8:
        return False
    if not any(c.isupper() for c in mdp):
        return False
    if not any(c.islower() for c in mdp):
        return False
    if not any(c.isdigit() for c in mdp):
        return False
    if not any(c in "!@#$%^&*" for c in mdp):
        return False
    return True

# crypter le mot de passe
def motdepasse_crypter(mdp):
    return hashlib.sha256(mdp.encode()).hexdigest()

mdp = input("Choisit un mot de passe : ")
while not verif_motdepasse(mdp):
    print("Erreur: mot de passe ne répond pas aux exigences de sécurité.")
    mdp = input("Choisit un mot de passe ")

print("Mot de passe valider.")
mdp_crypter = motdepasse_crypter(mdp)
print("Mot de passe crypter", mdp_crypter)
