
lnpdfmvt
==============================================

Purpose
----------------

Computes multivariate Student's t log-probabilities.

Format
----------------
.. function:: z = lnpdfmvt(x, corr, df)

    :param x: values at which to evaluate the multivariate Student's t log-probabilities.
    :type x: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :param df: degrees of freedom.
    :type df: scalar

    :return z: log-probabilities.

    :rtype z: Nx1 vector

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

  // Correlation matrix
  corr = { 1 0 , 0 1 };

  // Degrees of freedom
  df = 5;

  // X values
  x1 = seqa(-3, .2, 3/.2);
  x2 = seqa(-3, .2, 3/.2);
  x = x1~x2;

  t = lnpdfmvt(x, corr, df);

  print "t =";
  t;

::

  t =    -7.17907
         -6.80693
         -6.42082
         -6.02085
         -5.60755
         -5.18217
         -4.74697
         -4.30564
         -3.86388
         -3.42999
         -3.01553
         -2.63564
         -2.30874
         -2.05500
         -1.89343

Example 2
++++++++++++++

::

  // Correlation matrix
  corr = { 1 0.60 , 0.60 1 };

  // Degrees of freedom
  df = 5;

  // X values
  x1 = seqa(-3, .2, 3/.2);
  x2 = seqa(-3, .2, 3/.2);
  x = x1~x2;

  t = lnpdfmvt(x, corr, df);

  print "t =";
  t;

After the above code:

::

   t =   -5.74003
         -5.41290
         -5.07813
         -4.73673
         -4.39021
         -4.04075
         -3.69138
         -3.34617
         -3.01045
         -2.69093
         -2.39574
         -2.13420
         -1.91636
         -1.75201
         -1.64956


Source
------

lnpdfn.src

.. seealso:: Functions :func:`lnpdft`
