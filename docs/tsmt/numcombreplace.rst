==============
numCombReplace
==============

10.0.37numCombReplace
=====================

Purpose
-------
Calculates the number of possible permutations of n number of items
   chosen k times, with replacement.

Library
-------
tsmt

Format
------
y = numCombReplace( n, k );

Input
-----
= =========================================
   n scalar, number of items.
   k scalar, number of times items are chosen.
   = =========================================

Output
------
= =================================================================
   y scalar, number of possible combinations allowing for replacement.
   = =================================================================

Example
-------
To find the number of permutations of 10 items, chosen 3 times,
   allowing for replacement we call the GAUSS procedure numCombReplace

   ::

numCombReplace( 10, 3 );

   The resulting output reads

   ::

220.0000

Source
------
numperm.src
