===========
permReplace
===========

10.0.41permReplace
==================

Purpose
-------

.. container::
   :name: Purpose

   Lists all possible permutations with replacement for n number of
   items, chosen k times.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   y = permReplace(n, k);

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

   = ===========================================
   y a matrix listing all possible permutations.
   = ===========================================

Example
-------

.. container::
   :name: Example

   To list all permutations with replacement for 3 items, chosen 2
   times, we call the GAUSS procedure permReplace

   ::

      permReplace(3, 2);

   The resulting output reads

   ::

            1.0000000        1.0000000 
            1.0000000        2.0000000 
            1.0000000        3.0000000 
            2.0000000        1.0000000 
            2.0000000        2.0000000 
            2.0000000        3.0000000 
            3.0000000        1.0000000 
            3.0000000        2.0000000 
            3.0000000        3.0000000

Source
------

.. container:: gfunc
   :name: Source

   permReplace.src
