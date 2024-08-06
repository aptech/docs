htTest
======

Purpose
-------
Perform the Harris–Tzavalis panel series unit root testing. The z
statistics constructed from the mean t-statistic has an asymptotic
standardized normal distribution and tests the null hypothesis that
all series are I(1) against the alternative that all series are I(0).

Format
------

.. function:: {Z, z_infinite_t} = htTest(y, model)

   :param y: TxM matrix, data, M > 5.
   :type y: Matrix

   :param model: Scalar, indicates which test to run: 1 for homogeneous no mean, 2 for heterogeneous, fixed effect, 3 heterogeneous, fixed effect and time trend.
   :type model: Scalar

   :return Z: Small, t test statistic.
   :rtype Z: Scalar

   :return z_infinite_t: Large, t test statistic.
   :rtype z_infinite_t: Scalar

Example
-------

Example One: Data without mean 
+++++++++++++++++++++++++++++++

::

   new;
   cls;
   library tsmt;

   // Load cobb douglas production function data set
   y = loadd(getGAUSSHome("pkgs/tsmt/examples/production_cobb.dat"));

   // Run test using model one for data with no mean
   { z, zInf } = htTest(y, 1);

This prints the following report:

:: 

   Test:                             Harris and Tzavalis (1999) 
   Test Variable:                                             Y 
   Timespan:                                            Unknown 
   Ho:                                                Unit Root 
   Model:                                 Homogenous, Zero Mean 
   N. Obs:                                                   16 
   N. Groups:                                                48 
   Panel Type:                                         Balanced 
   ============================================================

   Z                                                      0.208 
   Z-infinite                                             0.215 
   ============================================================

   Cannot reject the null hypothesis of finite t case with unit root.
   Cannot reject the null hypothesis of infinite t case with unit root.

Example Two: Data with fixed effects 
++++++++++++++++++++++++++++++++++++
This example works with the same data as example one but includes fixed effects. 

::

   // Run HT test for model two for data with fixed effects
   { z_fe, zInf_fe } = htTest(y, 2);

This prints an updated report:

::
   
   Test:                             Harris and Tzavalis (1999) 
   Test Variable:                                             Y 
   Timespan:                                            Unknown 
   Ho:                                                Unit Root 
   Model:                            Heterogenous, Fixed Effect 
   N. Obs:                                                   16 
   N. Groups:                                                48 
   Panel Type:                                         Balanced 
   ============================================================

   Z                                                      6.328 
   Z-infinite                                             6.138 
   ============================================================

Library
-------
tsmt

Source
------
htTest.src

.. seealso:: Functions :func:`vmadfmt`, :func:`vmppmt`, :func:`kpss`, :func:`ips`
