
lnpdfn
==============================================

Purpose
----------------

Computes standard Normal log-probabilities.

Format
----------------
.. function:: z = lnpdfn(x)

    :param x: values at which to compute the normal log probabilities.
    :type x: NxK matrix or N-dimensional array

    :return z: log-probabilities.

    :rtype z: NxK matrix or N-dimensional array

Remarks
-------

This computes the log of the scalar Normal density function for each
element of *x*. *z* could be computed by the following GAUSS code:

::

   z = -ln(sqrt(2*pi))-x .* x / 2;

For multivariate log-probabilities, see :func:`lnpdfmvn`.


Examples
----------------

::

    x = { -2, -1, 0, 1, 2 };
    z = lnpdfn(x);

::

        -2.9189385
        -1.4189385
    z = -0.9189385
        -1.4189385
        -2.9189385
