gradpdfcdfmvlogit
==============================================

Purpose
----------------

Computes the non-standard partial cumulative multivariate logistic distribution function. 

Format
----------------
.. function:: { ga, gb } = gradpdfcdfmvlogit(a, b)


    :param a: (K1xQ) matrix of abscissae for equality conditions, where:
    :type a: (Specify type)
    :param b: (K2xQ) matrix of abscissae representing truncation from above, where:
    :type b: (Specify type)

    :return ga: (K1xQ) matrix of gradients for abscissae for equality conditions.
    :rtype ga: (Specify type)
    :return gb: (K2xQ) matrix of gradients for abscissae representing truncation from above.
    :rtype gb: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
