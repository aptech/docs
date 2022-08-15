======
vmppmt
======

10.0.71vmppmt
=============

Purpose
-------
Returns Phillips-Perron unit root test statistics and critical
   values.

Library
-------
tsmt

Format
------
{ ppb, ppt, pptcrit } = vmppmt( y, p, nwtrunc );

Input
-----
+---------+-----------------------------------------------------------+
   | y       | Tx1 vector, a time series.                                |
   +---------+-----------------------------------------------------------+
   | p       | scalar, order of the time-polynomial to include in the    |
   |         | regression. Set *p* = -1 for no deterministic part,       |
   |         | *p* = 0 for a constant term, and *p* = 1 for a constant   |
   |         | with trend.                                               |
   +---------+-----------------------------------------------------------+
   | nwtrunc | scalar, the number of autocorrelations to use in          |
   |         | calculating the Newey-West correction (*q* in the Remarks |
   |         | section below). If *nwtrunc* = 0, GAUSS will use a        |
   |         | truncation lag given by Newey and West, |image3|          |
   +---------+-----------------------------------------------------------+

Output
------
+---------+-----------------------------------------------------------+
   | ppb     | scalar, estimate of the autoregressive parameter, the *p* |
   |         | coefficient below.                                        |
   +---------+-----------------------------------------------------------+
   | ppt     | scalar, the adjusted t-statistic for testing: |image6|.   |
   +---------+-----------------------------------------------------------+
   | pptcrit | 6x1 vector of critical values, vector of critical values  |
   |         | for the adjusted t-statistic, in the order 1%,  5%,       |
   |         | 10%,  90%,  95%,  99%.                                    |
   +---------+-----------------------------------------------------------+

Remarks
-------
Phillips (1987) and Phillips and Perron (1988) test for unit roots by
   adjusting the OLS estimate of an *AR(1)* coefficient for serial
   correlation in the OLS residuals. Three specifications are
   considered, an *AR(1)* model without a drift, an *AR(1)* with a
   drift, and an *AR(1)* model with a drift and linear trend:

   .. image:: _static/images/Equation716.svg
:class: mcReset

   .. image:: _static/images/Equation717.svg
:class: mcReset

   .. image:: _static/images/Equation718.svg
:class: mcReset

   The unit root null hypothesis is

   .. image:: _static/images/Equation719.svg
:class: mcReset

   Hamilton (1994, pp. 506-511) tests this hypothesis using two
   statistics that are analogs of the Phillips and Perron (1988)
   |image7| and |image8| statistics. Hamilton’s statistics are based on
   OLS estimation of the above equations. They allow an identical
   formula for each statistic to be used for all three cases.

   The vmppmt procedure returns the |image9| statistic as calculated by
   Hamilton and critical values. Suppose any of the equations are
   estimated by OLS, returning |image10| and |image11| (the OLS
   estimates of |image12| and the standard error of |image13|,
   respectively), (the usual OLS t statistic for testing |image14|),
   |image15| (the OLS residuals), and |image16| (the estimated standard
   error of the regression).

   Hamilton's\ |image17| statistic is:

   .. image:: _static/images/Equation731.svg
:class: mcReset

   |image18|\ is an estimate of the asymptotic variance of the sample
   mean of |image19|. In the vmppmt procedure |image20| is estimated
   using the Newey-West (1987) estimator:

   .. image:: _static/images/Equation735.svg
:class: mcReset

   where

   .. image:: _static/images/Equation736.svg
:class: mcReset

   are the sample autocovariances of |image21|.

   The nwtrunc argument sets the number of autocorrelations to use in
   calculating the Newey-West correction (*q* in the above equation). If
   nwtrunc = 0, GAUSS will use a truncation lag given by Newey and West,

   .. image:: _static/images/Equation738.svg
:class: mcReset

   Under the null hypothesis, the |image22| statistics has the same
   asymptotic distribution as a Dickey-Fuller statistic.

References
----------
#. Hamilton, James D., (1994). Time Series Analysis, Princeton
University Press.

   #. Newey, W.K. and West, K.D., (1987), “A Simple Positive
Semi-Definite Heteroskedasticity and Autocorrelation-Consistent
Covariance Matrix,” Econometrica, 55, 703-708.
::

new;
cls;
library tsmt;

// Load data
airline = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/airline.dat");

// Transform data
y = airline;

// Use trend in test
p = 1;

// Number lags
lags = 4;

// Run test
{ ppb, ppt, pptcrit } = vmppmt(y, p, lags);

print "Estimated autoregressive parameter : ";; ppb;
print;
print "T-stat on autoregressive parameter : ";; ppt;
print;
print "Critical values : ";
pptcrit';

Source
------
varmamt.src

.. |image1| image:: _static/images/Equation714.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image2| image:: _static/images/Equation714.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image3| image:: _static/images/Equation714.svg
   :class: _inline_math_MCEquation_0 mcReset
.. |image4| image:: _static/images/Equation715.svg
   :class: mcReset
.. |image5| image:: _static/images/Equation715.svg
   :class: mcReset
.. |image6| image:: _static/images/Equation715.svg
   :class: mcReset
.. |image7| image:: _static/images/Equation720.svg
   :class: mcReset
.. |image8| image:: _static/images/Equation721.svg
   :class: mcReset
.. |image9| image:: _static/images/Equation722.svg
   :class: mcReset
.. |image10| image:: _static/images/Equation723.svg
   :class: mcReset
.. |image11| image:: _static/images/Equation724.svg
   :class: mcReset
.. |image12| image:: _static/images/Equation725.svg
   :class: mcReset
.. |image13| image:: _static/images/Equation726.svg
   :class: mcReset
.. |image14| image:: _static/images/Equation727.svg
   :class: mcReset
.. |image15| image:: _static/images/Equation728.svg
   :class: mcReset
.. |image16| image:: _static/images/Equation729.svg
   :class: mcReset
.. |image17| image:: _static/images/Equation730.svg
   :class: mcReset
.. |image18| image:: _static/images/Equation732.svg
   :class: mcReset
.. |image19| image:: _static/images/Equation733.svg
   :class: mcReset
.. |image20| image:: _static/images/Equation734.svg
   :class: mcReset
.. |image21| image:: _static/images/Equation737.svg
   :class: mcReset
.. |image22| image:: _static/images/Equation739.svg
   :class: mcReset
