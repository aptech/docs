========
breitung
========

10.0.11breitung
===============

Purpose
-------

.. container::
   :name: Purpose

   Panel series unit root testing. The *z*-statistic constructed from
   the mean *t*-statistic has an asymptotic standardized normal
   distribution and tests the null hypothesis that all series are *I(1)*
   against the alternative that all series are *I(0)*

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   bstat = breitung(y, trend, constant, demean, lags);

Input
-----

.. container::
   :name: Input

   +----------+----------------------------------------------------------+
   | y        | T×M matrix, data, M > 5.                                 |
   +----------+----------------------------------------------------------+
   | trend    | scalar, 0 = no trend, 1 = trend.                         |
   +----------+----------------------------------------------------------+
   | constant | if nonzero, constant included in model.                  |
   +----------+----------------------------------------------------------+
   | demean   | scalar, 0 to specify no demeaning or 1 to subtract       |
   |          | cross-sectional means.                                   |
   +----------+----------------------------------------------------------+
   | lags     | scalar, number of lags.                                  |
   +----------+----------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ===== ===============
   bstat test statistic.
   ===== ===============

Remarks
-------

.. container::
   :name: Remarks

   The Breitung panel series unit root test utilizes the sample mean of
   the *t*-statistics across all individual series within a panel of
   time series variables. However, the procedure pre-adjusts data to
   address biased estimation.

   It is assumed that the autoregressive parameter is constant across
   all panels. This allows the use of the standard *t*-statistic but
   requires that the panels be strongly balanced.

   The procedure performs an individual ADF test on each series n then
   forms the sample mean of the *t*-statistic. The *z*-statistic
   constructed from the mean *t*-statistic has an asymptotic
   standardized normal distribution and tests the null hypothesis that
   all series are *I(1)* against the alternative that all series are
   *I(0)*.

Example
-------

.. container::
   :name: Example

   ::

      new;
      library tsmt;

      //Load data
      fname = getGAUSSHome() $+ "pkgs/tsmt/examples/index.dat";
      y00 = loadd(fname);

      //Assign y
      y0 = y00[., 2:9];

      //Percent Change in Y
      y = 100*ln(y0[2:rows(y0), .]./y0[1:rows(y0)-1, .]);

      //Indicator to run test with trend variable
      trend = 1;

      //Indicator to run test with constant
      const = 1;

      //Turn off data demeaning
      demean = 0;

      //Set number of lags to 3
      lags = 3;

      //Compute test statistics
      tstat = breitung(y, trend, const, demean, lags);
      print "The Breitung test statistic = ";; tstat;

Source
------

.. container:: gfunc
   :name: Source

   breitung.src
