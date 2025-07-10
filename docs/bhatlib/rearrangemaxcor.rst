rearrangemaxcor
==============================================

Purpose
----------------
Rearranges a vector based on descending correlations among vector elements, specifically prioritizing the first two elements with the highest correlation.

Format
----------------
.. function:: { newa, newc, temp } = rearrangemaxcor(a, c)

    :param a: Column vector (mx1).
    :type a: vector

    :param c: Correlation matrix (mxm).
    :type c: matrix

    :return newa: Vector *a* rearranged based on the procedure, maintaining the same dimension.
    :rtype newa: vector

    :return newc: Correlation matrix *c* rearranged accordingly, maintaining the same dimension.
    :rtype newc: matrix

    :return temp: Vector indicating the indices of the rearranged vector elements in *newa*, maintaining the same dimension as *a*.
    :rtype temp: vector

Note
----------------
This procedure prioritizes rearranging the first two elements of *a* with the highest correlation, positioning the element with a higher absolute correlation with other elements first in *newa*. The rearrangement of *a* and *c* ensures all elements are retained but does not specifically order elements beyond the first two.

Example
----------------

Given a column vector `a` and a correlation matrix `c`:

::

    a = { 0.1, 0.2, 0.3, 0.4 };
    c = { 1.0  0.3  0.4  -0.25,
          0.3  1.0  0.1   0.4,
          0.4  0.1  1.0   0.5,
         -0.25 0.4  0.5   1.0 };

Applying `rearrangemaxcor` to rearrange `a` and `c`:

::

    { newa, newc, temp } = rearrangemaxcor(a, c);

Results in `newa`, `newc`, and `temp`:

::

    newa = { 0.4, 0.3, 0.1, 0.2 };
    newc = { 1.0  0.5  -0.25  0.4,
              0.5  1.0   0.4   0.1,
             -0.25 0.4   1.0   0.3,
              0.4  0.1   0.3   1.0 };
    temp = { 4, 3, 1, 2 };

This outcome demonstrates that `newa` and `newc` are rearranged to prioritize the elements of `a` (0.4 and 0.3 in this example) with the highest correlation, followed by the remaining elements without a specific order, as indicated by `temp`.

.. seealso:: :func:`rearrangemincor`

