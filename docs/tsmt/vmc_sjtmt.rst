=========
vmc_sjtmt
=========

10.0.67vmc_sjtmt
================

Purpose
-------

.. container::
   :name: Purpose

   Returns critical values for the Johansen Trace statistic.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   c_values = vmc_sjtmt( n, p );

Input
-----

.. container::
   :name: Input

   +---+-----------------------------------------------------------------+
   | n | scalar, number of variables in the system.                      |
   +---+-----------------------------------------------------------------+
   | p | scalar, order of the time-polynomial to include in the fitted   |
   |   | regression.                                                     |
   +---+-----------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ======== ==============================
   c_values 6×1 vector of critical values.
   ======== ==============================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Number of variables in the system
      num_vars = 3;

      //Order of time-polynomial included in fitted regression
      p = 2;

      //Find critical values
      c_values = vmc_sjtmt( num_vars, p );

      //Print solution
      print "Critical Values for Johansen Trace stat :";;
      c_values';

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
