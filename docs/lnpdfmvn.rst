
lnpdfmvn
==============================================

Purpose
----------------

Computes multivariate Normal log-probabilities.

Format
----------------
.. function:: z = lnpdfmvn(x, corr)

    :param x: values at which to evaluate the multivariate normal log probabilities.
    :type x: NxK matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :return z: log-probabilities.

    :rtype z: Nx1 vector

Examples
----------------

Uncorrelated variables
++++++++++++++++++++++

::

      // Correlation matrix
      corr = { 1 0 , 0 1 };

      // X values
      x1 = seqa(-3, .2, 3/.2);
      x2 = seqa(-3, .2, 3/.2);
      x = x1~x2;

      z = lnpdfmvn(x, corr);

      print "z =";
      z;

::

      z =    -10.83788
             -9.67788
             -8.59788
             -7.59788
             -6.67788
             -5.83788
             -5.07788
             -4.39788
             -3.79788
             -3.27788
             -2.83788
             -2.47788
             -2.19788
             -1.99788
             -1.87788

Example 2
++++++++++++++

::

      // Correlation matrix
      corr = { 1 0.60 , 0.60 1 };

      // X values
      x1 = seqa(-3, .2, 3/.2);
      x2 = seqa(-3, .2, 3/.2);
      x = x1~x2;

      z = lnpdfmvn(x, corr);

      print "z =";
      z;

After the above code:

::

       z =     -7.23973
               -6.51473
               -5.83973
               -5.21473
               -4.63973
               -4.11473
               -3.63973
               -3.21473
               -2.83973
               -2.51473
               -2.23973
               -2.01473
               -1.83973
               -1.71473
               -1.63973



Remarks
-------

This computes the multivariate Normal log-probability for each row of *x*.

Source
------

lnpdfn.src
