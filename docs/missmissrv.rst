
miss, missrv
==============================================

Purpose
----------------

:func:`miss` creates a scalar missing value or converts specified elements in a matrix to GAUSS's missing
value code. :func:`missrv` is the reverse of this, and converts missing values into specified values.

Format
----------------
.. function:: y = missrv(x, v)
              y = miss(x, v)
              y = miss()

    :param x: data
    :type x: NxK matrix

    :param v: ExE conformable with *x*.
    :type v: LxM matrix

    :return y: matrix with missing values either replaced or added.

    :rtype y: max(N,L) by max(K,M) matrix

Examples
----------------

Create a scalar missing value
+++++++++++++++++++++++++++++++

::

    // Create a scalar missing value
    m = miss();
    print m;

After the above code, ``m`` will be a scalar missing value and the code will print the following:

::

    .


Replace missing values
++++++++++++++++++++++

::

    // Create a 4x3 matrix with missing values
    x = { 1  .  3,
          .  5  .,
          7  8  .,
          . 10 11 };

    // Replace all missing values with 0.
    x_2 = missrv(x, 0);


    // Create a 1x3 row vector.
    replace = { -1 -2 -3 };

    // Replace missing values with the element
    // in the corresponding column of 'replace'
    x_3 = missrv(x, replace);

After the code above:

::

            1    0    3
    x_2 =   0    5    0
            7    8    0
            0   10   11

            1   -2    3
    x_3 =  -1    5   -3
            7    8   -3
           -1   10   11

Replace specific numbers with missing values
++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a 4x3 matrix
    x = { 1  2  3,
          4  5  6,
          7  8  4,
          4 10 11 };

    // Replace all instances of 4 with a missing value.
    x_2 = miss(x, 4);


    // Create a 1x3 row vector.
    replace = { 4 5 6 };

    // Replace all instances of 4 in the first column,
    // 5 in the second column and 6 in the third with a missing.
    x_3 = miss(x, replace);

After the code above:

::

            1    2    3
    x_2 =   .    5    6
            7    8    .
            .   10   11

            1    2    3
    x_3 =   .    .    .
            7    8    4
            .   10   11

Example 3
+++++++++

::

    // Create a 3x3 matrix with each element equal to 1
    x = ones(3, 3);

    // Assign the diagonal of 'x' to be equal to pi
    x = diagrv(x, pi);

    print "x = " x;

    // Change all 1's in 'x' into missing values and assign to
    // xmiss
    xmiss = miss(x, 1);

    print "xmiss = " xmiss;

    // Change all missings in 'xmiss' into 2*pi and assign to x2
    x2 = missrv(xmiss, 2*pi);

    print "x2 = " x2;

The code above, will return:

::

    x =
           3.1415927        1.0000000        1.0000000
           1.0000000        3.1415927        1.0000000
           1.0000000        1.0000000        3.1415927
    xmiss =
           3.1415927                .                .
                   .        3.1415927                .
                   .                .        3.1415927
    x2 =
           3.1415927        6.2831853        6.2831853
           6.2831853        3.1415927        6.2831853
           6.2831853        6.2831853        3.1415927

Remarks
-------

For :func:`miss`, elements in *x* that are equal to the corresponding elements in
*v* will be replaced with the GAUSS missing value code.

For :func:`missrv`, elements in *x* that are equal to the GAUSS missing value code
will be replaced with the corresponding element of *v*.

For complex matrices, the missing value code is defined as a missing
value entry in the real part of the matrix. For complex *x*, then, :func:`miss`
replaces elements with a ". + 0i" value, and :func:`missrv` examines only the
real part of *x* for missing values. If, for example, an element of :math:`x = 1 + .i`,
:func:`missrv` will not replace it.

These functions act like element-by-element operators. If *v* is a scalar,
for instance -1, then all -1's in *x* are converted to missing. If *v* is a
row (column) vector with the same number of columns (rows) as *x*, then
each column (row) in *x* is transformed to missings according to the
corresponding element in *v*. If *v* is a matrix of the same size as *x*, then
the transformation is done corresponding element by corresponding
element.

Missing values are given special treatment in the following functions
and operators: :math:`b/A` (matrix division when *a* is not square and neither *a*
nor *b* is scalar), :func:`counts`, :func:`scalmiss`, :func:`maxc`, :func:`maxindc`,
:func:`minc`, :func:`minindc`, :func:`miss`, :func:`missex`, :func:`missrv`,
:func:`moment`, :func:`packr`, :func:`scalmiss`, :func:`sortc`.

As long as you know a matrix contains no missings to begin with, :func:`miss`
and :func:`missrv` can be used to convert one set of numbers into another. For
example:

::

   y = missrv(miss(x, 0), 1);

will convert 0's to 1's.

To convert a range of values, such as:

.. math::

   0.5 < x < 1.3

into missing values, use the :func:`missex` function.

.. seealso:: Functions :func:`counts`, :func:`impute`, :func:`ismiss`, :func:`missex`, :func:`packr`, :func:`scalmiss`
