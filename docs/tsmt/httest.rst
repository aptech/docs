======
htTest
======

10.0.25htTest
=============

Purpose
-------

.. container::
   :name: Purpose

   Perform the Harris–Tzavalis panel series unit root testing. The z
   statistics constructed from the mean t-statistic has an asymptotic
   standardized normal distribution and tests the null hypothesis that
   all series are I(1) against the alternative that all series are I(0).

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   {Z, z_infinite_t} = htTest(y, model);

Input
-----

.. container::
   :name: Input

   +-------+-------------------------------------------------------------+
   | y     | TxM matrix, data, M > 5.                                    |
   +-------+-------------------------------------------------------------+
   | model | Scalar, indicates which test to run: 1 for homogenous no    |
   |       | mean, 2 for heterogenous, fixed effect, 3 heterogenous,     |
   |       | fixed effect and time trend.                                |
   +-------+-------------------------------------------------------------+

Output
------

.. container::
   :name: Output

   ============ ========================
   Z            Small, t test statistic.
   Z_infinite_t Large, t test statistic.
   ============ ========================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Load cobb douglas production function data set
      y = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/production_cobb.dat");

      //Run test using model one for data with no mean
      {z , zInf} = htTest(y , 1 );

      //Run HT test for model two for data with fixed effects
      {z, zInf} = htTest(y , 2);

      //Run HT test for model three for data with fixed effects
      //and time trend
      {z, zInf} = htTest(y , 3);

Source
------

.. container:: gfunc
   :name: Source

   htTest.src
