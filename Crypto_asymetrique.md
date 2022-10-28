# Crypto asymétrique


# Algorithmes
## Diffie-Hellman
### Générer les paramètres publics
- Choisir deux nombres premiers p et q qui respectent p = cq + 1
  - Cette relation permet l'existence d'un élément d'ordre q, puisque comme ça l'ordre du groupe p-1 est un multiple de q
  - Le fait que q soit premier empêche certaines attaques
- Trouver g, un élément d'ordre q du groupe multiplicatif &Zopf;<sub>p</sub>* 
#### EC
- Courbe elliptique avec N points
- point G d'ordre n premier
### Protocole
![This is an image](images/diffie-hellman.png)
- KDF : key derivation function
#### EC
- a et b sont dans 1, ..., n-1
- Y<sub>a</sub> = aG, Y<sub>b</sub> = bG
- K = abG

## El Gamal
Chiffrement non déterministe
### Clés
- Clé privée : a appartient à &Zopf;<sub>q</sub>
- Clé publique : A = g<sup>a</sup> mod p
#### EC
- Clé privée : a appartient à 1, ... , n-1
- Clé publique : A = aG
### Chiffrement
- Tirer k appartient à &Zopf;<sub>q</sub> uniformément au hasard
- (u, v) = (g<sup>k</sup> mod p, MA<sup>k</sup> mod p)
#### EC
- Tirer k appartient à 1, ..., n-1
- (u, v) = (kG, M + [kA]<sub>x</sub>)
### Déchiffrement
m = v/u<sup>a</sup> mod p
#### EC
m = v - [au]<sub>x</sub>
## Signatures DSA
![This is an image](images/dsa.png)

![This is an image](images/dsa_verification.png)
### EC
![This is an image](images/ecdsa.png)

![This is an image](images/ecdsa_verification.png)
## Chiffrement RSA
### Génération des clés
- Choisir des nombres premiers p et q, calculer n = pq
- Choisir un e premier avec phi(n) = (p-1)(q-1)
  - On choisit souvent e = 65537
    - Permet de chiffrer de manière efficace car e = 100...1
    - C'est un nombre premier donc il est inversible modulo phi(n) (sauf si il divise phi(n))
- Calculer d = l'inverse de e modulo phi(n)
- (n, e) est la clé publique, (n, d) est la clé privée
### Chiffrement / déchiffrement textbook RSA
- c = m<sup>e</sup> mod n
- m = c<sup>d</sup> mod n
### Formatage de message
RSA-OAEP

![This is an image](images/rsa-oaep.png)
### Problèmes/attaques
- Sur textbook RSA (donc sans formatage)
  - Comme la clé publique est connue et que RSA est déterministe, l'attaquant peut toujours faire une attaque à texte clair choisi
  - Si il y a un nombre trop faible de messages possibles, on peut retrouver le message par bruteforce
- Si un attaquant connaît phi(n)
  - Il peut retrouver d en calculant l'inverse de e mod phi(n)
  - Il peut retrouver p et q en résolvant n = pq, phi(n) = (p - 1)(q - 1)
## Signatures RSA
- Signature s = m<sup>d</sup> mod n
- Vérification : m = s<sup>e</sup> mod n et on vérifie que m = le message signé
### Signature rapide avec le CRT
- s<sub>p</sub> = m<sup>d mod p-1</sup> mod p
- s<sub>q</sub> = m<sup>d mod q-1</sup> mod q
- s = s<sub>p</sub> q<sup>-1</sup> q + s<sub>q</sub> p<sup>-1</sup> p mod n
- Beaucoup plus efficace parce que les exponentiations se font modulo la moitié de la taille de n
### Formatage
RSA-PSS
### Problèmes / attaques
- Les signatures textbook RSA (donc sans formatage) sont malléables
  - Pour un message et une signature (m, s), (m<sup>k</sup>, s<sup>k</sup>) est aussi une paire valide

# Problèmes difficiles sous-jacents
- Diffie-Hellman, El Gamal, DSA : logarithme discret dans &Zopf;<sub>p</sub>*
- ECDH, El Gamal courbes éliptiques, ECDSA : logarithme discret sur une courbe elliptique
- RSA : factorisation d'un nombre entier

# Tailles de clés
- RSA
  - taille de n : 2048 - 3072 bits
- DH, El Gamal, DSA
  - taille de p : 2048 - 3072 bits
  - taille de q, et donc des valeurs secrètes : 200 - 256 bits
- Elliptic curve
  - 256 bits