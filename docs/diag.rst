
diag
==============================================

Purpose
----------------

Creates a column vector from the diagonal of a matrix.

Format
----------------
.. function:: y = diag(x)

    :param x: Data matrix.
    :type x: NxK matrix or LxNxK array

    :return y: The diagonal of the *x* matrix where the last two dimensions are min(N,K)x1.

    :rtype y: min(N,K)x1 vector or L-dimensional array

Examples
----------------

Get the diagonal from a matrix.
+++++++++++++++++++++++++++++++++++++++++++++
::

    // Set rng seed for reproducibility
    rndseed 458716;

    // Create random matrix
    x = rndu(3, 3);

    // Take diagonal of y
    y = diag(x);

    // Print results
    print "x = " x;
    print "y = " y;

After the above code,

::

    x =
    0.96748215 0.31791692 0.46520760
    0.04558545 0.78613263 0.20528802
    0.73825699 0.30528745 0.73350290

    y =
    0.96748215
    0.78613263
    0.73350290

Using :func:`diag` function for a 2x4x4 dimensional array.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    // Create random matrix
    x = rndn(32, 1);

    // Reshape the 32x1 vector into a 2x4x4 dimensional array
    x = areshape(x, 2|4|4);
    d = diag(x);

Now *x* is equal to:

::

    Plane [1,.,.]

          1.0305361       -1.5803315       0.31002373      -0.99371013
         -1.3967459       0.79842593       0.57613617        1.0063836
        -0.22636263       0.89422800      0.089845674       0.56126503
          1.1532259        1.1146830       0.60477874     -0.035759847

     Plane [2,.,.]

          1.1957213      -0.57905631      -0.75646146     -0.068990606
          1.5065762       0.43443580     -0.033498917       -1.5231533
          1.1028613       -2.0432636       -1.0517457      0.021677957
         -1.0861596      -0.76471535      -0.60429045       0.49674694

and *d* is a 2x4x1 array containing the diagonals from *x* above.

::

    Plane [1,.,.]

          1.0305361
         0.79842593
        0.089845674
       -0.035759847

    Plane [2,.,.]

          1.1957213
         0.43443580
         -1.0517457
         0.49674694


Remarks
-------

If *x* is a matrix, it need not be square. Otherwise, if *x* is an array,
the last two dimensions need not be equal.

If *x* is an array, the result will be an array containing the diagonals
of each 2-dimensional array described by the two trailing dimensions of
*x*. For example, for a 10x4x4 array, the result will be a 10x4x1 array
containing the diagonals of each of the 10 4x4 arrays contained in *x*.

:func:`diagrv` reverses the procedure and puts a vector into the diagonal of a
matrix.


.. seealso:: Functions :func:`diagrv`
