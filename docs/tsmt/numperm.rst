=======
numPerm
=======

10.0.38numPerm
==============

Purpose
-------
Calculates the number of possible permutations of n number of items
   chosen k times, without replacement.

Library
-------
tsmt

Format
------
num = numPerm(n, k);

Input
-----
= =========================================
   n scalar, number of items.
   k scalar, number of times items are chosen.
   = =========================================

Output
------
=== ============================================================
   num scalar, number of possible permutations without replacement.
   === ============================================================

Example
-------
To find the number of permutations of 10 items, chosen 3 times,
   withut replacement we call the GAUSS procedure numPerm

   ::

numperm(10, 3);

   The resulting output reads

   ::

720.0000

Source
------
numperm.src
