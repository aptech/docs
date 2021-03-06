
moment
==============================================

Purpose
----------------

Computes a cross-product matrix. This is the same as x'x.

Format
----------------
.. function:: y = moment(x, d)

    :param x: data
    :type x: NxK matrix or M-dimensional array where the last two dimensions are NxK

    :param d: controls handling of missing values.

        .. list-table::
            :widths: auto

            * - 0
              - missing values will not be checked for. This is the fastest option.
            * - 1
              - "listwise deletion" is used. Any row that contains a missing value in any of its elements is excluded from the computation of the moment matrix. If every row in *x* contains missing values, then ``moment(x,1)`` will return a scalar zero.
            * - 2
              - "pairwise deletion" is used. Any element of *x* that is missing is excluded from the computation of the moment matrix.  Note that this is seldom a satisfactory method of handling missing values, and special care must be taken in computing the relevant number of observations and degrees of freedom.

    :type d: scalar

    :return y: where the last two dimensions are KxK, the cross-product of *x*.

    :rtype y: KxK matrix or M-dimensional array

Examples
----------------

::

    rndseed 129070;

    // Create data
    x = ones(100, 3)*rndn(100, 3);
    b_true = {1.3 0.5 0.75 -1.9};

    y = x*b_true' + 0.5*rndn(100,3);

    // Create moment matrix
    xx = moment(x, 2);

    // Find inverse of moment matrix
    ixx = invpd(xx);

    // Find coefficients
    b = ixx*missrv(x, 0)'y;

    print "b_true~b_est";
    b_true'~b_est;

::

     1.3000000        1.2808949
     0.50000000       0.49703322
     0.75000000       0.73297298
     -1.9000000       -1.8087071

In this example, the regression of *y* on *x* is
computed. The moment matrix (*xx*) is formed using the
:func:`moment` command (with pairwise deletion, since the
second parameter is 2). Then *xx* is inverted using
the :func:`invpd` function. Finally, the ols coefficients
are computed. :func:`missrv` is used to emulate pairwise
deletion by setting missing values to 0.

Remarks
-------

The fact that the moment matrix is symmetric is taken into account to
cut execution time almost in half.

If *x* is an array, the result will be an array containing the
cross-products of each 2-dimensional array described by the two trailing
dimensions of *x*. In other words, for a 10x4x4 array *x*, the resulting
array *y* will contain the cross-products of each of the 10 4x4 arrays
contained in *x*, so :math:`y[n,.,.]=x[n,.,.]'x[n,.,.]` for :math:`1 <= n <= 10`.

If there is no missing data then d = 0 should be used because it will be
faster.

The ``/`` operator (matrix division) will automatically form a moment matrix
(performing pairwise deletions if ``trap 2`` is set) and will compute
the ols coefficients of a regression. However, it can only be used for
data sets that are small enough to fit into a single matrix. In
addition, the moment matrix and its inverse cannot be recovered if the ``/``
operator is used.


