==============
numCombReplace
==============

10.0.37numCombReplace
=====================

Purpose
-------

.. container::
   :name: Purpose

   Calculates the number of possible permutations of n number of items
   chosen k times, with replacement.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   y = numCombReplace( n, k );

Input
-----

.. container::
   :name: Input

   = =========================================
   n scalar, number of items.
   k scalar, number of times items are chosen.
   = =========================================

Output
------

.. container::
   :name: Output

   = =================================================================
   y scalar, number of possible combinations allowing for replacement.
   = =================================================================

Example
-------

.. container::
   :name: Example

   To find the number of permutations of 10 items, chosen 3 times,
   allowing for replacement we call the GAUSS procedure numCombReplace

   ::

      numCombReplace( 10, 3 );

   The resulting output reads

   ::

      220.0000

Source
------

.. container:: gfunc
   :name: Source

   numperm.src
