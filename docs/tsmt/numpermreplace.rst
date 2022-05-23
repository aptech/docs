==============
numPermReplace
==============

10.0.39numPermReplace
=====================

Purpose
-------
Calculates the number of possible permutations of *n* number of items
   chosen *k* times with replacement.

Library
-------
tsmt

Format
------
num = numPermReplace(n, k);

Input
-----
= =================================
   n number of items.
   k number of times items are chosen.
   = =================================

Output
------
=== =========================================================
   num number of possible permutations allowing for replacement.
   === =========================================================

Example
-------
To find the number of permutations of 10 items, chosen 3 times,
   allowing for replacement we call the GAUSS procedure numPermReplace

   ::

numPermReplace(10, 3);

   The resulting output reads

   ::

1000.0000

Source
------
numperm.src
