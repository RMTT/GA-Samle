#### Genetic Algorithm Sample

A grid contain some stamp,a robot from (0,0) to somewhere to collect the stamp

Here are the actions:
+ move one cell northward
+ move one cell southward
+ move one cell eastward
+ move one cell westward
+ immovability
+ collect stamp
+ random movement

Here are the rules:
+ beyond the boundary: -5 scores
+ apply action of collect stamp but no stamp: -1 score
+ apply action of collect stamp and success: +10 scores
+ immovability: -1 score
