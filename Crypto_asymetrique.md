Crypto asymétrique
===

# Algorithmes
## Diffie-Hellman
### Principe général
#### Paramètres publics
- Groupe G où le logarithme discret est difficile
- g &#8712; G, d'ordre premier q
  - Le fait que q soit premier empêche certaines attaques
#### Algorithme
- Alice
  - Choisit un exposant a &in; &Zopf;<sub>q</sub>*
  - Envoie y<sub>a</sub> = g<sup>a</sup>
  - Secret partagé k = KDF(y<sub>b</sub><sup>a</sup>)
- Bob
  - Choisit un exposant b &#8712; &Zopf;<sub>q</sub>*
  - Envoie y<sub>b</sub> = g<sup>b</sup>
  - Secret partagé k = KDF(y<sub>a</sub><sup>b</sup>)
### G = groupe multiplicatif &Zopf;<sub>p</sub>* avec p premier
- Choisir deux nombres premiers p et q qui respectent p = cq + 1
  - Cette relation permet l'existence d'un élément d'ordre q, puisque comme ça l'ordre du groupe p-1 est un multiple de q
- Trouver g, un élément d'ordre q du groupe multiplicatif &Zopf;<sub>p</sub>* 
### Courbe elliptique
- Point G d'ordre n premier

## El Gamal
Chiffrement non déterministe
### Principe général
#### Paramètres publics
Comme pour Diffie-Hellman
#### Clés
- Clé privée
  - a &in; &Zopf;<sub>q</sub>
- Clé publique
  - A = g<sup>a</sup>
#### Chiffrement
- Tirer k &in; &Zopf;<sub>q</sub> uniformément au hasard
- (u, v) = (g<sup>k</sup>, M chiffré avec A<sup>k</sup>)
#### Déchiffrement
M = v déchiffré avec u<sup>a</sup>

## Signatures DSA
### Principe général
#### Paramètres publics
- Groupe G où le logarithme discret est difficile
- g &in; G, d'ordre premier q
#### Clés
- Clé privée
  - a &in; &Zopf;<sub>q</sub>
- Clé publique
  - A = g<sup>a</sup>
#### Idée intuitive de la signature
- Choisir un exposant *k &in; &Zopf;<sub>q</sub>*
  - Choisi uniformément au hasard
  - Secret
- Fixer *r* déterminé par *g<sup>k</sup> &in; G*
  - *r* premier élément de la signature
- Soit l'exposant *b &in; &Zopf;<sub>q</sub>* déterminé par *M*, *a* et *r*
- Calculer *s &in; &Zopf;<sub>q</sub>* t. q. *g<sup>bs</sup> = g<sup>k</sup>*
  - *s* deuxième élément de la signature
  - *s* est l'exposant qui permet de "se déplacer" de *g<sup>b</sup>* à *g<sup>k</sup>*
  - Le fait que le point de départ dépende de *r* permet de prouver qu'on n'a pas choisi *g<sup>k</sup>* a posteriori
  - En calculant *s*, on donne la preuve qu'on connaît *a*
#### Idée intuitive de la vérification
- Calculer *g<sup>b</sup>* en utilisant *g<sup>a</sup>*, *M* et *r* qui sont connus
- Calculer *g<sup>bs</sup>*
  - Si la signature est valide, ça doit être égal à *g<sup>k</sup>* qui doit donner *r*
#### Modulo
- Tous les calculs d'exposants ont lieu modulo q
- C'est ok puisque q est l'ordre de g
### DSA
*s* est inversé

![This is an image](images/dsa.png)

D'abord vérifier que r et s sont dans &Zopf;<sub>q</sub>

![This is an image](images/dsa_verification.png)
### ECDSA
*s* est inversé

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
### RSA PKCS v1.5
- Inclut (facultatif) de l'aléatoire
- N'est pas IND-CPA
- Ne pas utiliser
### RSA-OAEP
![This is an image](images/rsa-oaep.png)

IND-CCA secure contre les adversaires black box
### Problèmes/attaques
- Sur textbook RSA (donc sans formatage)
  - Comme la clé publique est connue et que RSA est déterministe, l'attaquant peut toujours faire une attaque à texte clair choisi
  - Si il y a un nombre trop faible de messages possibles, on peut retrouver le message par bruteforce
  - e trop petit
    - m<sup>e</sup> < n, donc pas de modulo et c'est facile de calculer la racine nième de c.
    - Même si m est assez grand pour que le modulo ait lieu, si e est petit et réutilisé plusieurs fois pour le même message avec des n différents, on peut utiliser le CRT pour retrouver m
    - Si e est petit, on peut faire une attaque de Coppersmith
  - d trop petit
    - Wiener key recovery attack : si d < racine quatrième de n.
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