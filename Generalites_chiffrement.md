# Généralités chiffrement
## Permutations
- Un algorithme de chiffrement déterministe est une famille de permutations
    - Permutation <=> on peut inverser l'algorithme
    - La clé détermine une permutation précise
    - Sur {0, 1}<sup>n</sup> il existe 2<sup>n</sup>! permutations
## Chiffrement parfaitement sûr
Un chiffrement est appelé parfaitement sûr si le texte clair X et le texte chiffré Y sont statistiquement indépendants.
- <=> Pr[X|Y] = Pr[X]
- La connaissance du texte chiffré n'apporte aucune connaissance sur le texte clair
## Nonce et chiffrement déterministe
- Si le chiffrement est déterministe 
  - L'attaquant sait si deux messages identiques sont envoyés
  - Si l'attaquant a accès à un oracle de chiffrement, il peut faire un bruteforce sur le message clair
- Une manière de résoudre ce problème est que l'algorithme utilise un nonce ou un IV, différent pour chaque message
## Modèles de sécurité
### Attaques
- Attaque à texte chiffré : l'adversaire connaît un ou plusieurs textes chiffrés
- Attaque à texte clair connu : l'adversaire connaît une ou plusieurs paires (texte clair, texte chiffré)
- Attaque à texte clair choisi : l'adversaire a accès à un oracle de chiffrement
- Attaque à texte chiffré choisi : l'adversaire a accès à un oracle de déchiffrement
- Attaque à texte clair et chiffré choisi : combinaison des deux précédentes
### Oracle
Les attaques où l'adversaire a accès à un oracle sont soit :
- Adaptatives : l'adversaire peut attendre la réponse de l'oracle avant de faire une nouvelle requête
- Non-adaptative : l'adversaire doit effectuer toutes ses requêtes d'un coup
## Tailles de clés
La taille de la clé dépend de pendant combien de temps on veut protéger les données
- Clé symétrique : il faut prendre en compte la complexité du bruteforce et la loi de Moore.
- Clé asymétrique : en plus de la loi de Moore, il faut prendre en compte les meilleurs algorithmes connus pour casser le problème difficile sous-jacent

## Modèles de sécurité pour crypto asymétrique
### IND-CPA
- L'adversaire a la clé publique => oracle de chiffrement
- Si système de chiffrement est déterministe, il n'est pas IND-CPA
### IND-CCA
- L'adversaire a accès à un oracle de déchiffrement
  - Peut demander n'importe quoi sauf y
- IND-CCA : non adaptative
  - Accès à l'oracle seulement avant de recevoir y
- IND-CCA2 : adaptative
  - Accès à l'oracle avant et après