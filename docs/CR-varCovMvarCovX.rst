
varCovM, varCovX
==============================================

Purpose
----------------
Computes the population variance-covariance matrix.

Format
----------------
.. function:: varCovM(mm) 
			  varCovX(x)

    :param mm: KxK moment (x'x) matrix. A constant term MUST have been the first variable when the moment matrix was computed.
    :type mm: TODO

    :param x: NxK matrix of data.
    :type x: TODO

    :returns: vc (*TODO*), KxK variance-covariance matrix.

Examples
----------------

::

    //Set rndseed for repeatable random numbers
    rndseed 7234242;
    
    //Create three randomly generated independent variables
    x = rndn(500, 3);
    
    //Create the population variance-covariance matrix from data matrix 'x'
    var_x = varCovX(x);

After the code above, var_x will be equal to:

::

    1.0941806   0.0040829  -0.0024871
       0.0040829   1.0606611   0.0493555
      -0.0024871   0.0493555   0.8729622

where the diagonal elements in the matrix represent the population variance of the each column, while the off-diagonal elements represent the population covariance between the data columns.
The population variance can also be calculated using the moment matrix, x’x and the GAUSS function varCovM. A constant term must be included in the data matrix x when computing the moment equation. Consider the following data matrix x1, consisting of the original data matrix x and a column of ones:

::

    //Set rndseed so 'rndn' will return the same numbers as above
    rndseed 7234242;
    
    //Note: the ~ operator performs horizontal concatenation
    x1 = ones(500,1)~rndn(500,3);
    
    //Create moment matrix
    x2 = x1'x1;
    
    //Calculate variance-covariance matrix using the moment matrix
    var_xm = varCovM(x2);

After the code above, var_xm will be equal to:

::

    1.0941806   0.0040829  -0.0024871
       0.0040829   1.0606611   0.0493555
      -0.0024871   0.0493555   0.8729622

Remarks
+++++++

The variance covariance matrix is that of the population data matrix. It
is computed as the moment matrix of deviations about the mean divided by
the number of observations N. For a sample covariance matrix which uses
N - 1 rather than N see varCovMS or varCovXS.

Source
++++++

corrs.src

.. seealso:: Functions :func:`momentd`, :func:`corrms`, :func:`corrxs`, :func:`corrm`, :func:`corrvc`, :func:`corrx`

population variance covariance matrix moment data
