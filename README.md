#### Genetic Algorithm Sample

A grid contain some stamp,a robot from (0,0) to somewhere to collect the stamp

Here are the actions:
+ move one grid northward
+ move one grid southward
+ move one grid eastward
+ move one grid westward
+ immovability
+ collect stamp
+ random movement

Here are the rules:
+ beyond the boundary: -5 scores
+ apply action of collect stamp but no stamp: -1 scores
+ apply action of collect stamp and success: +10 scores
