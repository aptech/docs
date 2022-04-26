==========
tautocovmt
==========

10.0.57tautocovmt
=================

Purpose
-------

.. container::
   :name: Purpose

   Computes the theoretical autocovariances given the coefficient values
   from an ARMA( *p, q* ) process.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   g = tautocovmt( b, p, q );

Input
-----

.. container::
   :name: Input

   = ===================================
   b Kx1 vector, parameter coefficients.
   p scalar, the autoregressive order.
   q scalar, the moving average order.
   = ===================================

Output
------

.. container::
   :name: Output

   = =======================================================
   g [Max( p , q )+1]×1 vector, theoretical autocovariances.
   = =======================================================

Remarks
-------

.. container::
   :name: Remarks

   The theoretical autocorrelations are found by dividing *g* by
   *g*\ [1].

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //ARMA parameter coefficients
      b = { 0.6, -0.3, -0.5 };

      //AR lags
      p = 2;

      //MA lags
      q = 1;

      //Find theoretical autocovariances
      g = tautocovmt( b, p, q );

      //Print solution
      print "Theoretical autocovariances :";;
      g';

Source
------

.. container:: gfunc
   :name: Source

   tautocovmt.src
