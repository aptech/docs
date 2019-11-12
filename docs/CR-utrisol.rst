
utrisol
==============================================

Purpose
----------------

Computes the solution of :math:`Ux = b` where :math:`U` is an upper triangular matrix.

Format
----------------
.. function:: x = utrisol(b, U)

    :param b: data
    :type b: PxK matrix

    :param U: data
    :type U: PxP upper triangular matrix

    :return x: solution of :math:`Ux = b`.

    :rtype x: PxK matrix

Example
----------

::

    // Create upper triangular matrix
    U = { 9.8    -0.32     0.66       1.28,
            0     9.32    -0.25    -0.0084,
            0        0     8.37       0.54,
            0        0        0      10.17 };
    
    b = { -0.7, 
           1.5,
          -0.8,
        -0.003 };
    
    // Solve the system of equations
    x = utrisol(b, U);

    b_pred = U * x;

The above code will make the following assignments:

::

    x = -0.0597827 
          0.158381 
        -0.0955604 
      -0.000294985

   b_pred = -0.7 
             1.5 
            -0.8 
          -0.003

Remarks
-------

:func:`utrisol` applies a back solve to :math:`Ux = b` to solve for :math:`x`. If :math:`b` has more
than one column, each column is solved for separately, i.e., :func:`utrisol` applies a back solve to :math:`U * x[., i] = b[., i]`.

.. seealso:: Functions :func:`ltrisol`, :func:`solpd`
