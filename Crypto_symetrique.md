# Crypto symétrique
## Chiffrement symétrique
### Algorithmes linéaires (et affines)
#### Description
La clé est (K, k), avec K une matrice inversible de taille n x n et k un vecteur de taille n. Les messages clairs et chiffrés m et c sont des vecteurs de taille n.

Chiffrement : <br>
c = Km + k (mod m)

Déchiffrement :<br>
m = K<sup>-1</sup>(c-k)
#### Attaque contre le chiffre de Vigenère (K = 1)
À partir d'une paire (message claire m, message chiffré c) on calcule k = c - m

#### Attaque contre le chiffrement linéaire (k = 0)
À partir de n paires (message claire, message chiffré) on peut poser :

KM = C

Où les colonnes de M sont les messages clairs et les colonnes de C sont les messages chiffrés.

On retrouve la clé en résolvant cette équation pour K (ce qui revient à calculer CM<sup>-1</sup>)

#### Attaque contre le chiffrement affine dans le cas général (chiffre de Hill)
À partir de de n+1 paires (message claire m, message chiffré c) on peut poser :

KM = C

Où la ième colonne de M est m<sub>i</sub> - m<sub>0</sub> et la ième colonne de C est c<sub>i</sub> - c<sub>0</sub>.

On retrouve K en résolvant cette équation pour K (ce qui revient à calculer CM<sup>-1</sup>). On retrouve k = c<sub>0</sub> - Km<sub>0</sub>

### Masque jetable
c = m xor k
- La clé k est une chaîne de bits
  - au moins aussi longue que le message
  - tirée de manière uniformément aléatoire
  - jamais réutilisée
- Sous ces conditions, le chiffrement est parfaitement sûr
- C'est un chiffrement affine, mais l'attaque contre un chiffrement affine suppose que la clé soit réutilisée
#### Attaques / problèmes
- Si la clé est réutilisée pour deux paires (m1, c1) et (m2, c2), l'adversaire peut récupérer m1 xor m2 = c1 xor c2
- Le message est facile à manipuler, inverser un bit du message chiffré ou de la clé inverse le bit correspondant du message déchiffré
- Il est difficile de générer une clé parfaitement aléatoire
- Transmettre des clés longues et nombreuses de manière sûre peut poser problème

### Chiffrement par bloc
#### Algorithmes de chiffrement par bloc
![This is an image](images/block_cipher.png)
- Déterministe (pas de nonce)
- Chiffre un nombre fixe de bits

Chiffrement itéré :


![This is an image](images/chiffrement_itere.png)
- On itère une fonction de ronde un certain nombre de fois
- K1, K2, ... sont appelés des sous-clés

Algorithmes :
- Data Encryption Standard (DES)
  - Taille de bloc : 64 bits
  - Taille de clé : 56 bits
    - Trop petit
- Triple-DES
  - À deux clés : chiffrer avec K1 -> déchiffrer avec K2 -> chiffrer avec K1
  - À trois clés : chiffrer avec K1 -> déchiffrer avec K2 -> chiffrer avec K3
  - Si on utilise à chaque fois la même clé, on obtient DES normal
- AES
  - Taille de bloc : 128 bits
  - Taille de clé : 128 bits, 192 bits ou 256 bits
  - Éléments d'une ronde :
    - AddRoundKey : seule étape qui dépend de la clé
    - SubBytes : seule étape pas linéaire
    - MixColumns : diffusion
    - ShiftRows : diffusion
#### Modes opératoires
Electronic code book (ECB)

![This is an image](images/ecb.png)
- Problèmes / attaques
  - Deux blocs identiques sont chiffrés de manière identique => perte de confidentialité
  - Résiste très mal aux attaques contre l'intégrité : un attaquant peut ajouter des blocs et changer leur ordre

Cipher block chaining (CBC)

![This is an image](images/cbc.png)
- Chiffrement séquentiel, déchiffrement peut être parallélisé
- Problèmes / attaques
  - Collision de blocs de ciphertext
    - Si on a deux blocs de ciphertext c<sub>i</sub> = c<sub>j</sub><br>alors c<sub>i-1</sub> XOR c<sub>j-1</sub> = m<sub>i</sub> XOR m<sub>j</sub>
    - Longueur du message en bits pour avoir une bonne probabilité de collision : k2<sup>k/2</sup> bits, avec k la taille d'un bloc en bits.

Counter mode (CTR)

![This is an image](images/ctr.png)

- Problèmes / attaques
  - Résiste mal aux attaques contre l'intégrité : inverser un bit du cipher text inverse le bit correspondant du message déchiffré
### Chiffrement par flot
- Souvent plus efficace que le chiffrement par bloc
#### RC4
- Taille de clé : 40 à 2048 bits
- Pas d'IV, la clé ne doit jamais être réutilisée
- Les premiers 256 octets possèdent de nombreuses faiblesses statistiques exploitables
- Pas recommandé
#### ChaCha20
- Taille de clé : 128 bits ou 256 bits
- Nonce de 64 bits (ou variante 96 bits)
![This is an image](images/chacha20.png)
![This is an image](images/chacha20_detail.png)
- Une double ronde contient 8 "quarter-rounds", une pour chaque colonne et pour chaque diagonale
- Les 10 doubles rondes sont inversibles. Sans l'addition mot par mot finale, on pourrait retrouver l'état initial à partir de la sortie de 512 bits 
### Taille de clés pour le chiffrement par bloc et par flot
- 128 - 256 bits.
- 80 bits est insuffisant.
- Pour une clé de taille l, l'attaquant doit essayer 2<sup>l - 1</sup> clés en moyenne, 2<sup>l</sup> clés au pire.

## MAC
### HMAC
![This is an image](images/hmac.png)
#### Problèmes / attaques
Si on fait un seul hash et pas les deux, et que la fonction de hashage utilise Merkel-Damgard:<br>
À partir d'un message M et de son MAC on peut générer un MAC valide pour un autre message en "continuant" le Merkel-Damgard :<br>
- M' = M || pad(M) || M2
- MAC' = f(MAC, M2 || pad(M || pad(M) || M2))
  - Où f est la fonction de réduction
  - Il faut éventuellement découper en plusieurs blocs et appliquer plusieurs fois f
### CBC-MAC
On chiffre le message avec CBC et un IV de 0. Le MAC est la valeur du dernier bloc chiffré.
#### Problèmes / attaques
À partir d'un message et de son MAC, on peut générer un autre message pour lequel le même MAC est valide :
- Pour un message faits des blocs m1, m2, m3, ... mn, on utilise m1, m2, m3, ..., mn, m1 xor MAC, m2, m3, ... mn.
  ![This is an image](images/attaque_cbcmac.png)
- Solutions :
  - Avoir uniquement des messages de taille fixe
  - Ajouter la longueur du message comme premier bloc
  - Surchiffrer le résultat avec une seconde clé / le xorer avec quelque chose qui dépend de la clé
### Galois MAC
Tag = c + M<sub>n</sub>H + M<sub>n-1</sub>H<sup>2</sup> + M<sub>n-2</sub>H<sup>3</sup> + ... + M<sub>1</sub>H<sup>n</sup>

Où c et H sont des valeurs dérivées de la clé, et où les calculs sont faits dans GF(2<sup>128</sup>)
#### Problèmes / attaques
- Si l'attaquant connaît H, il peut modifier n'importe quel bloc et générer un tag valide.
  - Par exemple si il modifie M<sub>n-2</sub> en M<sub>n-2</sub>', il obtient le nouveau tag en faisant tag' = tag + M<sub>n-2</sub>H<sup>3</sup> + M<sub>n-2</sub>'H<sup>3</sup>
- Si on ne surchiffre pas avec c, l'attaquant peut retrouver H
  - Si le message fait un seul bloc, on a H = Tag / M
  - Sinon on peut poser Tag = M<sub>n</sub>H + M<sub>n-1</sub>H<sup>2</sup> + M<sub>n-2</sub>H<sup>3</sup> + ... + M<sub>1</sub>H<sup>n</sup> et résoudre l'équation pour H
## Chiffrement authentifié
  ### CCM
![This is an image](images/ccm.png)
- CTR génère un keystream
- Le message est chiffré avec les blocs 1, 2, ... du keystream
- MAC 
  - Généré sur le message clair et le nonce
  - Fait avec CBC-MAC
  - Surchiffré avec le bloc 0 du keystream
### GCM
![This is an image](images/gcm.png)
- CTR génère un keystream
- Le message est chiffré avec les blocs 2, 3, ... du keystream
- MAC
  - Généré sur le message chiffré, n'utilise pas le nonce
  - Fait avec Galois MAC, où H est obtenu en chiffrant un bloc de zéros
  - Surchiffré avec le bloc 1 du keystream
## Fonctions de hachage
### Définition fonction de hachage cryptographiquement sûre
- À partir d'un message m de taille arbitraire, génère une empreinte h de taille constante l
- Le calcul d'une empreinte est rapide
- Résiste aux trois points suivants 
#### Résistance à la première préimage
- À partir de h, il est impossible de trouver m tel que h = H(m)
- Coût d'une attaque (bruteforce) : O(2<sup>l</sup>)
#### Résistance à la seconde préimage
- À partir de m et h = H(m), il est impossible de trouver m' différent de m tel que h = H(m')
- Coût d'une attaque (bruteforce) : O(2<sup>l</sup>)
#### Résistance aux collisions
- Il est impossible de trouver m, m' différents tels que H(m) = H(m')
- Coût d'une attaque : O(2<sup>l/2</sup>)
  - On calcule le hash de messages aléatoires et on les stocke dans une hashtable
### Constructions
#### Merkle-Damgard
![This is an image](images/merkle.png)

f est une fonction de compression.<br>
Une fonction de compression peut être fait avec la construction de Davies-Meyer :
![This is an image](images/davies-meyer.png)

#### Éponge
![This is an image](images/eponge.png)
### Padding
- Il peut être facile de trouver des préimages ou des collisions si le padding est mal géré
- Padding ok : 1 suivi de 0s puis de la longueur du message encodé sur 64 bits
  - Il faut toujours mettre un padding, même si la longueur du message est déjà un multiple de la taille de bloc

### Fonctions de hachage utilisées
#### MD5
- Cassé, il est possible de trouver rapidement des collisions
- Merkle-Damgard
- Empreintes de 128 bits
#### SHA-1
- Cassé, il est possible de trouver rapidement des collisions
- Merkle-Damgard
- Empreintes de 160 bits
#### SHA-256, SHA-512 (SHA-2)
- Sûr
- Merkle-Damgard + Davies-Meyer
- Empreintes de 224, 256, 384, 512 bits
#### SHA-3
- Sûr
- Construction éponge
- Empreintes de 224, 256, 384, 512 bits