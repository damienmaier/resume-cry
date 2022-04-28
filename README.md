# resume-cry

|                            | anneau &Zopf;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                            | anneau &Zopf;<sub>p</sub>[x]                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre d'éléments          | Infini                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                            | Infini                                                                                                                                                                                                                                                                                                                                                                                        |
|                            | 1 divise tous les nombres                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                            | les polynômes constants divisent tous les polynômes                                                                                                                                                                                                                                                                                                                                           |
| Nombre premier p           | Non égal à 1<br/>Divisible uniquement par : <br/>- 1<br/>- p                                                                                                                                                                                                                                                                                                                                                                                                                                 | Polynôme irréductible p(x)                 | Non constant<br/>Divisible uniquement par:<br/>- les polynômes constants<br/>- &alpha;p(x), pour tous les &alpha; &in; &Zopf;<sub>p</sub>                                                                                                                                                                                                                                                     |
| Crible d'Eratosthène       | Trouve les nombres premiers < n : <br/> Barrer tous les multiples du plus petit entier non barré, s'arrêter à ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\sqrt{n}) <br/>Problème : coût en calcul et en mémoire                                                                                                                                                                                                                                         | Déterminer si un polynôme est irréductible | <ul><li>Degré 0 : jamais irréductible</li><li>Degré 1 : toujours irréductible</li><li>Degré 2 ou 3 : racine <=> pas irréductible</li><li>Degré > 3 :<br/>racine => pas irréductible<br/>tester de diviser par tous les polynômes irréductibles de degré &le; degré/2</li></ul>                                                                                                                |
| Nombres premiers < 100     | 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97                                                                                                                                                                                                                                                                                                                                                                                               | Liste de polynômes unitaires irréductibles | <ul><li>Dans &Zopf;<sub>2</sub>[x] (liste complète pour les degrés 2,3,4) :<br/>x<sup>2</sup>+x+1,<br/>x<sup>3</sup>+x<sup>2</sup>+1, x<sup>3</sup>+x+1<br/>x<sup>4</sup>+x<sup>3</sup>+x<sup>2</sup>+x+1, x<sup>4</sup>+x<sup>3</sup>+1, x<sup>4</sup>+x+1</li><li>Dans &Zopf;<sub>3</sub>[x] :<br/>x<sup>2</sup>+1, x<sup>2</sup>+2x+2</li></ul>                                            |
| Factorisation unique       | Tout nombre naturel &ge; 2 est le produit unique de nombres premiers.<br/><br/> On ne connaît pas d'algorithme efficace pour trouver cette factorisation.                                                                                                                                                                                                                                                                                                                                    |                                            | Tout polynôme a(x) &in; &Zopf;<sub>p</sub>[x] non nul est le produit unique de polynômes unitaires irréductibles et d'un entier.<br/><br/>Il existe des algorithmes efficaces pour trouver cette factorisation.                                                                                                                                                                               |
| Nombre de nombres premiers | <ul><li>Il existe une infinité de nombres premier</li><li>Nombre de nombres premiers &le; n : &pi;(n) &thickapprox; n / ln(n)</li><li>Probabilité de tomber sur un nombre premier si on choisit entre 0 et n : environ 1 / ln(n)</li><li>Probabilité de tomber sur un nombre premier si on choisit un nombre à n bits : environ 1 / n ln(2)</li></ul>                                                                                                                                        |||
| PGCD                       | Plus grand diviseur commun<br/><br/>On le trouve avec l'algorithme d'Euclide.<br/><br/>Pour a > b :<br/>pgcd(a, b) = pgcd(b, (pgcd(a, b))                                                                                                                                                                                                                                                                                                                                                    |                                            | PGDC de a(x) et b(x) :<br/>Unique polynôme **unitaire** de degré maximal qui divise a(x) et b(x)<br/><br/>On le trouve avec l'algorithme d'Euclide. Si le résultat n'est pas un polynôme unitaire, il faut le diviser par le facteur du plus haut degré pour obtenir un polynôme unitaire.<br/><br/>Pour degré de a(x) > degré de b(x) :<br/>pgcd(a(x), b(x)) = pgcd(b(x), (pgcd(a(x), b(x))) |
| Nombres premiers entre eux | a est premier avec b<br/><=> pgdc(a, b) = 1<br/><=> a est inversible modulo b, càd il existe a<sup>-1</sup> tel que a<sup>-1</sup>a &Congruent; 1 (mod b)<br/><=> les décompositions en facteurs premiers de a et b n'ont aucun facteur commun<ul><li>Deux nombres premiers sont toujours premiers entre eux</li><li>Un nombre premier p est premier avec tous les nombres < p</li><li>Les seuls nombres qui ne sont pas premiers avec un nombre premier p sont les multiples de p</li></ul> |                                            | pgdc(a(x), b(x)) = 1<br/><=> a(x) est inversible modulo b(x)<br/><=> les décompositions en polynômes unitaires irréductibles de a(x) et b(x) n'ont aucun polynôme en commun                                                                                                                                                                                                                   |
| Identité de Bézout         | Pour d = pgdc(a, b), l'identité de Bézout est l'équation :<br/>ax + by = d<br/><br/>Si d = 1, y est l'inverse de b modulo a.<br/><br/>On trouve x et y avec l'algorithme d'Euclide étendu                                                                                                                                                                                                                                                                                                    |                                            | Idem.                                                                                                                                                                                                                                                                                                                                                                                         |
| Lemme d'Euclide            | Si un nombre premier p divise rs, alors p est un des facteurs premiers de r ou de s                                                                                                                                                                                                                                                                                                                                                                                                          |

|                   | Groupe &Zopf;<sub>m</sub><sup>*</sup>                                                                                                                                                                                                                                                                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nombre d'éléments | Nombre d'éléments premiers avec m, noté &phi;(m)<br/><br/>Pour p premier:<ul><li>&phi;(p) = p - 1</li><li>&phi;(p<sup>k</sup>) = (p - 1)p<sup>k-1</sup></li></ul>Pour m et n premiers entre eux:<ul><li>&phi;(mn) = &phi;(m)&phi;(n)</li></ul>Algo général pour &phi;(n) :<br/>resultat = n<br/>pour chaque facteur premier p de n :<br/>&nbsp;resultat -= resultat/p |
