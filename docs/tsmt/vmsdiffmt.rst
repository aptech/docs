=========
vmsdiffmt
=========

10.0.75vmsdiffmt
================

Purpose
-------

.. container::
   :name: Purpose

   Seasonally Differences matrices.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   y = vmsdiffmt(x, d, s);

Input
-----

.. container::
   :name: Input

   = =============================================================
   x matrix, T×K, data to be differenced.
   d scalar, the number of periods over which differencing occurs.
   s scalar, seasonal parameter, .
   = =============================================================

Output
------

.. container::
   :name: Output

   = ================================================
   y (T-d)×K matrix, the seasonally differenced data.
   = ================================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Load airline data
      airline = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/airline.dat");
      y = ln(airline);

      //Set parameters for differencing data
      s = 12;

      //Order of differencing
      d = 1;

      //Take seasonal differences
      y_sd = vmsdiffmt(y, s, d);

Source
------

.. container:: gfunc
   :name: Source

   vmutilsmt.src
