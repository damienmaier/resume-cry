# Aléatoire
## Random number generator RNG
Quelque chose qui génère une suite de nombres qui paraît aléatoire.
## Entropie d'un bit
Mesure de l'incertitude sur ce bit, déterminé par sa distribution de probabilité
- Distribution uniforme : 1
- Distribution constante : 0
## Propriétés nécessaires pour la crypto
- Avoir de bonne propriétés statistiques
  - Tests statistiques : NIST, Diehard, Dieharder, variance, Chi-squared, ...
- Être imprédictible
  - <=> Passe le Next-bit test :
    - Un adversaire qui connaît les i premiers bits ne peut pas prédire le bit i+1
      - Avec une probabilité significativement meilleure que 1/2
      - Avec un effort de calcul réalisable
### Randomness extraction
Permet de transformer une suite de bits 
- Biaisés : Pr[b=0] != 0.5
- Mais indépendants Pr[b1, b2] = Pr[b1]Pr[b2]

en une suite de bits non biaisés.

- Von Neumann Randomness Extraction
  - 00|**10**|00|**10**|11|00|**01** devient
  - 1     1        0
- Il en existe d'autres, plus efficaces.
## True random number generator TRNG
Appareil qui génère des nombres aléatoires à partir d'un processus physique.
- Effets quantiques, bruit atmosphérique, ...
- Mauvais TRNG pour la crypto (prédictibles ou influençables par un attaquant) :
  - Time, PID, température
## Pseudo random number generator PRNG
- Algorithme qui génère une séquence de nombres
  - Ayant de bonnes propriétés statistiques
  - Déterminée par une seed
### Mauvais PRNGs pour la crypto
- Mersenne Twister
  - Prédictible : avec 624 outputs, on connaît l'état interne
- La plupart des PRNGs par défaut dans les langages et les librairies courantes.
- RC4, Lagged Fibonacci, LFSR, Lehmer
- random.org, randomnumbers.info, ...
  - Parce qu'ils peuvent découvrir nos secrets
### Bons PRNGs pour la crypto : CPRNGs
- Stream ciphers
- Blum Blum Shub
  - Problème sous-jacent : factorisation de grands nombres
  - Algo
    - n = pq
      - p, q premiers
      - p, q = 3 (mod 4)
    - x<sub>0</sub> = seed (qui est dans [2, n-1])
    - x<sub>i</sub> = x<sub>i-1</sub> mod n
    - b<sub>i</sub> = lsb(x<sub>i</sub>)
  - Très lent
- Blum-Micali
  - Problème sous-jacent : log discret
  - Algo
    - p grand nombre premier, g générateur dans le groupe multiplicatif &Zopf;<sub>p</sub><sup>*</sup>
    - x<sub>0</sub> = seed (qui est dans [2, p-1])
    - x<sub>i</sub> = g<sup>x<sub>i-1</sub></sup> mod p
    - b<sub>i</sub> = 1 si x<sub>i</sub> <= (p-1)/2
  - Très lent