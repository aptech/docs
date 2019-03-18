
moment
==============================================

Purpose
----------------

Computes a cross-product matrix. This is the same as x'x.

Format
----------------
.. function:: moment(x,  d)

    :param x: NxK matrix or M-dimensional array where  the last two dimensions are NxK.
    :type x: TODO

    :param d: controls handling of missing values.
    :type d: scalar

    .. csv-table::
        :widths: auto

        "0", "missing values will not be checked for. This is the fastest option."
        "1", ""listwise deletion" is used. Any row that contains a missing value in any of its elements is excluded from the computation of the moment matrix. If every row in x contains missing values, then moment(x,1) will return a scalar zero."
        "2", ""pairwise deletion" is used. Any element of x that is missing is excluded from the computation of the moment matrix.  Note that this is seldom a satisfactory method of handling missing values, and special care must be taken in  computing the relevant number of observations and degrees of freedom."

    :returns: y (*TODO*), KxK matrix or M-dimensional array where the last two dimensions are KxK, the cross-product of x.

Examples
----------------

::

    xx = moment(x,2);
    ixx = invpd(xx);
    b = ixx*missrv(x,0)'y;

In this example, the regression of y on x is
computed. The moment matrix (xx) is formed using the
moment command (with pairwise deletion, since the
second parameter is 2). Then xx is inverted using
the invpd function. Finally, the ols coefficients
are computed.  missrv is used to emulate pairwise
deletion by setting missing values to 0.

cross product moment matrix x'x missing value
