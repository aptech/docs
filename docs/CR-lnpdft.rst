
lnpdft
==============================================

Purpose
----------------

Computes Student's t log-probabilities.

Format
----------------
.. function:: z = lnpdft(x, df)

    :param x: values at which to compute the Student's t log-probabilities.
    :type x: NxK matrix

    :param df: degrees of freedom.
    :type df: scalar

    :return z: log-probabilities.

    :rtype z: NxK matrix

Examples
----------------

::

        // Set x
        x = { -2, -1, 0, 1, 2 };

        // Degrees of freedom
        df = 5;

        z = lnpdft(x, df);

::

        -2.73198
        -1.51558
  z =   -0.96862
        -1.51558
        -2.73198 

Remarks
-------

This does not compute the log of the joint Student's t pdf. Instead, the
scalar Normal density function is computed element-by-element.

For multivariate probabilities with covariance matrix see :func:`lnpdfmvt`.

.. seealso:: Functions :func:`lnpdfmvt`
