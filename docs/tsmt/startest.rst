starTest
========

Purpose
-------
Estimates a p\ :sup:`th` order threshold autoregression and tests the
hypothesis of a linear autoregression, using the statistics described
in "Inference when a nuisance parameter is not identified under the
null hypothesis." (Hansen, 1996).

Format
------
.. function:: { s3, p3 } = starTest(yt, p, omit)

   :param yt: Nx1 data.
   :type yt: matrix

   :param p: autoregressive order of the TAR model.
   :type p: scalar

   :param omit: lags (below p) to omit from autoregression [0 implies an AR(p)].
   :type omit: scalar or vector

   :return s3: value of the LM test statistic.
   :rtype s3: scalar

   :return p3: p-value of s3.
   :rtype p3: scalar

Example
-------

::

   new;
   cls;
   library tsmt;

   //Real GNP data 
   //Seasonally adjusted and transformed in annualized quarterly growth rates
   gnp = loadd( getGAUSSHome() $+ "pkgs/tsmt/examples/gnp_4790.fmt");
   yg = ln( gnp[., 1] );
   y = (yg[2:rows(yg)]-yg[1:rows(yg)-1])*400;

   //Maximum number of lags considered
   p = 5;

   //Lags to omit from the test
   omit = { 3, 4 };

   {s3, p3} = starTest( y, p, omit );

   //Print results
   print "LM statistic :";; s3;
   print;
   print "P-value :";; p3;

References
----------
#. Hansen, B.E. (1996). Inference when a nuisance parameter is not
   identified under the null hypothesis, Econometrica, 64(2),
   413-430.
#. Franses, P.H. and Dijk, D. (2000) Non-linear Time Series Models in
   Empirical Finance. Cambridge University Press, New York.

Library
-------
tsmt

Source
------
startest.src
