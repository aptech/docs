kpss
====

Purpose
-------
Test for stationarity using a Lagrange Multiplier score statistic.

Format
------
.. function:: { tstat, crit } = kpss(y, max_lags[, trend, qsk, auto, print_out])

   :param y: data.
   :type y: Nx1 vector

   :param max_lags: Optional input, if max_lags <= 0, maximum lag set using Schwert criterion; if -1, Schwert criterion = 12; if 0, Schwert criterion = 4; else if max_lags > 0, maximum lag = max_lags. Default = 0.
   :type max_lags: scalar

   :param trend: Optional input, 0 no trend, 1 trend. Default = 0.
   :type trend: scalar

   :param qsk: Optional input, if nonzero, quadratic spectral kernel is used. Default = 0.
   :type qsk: scalar

   :param auto: Optional input, if nonzero, automatic maxlags computed. Default = 1.
   :type auto: scalar

   :param print_out: Optional input, if nonzero, intermediate quantities printed to the screen. Default = 1.
   :type print_out: scalar

   :return tstat: test statistic for each lag.
   :rtype tstat: matrix

   :return crit: Elliot, Rothenberg and Stock (1996) critical values for the GLS detrended unit root test at the 1%, 2.5%, 5%, and 10% significance level.
   :rtype crit: matrix

Example
-------
::

   new;
   cls;
   library tsmt;

   // Load data
   npdb = loadd( getGAUSSHome("pkgs/tsmt/examples/nelsonplosser.gdat") );
   yt = packr(npdb[., "lrgnp"]);

   // Test using basic KPSS testing: Trend stationary
   // Step One: Set-up testing parameters
   // Maximum lags to include
   max_lags = 5;

   // Include trend
   trend = 1;

   // Use quadratic spectral kernel
   qsk = 1;

   // Automatic maxlag computation
   auto = 1;

   // Print results to screen
   print_out = 1;

   // Running KPSS test
   { mat, crit } = kpss(yt, max_lags, trend, qsk, auto, print_out);

   print "The tstats for all possible lags:";
   mat;

   print "Critical values:";
   crit;

  
Library
-------
tsmt

Source
------
kpss.src
