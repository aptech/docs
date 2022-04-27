==============
numPermReplace
==============

10.0.39numPermReplace
=====================

Purpose
-------

.. container::
   :name: Purpose

   Calculates the number of possible permutations of *n* number of items
   chosen *k* times with replacement.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   num = numPermReplace(n, k);

Input
-----

.. container::
   :name: Input

   = =================================
   n number of items.
   k number of times items are chosen.
   = =================================

Output
------

.. container::
   :name: Output

   === =========================================================
   num number of possible permutations allowing for replacement.
   === =========================================================

Example
-------

.. container::
   :name: Example

   To find the number of permutations of 10 items, chosen 3 times,
   allowing for replacement we call the GAUSS procedure numPermReplace

   ::

      numPermReplace(10, 3);

   The resulting output reads

   ::

            1000.0000

Source
------

.. container:: gfunc
   :name: Source

   numperm.src
