===========
vmrztcritmt
===========

10.0.78vmrztcritmt
==================

Purpose
-------

.. container::
   :name: Purpose

   Returns |image1| critical values for the Augmented Dickey-Fuller
   statistic, derived from the residuals of a cointegrating regression.
   Depends on *p*, the AR order in the fitted regression, the number of
   observations, and the number of explanatory variables.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   c_values = vmrztcritmt( nobs, n, p );

Input
-----

.. container::
   :name: Input

   ==== ============================================================
   nobs scalar, number of observations in the series.
   n    scalar, column dimension of *x*.
   p    scalar, order of the time-polynomial in the null hypothesis.
   ==== ============================================================

Output
------

.. container::
   :name: Output

   ======== ==============================
   c_values 6×1 vector of critical values.
   ======== ==============================

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Data
      yt = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/panel_g.csv" );
      log_yt = log(yt[., 2:9]);

      //Test first column of data
      y_test = log_yt[., 1]; 

      //Number of observations
      numObs = rows(y_test);

      //Set lags to follow Enders, Table 4.8
      p = 5;

      //Number of columns in x
      n = 2;

      //Find critical values
      crit = vmrztcritmt(numObs, n, p);

      print "The tau critical values for the Augmented Dickey-Fuller stat : ";
      crit';

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src

.. |image1| image:: _static/images/Equation743.svg
   :class: mcReset
