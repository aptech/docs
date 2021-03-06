
varCovMS, varCovXS
==============================================

Purpose
----------------
Computes a sample variance-covariance matrix.

Format
----------------
.. function:: vc = varCovMS(mm)
              vc = varCovXS(x)

    :param mm: A constant term MUST have been the first variable when the moment matrix was computed.
    :type mm: KxK moment (:math:`x'x`) matrix

    :param x: data
    :type x: NxK matrix

    :return vc: sample variance-covariance computed from *mn* or *x*.

    :rtype vc: KxK variance-covariance matrix

Examples
----------------

::

    // Set rndseed for repeatable random numbers
    rndseed 7234242;

    // Create three randomly generated independent variables
    x = rndn(500, 3);

    // Create the sample variance-covariance matrix from data matrix 'x'
    var_x = varCovXS(x);

After the code above, ``var_x`` will be equal to:

::

       1.0963733   0.0040911  -0.0024921
       0.0040911   1.0627867   0.0494544
      -0.0024921   0.0494544   0.8747116

where the diagonal elements in the matrix represent the sample variance of the each
column, while the off-diagonal elements represent the sample covariance between the
data columns.

The sample variance can also be calculated using the moment matrix, :math:`x'x` and the GAUSS
function :func:`varCovMS`. A constant term must be included in the data matrix ``x`` when
computing the moment equation. Consider the following data matrix ``x1``, consisting of the
original data matrix ``x`` and a column of ones:

::

    // Set rndseed so 'rndn' will return the same numbers as above
    rndseed 7234242;

    // Note: the ~ operator performs horizontal concatenation
    x1 = ones(500, 1)~rndn(500, 3);

    // Create moment matrix
    x2 = x1'x1;

    // Calculate variance-covariance matrix using the moment matrix
    var_xm = varCovMS(x2);

After the code above, ``var_xm`` will be equal to:

::

       1.0963733   0.0040911  -0.0024921
       0.0040911   1.0627867   0.0494544
      -0.0024921   0.0494544   0.8747116

Remarks
-------

The variance covariance matrix is that of the sample data matrix. It is
computed as the moment matrix of deviations about the mean divided by
the number of observations minus one, :math:`N - 1`. For a population covariance
matrix which uses :math:`N` rather than :math:`N - 1` see :func:`varCovM` or :func:`varCovX`.

Source
------

corrs.src

.. seealso:: Functions :func:`momentd`, :func:`corrms`, :func:`corrxs`, :func:`corrm`, :func:`corrvc`, :func:`corrx`
