=========
vmrootsmt
=========

10.0.72vmrootsmt
================

Purpose
-------

.. container::
   :name: Purpose

   Computes and prints the roots of the AR and MA characteristic
   equations.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   { arroots, maroots } = vmrootsmt( vout , printOutput );

Input
-----

.. container::
   :name: Input

   +-------------+-------------------------------------------------------+
   | vout        | An instance of the varmaOut structure, initialized    |
   |             | and filled during the ecmmt, svarmaxmt, varmaxmt      |
   |             | procedures.                                           |
   +-------------+-------------------------------------------------------+
   | printOutput | Scalar, a non-zero value indicates results are        |
   |             | printed to screen.                                    |
   +-------------+-------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ======= =================================================
   arroots Matrix, px1 vector of AR roots, possibly complex.
   maroots Matrix, px1 vector of MA roots, possibly complex.
   ======= =================================================

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
