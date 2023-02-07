# Side channel attacks

## Differential power analysis (DPA)

Idée :

 - Device hardware qui contient un secret K, prend un input X et effectue un calcul qui fait intervenir ces deux valeurs
 - On trouve un critère (par exemple la valeur d'un certain bit à un moment du calcul) qui change la consommation électrique du device. En observant la consommation électrique lors d'un calcul pour un certain X, on peut voir si le critère était réalisé ou non (si le bit était à 0 ou 1), selon si on a une consommation électrique de type A ou B.
 - On fait effectuer des calculs au device avec différentes valeurs de X. Pour chaque K, on peut associer un partitionnement des X, en fonction de si la valeur de X doit donner une consommation électrique de type A ou de type B (en fonction de si le bit de notre critère est à 0 ou 1 pour cette combinaison K et X).
 - On observe le partitionnement réel des consommations lors des calculs et on identifie si il correspond au partitionnement pour un certain K.
 - Problème : en réalité le bruit fait qu'on ne peut pas distinguer une consommation de type A ou B
 - Pour un partitionnement qu'on veut tester, on calcule la différence entre la moyenne des consommations des X qui doivent être A et des X qui doivent être B. Si on voit une différence, le partitionnement est le bon et donc notre K est le bon.