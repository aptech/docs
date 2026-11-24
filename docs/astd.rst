
astd
==============================================

Purpose
----------------
Computes the standard deviation of the elements across one dimension of an N-dimensional array.

Format
----------------
.. function:: y = astd(x, dim[, divisor="sample"])

    :param x:
    :type x: N-dimensional array

    :param dim: number of dimension to sum across.
    :type dim: scalar

    :param divisor: Optional string, ``"sample"`` (the default) divides by N-1;
        ``"population"`` divides by N. Other values are errors.
    :type divisor: string

    :return y: standard deviation across specified dimension of *x*.

    :rtype y: N-dimensional array

Examples
----------------

Keyword arguments
+++++++++++++++++

Arguments can be named to make their meaning clear::

    y = astd(areshape({1,2,3,4}, 4|1), dim=2, divisor="population");

Omitting ``divisor`` keeps the sample standard deviation.
Positional arguments must come before named arguments. An argument cannot
be supplied twice, and unknown keyword names are errors.


::

    /*
    ** Create a 1e6x1 vector of random normal numbers with a
    ** standard deviation of 25 and reshape it into a
    ** 2e5x3x2 array
    */
    rndseed 456;
    a = areshape(25*rndn(2e6, 1), 2e5|3|2);
    y = astd(a, 3);

The code above should produce a 3x2 matrix with all elements close to 25 similar to what we see below.

::

    25.070091        24.994774
    24.988263        24.990370
    24.956467        24.987882

Remarks
-------

The output *y*, will have the same sizes of dimensions as *x*, except that
the dimension indicated by *dim* will be collapsed to 1.

By default, for each column this function computes sample standard
deviation, *s*:

.. math:: s = \sqrt{\frac{1}{n−1⁢}×\Sigma_{i=1}^n(X_i − \bar{X})^2}

Thus, the divisor is *N-1* rather than *N*, where *N* is the number of
elements being summed. See :func:`astds` for the alternate definition.

.. seealso:: Functions :func:`astds`, :func:`stdc`
