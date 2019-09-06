
movingaveExpwgt
==============================================

Purpose
----------------

Computes exponentially weighted moving average of a series.

Format
----------------
.. function:: y = movingaveExpwgt(x, d, p)

    :param x: data
    :type x: NxK matrix

    :param d: order of moving average.
    :type d: scalar

    :param p: smoothing coefficient where :math:`0 > p > 1`.
    :type p: scalar

    :return y: filtered series. The first :math:`d-1` rows of *x* are set to missing values.

    :rtype y: NxK matrix

Examples
------------

Smoothing of random walk data
+++++++++++++++++++++++++++++

::

      // Create random data, setting initial seed
      // value to be the hundredths of a second
      // since midnight
      numPoints = 1000;
      seed = hsec;
      { delta, state } = rndn(numPoints, 1, seed);

      // Set mean of data to be > 0
      // to give data long term positive bias
      delta = delta + 0.01;

      // Increase magnitude of delta to
      // create desired level of volatiliy
      delta = 2*delta;

      // Instantiate y : index price data
      y = 1000*ones(numPoints,1);

      // Loop through y and add the cumulative
      // sums of delta to create random walk
      for i(2, numPoints, 1);
      	y[i]= y[i-1] + delta[i];
      endfor;

      // Find moving averag
      twentyMA = movingaveExpwgt(y, 20, 0.8);

Remarks
-------

:func:`movingaveExpwgt` is smoothing time series filter using exponential
weights. The moving average as performed by column and thus it treats
the NxK matrix as *K* time series of length *N*.

.. seealso:: Functions :func:`movingaveWgt`, :func:`movingave`
