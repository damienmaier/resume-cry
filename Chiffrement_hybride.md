# Principe
![This is an image](images/chiffrement_hybride.png)

Deux parties :
- Key encapsulation mechanism (KEM)
- Data encapsulation mechanism (DEM)
  - Algo de chiffrement symétrique

# ECIES
- Elliptic curve El Gamal
- Clé secrète k, clé publique kG
- Random r
- clé chiffrement || clé MAC = KDF(krG)

# RSA-KEM
- Textbook RSA (mais ok parce que utilisé une seule fois pour chiffrer un grand nombre)
- clé chiffrement || clé MAC = KDF(z)
- On chiffre z avec RSA