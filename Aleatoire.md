# Aléatoire
# Random number generator RNG
Quelque chose qui génère une suite de nombres qui paraît aléatoire.
# Entropie d'un bit
Mesure de l'incertitude sur ce bit, déterminé par sa distribution de probabilité
- Distribution uniforme : 1
- Distribution constante : 0
# Propriétés nécessaires pour la crypto
- Avoir de bonne propriétés statistiques
  - Tests statistiques : NIST, Diehard, Dieharder, variance, Chi-squared, ...
- Être imprédictible
  - <=> Passe le Next-bit test :
    - Un adversaire qui connaît les i premiers bits ne peut pas prédire le bit i+1
      - Avec une probabilité significativement meilleure que 1/2
      - Avec un effort de calcul réalisable
# Randomness extraction
Permet de transformer une suite de bits 
- Biaisés : Pr[b=0] != 0.5
- Mais indépendants Pr[b1, b2] = Pr[b1]Pr[b2]

en une suite de bits non biaisés.

- Von Neumann Randomness Extraction
  - 00|**10**|00|**10**|11|00|**01** devient
  - 1     1        0
- Il en existe d'autres, plus efficaces.
# True random number generator TRNG
Appareil qui génère des nombres aléatoires à partir d'un processus physique.
- Effets quantiques, bruit atmosphérique, ...
- Mauvais TRNG pour la crypto (prédictibles ou influençables par un attaquant) :
  - Time, PID, température
# Pseudo random number generator PRNG
- Algorithme qui génère une séquence de nombres
  - Ayant de bonnes propriétés statistiques pour ressembler à de l'aléatoire
  - Déterminée par une seed
### Forward security
Si dans le futur l'état interne de PRNG fuite, les bits générés actuellement ne seront pas compromis.
### Backward security
Si un état interne passé du PRNG fuite, les bits générés actuellement ne sont pas compromis.
- Nécessite d'ajouter régulièrement de la nouvelle entropie : reseeding
## Injection d'entropie
Se fait au moment du seeding et du reseeding
- Pour combiner différentes sources d'entropie il faut faire quelque chose du genre *nouvelle pool d'entropie* = Hash(*anciennce pool* | *nouvelles données aléatoires*)
  - Si on faisait juste un xor avec la valeur contenant de la nouvelle entropie, un attaquant capable de lire la pool actuelle et de contrôler la valeur ajoutée pourrait contrôler la valeur de la nouvelle pool.

## Mauvais PRNGs pour la crypto
- Mersenne Twister
  - Prédictible : avec 624 outputs, on connaît l'état interne
- La plupart des PRNGs par défaut dans les langages et les librairies courantes.
- RC4, Lagged Fibonacci, LFSR, Lehmer
- random.org, randomnumbers.info, ...
  - Parce qu'ils peuvent découvrir nos secrets
- DUAL_EC_DRBG
  - Backdoor potentielle
## Bons PRNGs pour la crypto : CPRNGs
### Stream ciphers
### Blum Blum Shub
- Problème sous-jacent : factorisation de grands nombres
- Algo
  - n = pq
    - p, q premiers
    - p, q = 3 (mod 4)
  - x<sub>0</sub> = seed (qui est dans [2, n-1])
  - x<sub>i</sub> = x<sub>i-1</sub> mod n
  - b<sub>i</sub> = lsb(x<sub>i</sub>)
- Très lent
### Blum-Micali
- Problème sous-jacent : log discret
- Algo
  - p grand nombre premier, g générateur dans le groupe multiplicatif &Zopf;<sub>p</sub><sup>*</sup>
  - x<sub>0</sub> = seed (qui est dans [2, p-1])
  - x<sub>i</sub> = g<sup>x<sub>i-1</sub></sup> mod p
  - b<sub>i</sub> = 1 si x<sub>i</sub> <= (p-1)/2
- Très lent
### Hash_DRBG
### HMAC_DRBG
- Initialisation : générer K et V qui sont déterminés par la seed
- Update : V<sub>i+1</sub> := HMAC(K, V<sub>i</sub>)
- Reseeding : Générer de nouveaux K et V déterminés par l'ancien K, l'ancien V et les nouvelles données.
- Plus lent que HASH_DRBG mais plus sûr
### CTR_DRBG
# Sources d'aléatoire sur un ordinateur
- `/dev/random` et `/dev/urandom`
  - PRNG régulièrement resseedé à partir de différentes sources d'aléatoire (disques, réseau, clavier, ...)
- Instructions pour obtenir de l'aléatoire du CPU
  - `RDSEED`
    - Données aléatoires issues d'un TRNG
  - `RDRAND`
    - Données aléatoires issues d'un PRNG régulièrement resseedé avec des données issues d'un TRNG
# Choisir un élément uniformément aléatoirement dans &Zopf;<sub>n</sub>
Rejection method :
- Obtenir log(n) bits aléatoires
- Si le nombre généré est >= n, recommencer