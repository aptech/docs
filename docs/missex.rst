
missex
==============================================

Purpose
----------------

Converts numeric values to the missing value code according to the values given in a logical
expression.

Format
----------------
.. function:: y = missex(x, mask)

    :param x: data
    :type x: NxK matrix

    :param mask: (matrix of 0's and 1's) that serves as a "mask" for *x*; the 1's in
        mask correspond to the values in *x* that are to be converted into missing values
    :type mask: NxK logical matrix

    :return y: but with those elements that correspond to the 1's in *e* converted to missing.

    :rtype y: NxK matrix that equals x

Examples
----------------

::

    // Set seed for repeatable random numbers
    rndseed 49728424;

    x = rndu(3, 2);

    // Logical expression
    mask =(x .> .30) .and (x .< .60);
    y = missex(x, mask);

After the code above:

::

         0.525  0.419          1  1           .      .
    x =  0.869  0.973   mask = 0  0   y = 0.869  0.973
         0.021  0.357          0  1       0.021      .

A 3x2 matrix of uniform random numbers is created.
All values in the interval (0.30, 0.60) are converted
to missing.

Remarks
-------

The matrix *e* will usually be created by a logical expression. For
instance, to convert all numbers between 10 and 15 in *x* to missing, the
following code could be used:

::

    y = missex(x, (x .> 10) .and (x .< 15));

Note that "dot" operators MUST be used in constructing the logical
expressions.

For complex matrices, the missing value code is defined as a missing
value entry in the real part of the matrix. For complex *x*, then, :func:`missex`
replaces elements with a ". + 0i" value.

This function is like :func:`miss`, but is more general in that a range of
values can be converted into missings.

Source
------

datatran.src

.. seealso:: Functions :func:`miss`, :func:`missrv`
