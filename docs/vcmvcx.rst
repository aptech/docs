
vcm, vcx
==============================================

Purpose
----------------
Computes an estimate of a variance-covariance matrix.

Format
----------------
.. function:: vc = vcm(m [, ddof])
              vc = vcx(x [, ddof])

    :param m: A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (:math:`x'x`) matrix

    :param x: data
    :type x: NxK matrix

    :param ddof: Optional input,  delta degrees of freedom. The divisor
          will be :math:`(N - ddof)`. Default = 1 (sample covariance matrix).
    :type ddof: Scalar

    :return vc: an estimate of the variance-covariance matrix.

    :rtype vc: KxK variance-covariance matrix


Examples
-------------

Compute covariance matrices from a data matrix, :math:`x`.

::

    x = { 2 3, 
          3 0, 
          4 4, 
          1 2 };

    // Compute the sample covariance matrix
    vcs = vcx(x);
 
    // Compute the population covariance matrix
    vcp = vcx(x, 0);

    // Compute the sample covariance matrix
    vcs2 = vcx(x, 1);

After the above code:

::

    vcs  =  1.6666667       0.5000000
            0.5000000       2.9166667

    vcp  =  1.2500000       0.3750000
            0.3750000       2.1875000

    vcs2 =  1.6666667       0.5000000
            0.5000000       2.9166667


Compute covariance matrices from a moment matrix, :math:`x'x`.

::

    // Create matrix with a constant
    x = { 1 2 3, 
          1 3 0, 
          1 4 4, 
          1 1 2 };

    // Compute moment matrix
    m = x'x;

    // Compute the sample covariance matrix
    vcs = vcm(m);
 
    // Compute the population covariance matrix
    vcp = vcm(m, 0);

    // Compute the sample covariance matrix
    vcs2 = vcm(m, 1);

After the above code:

::

    vcs  =  1.6666667       0.5000000
            0.5000000       2.9166667

    vcp  =  1.2500000       0.3750000
            0.3750000       2.1875000

    vcs2 =  1.6666667       0.5000000
            0.5000000       2.9166667



Source
------

corr.src

.. seealso:: Functions :func:`momentd`
