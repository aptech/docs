
factorial
==============================================

Purpose
----------------

Computes the factorial of a number.

Format
----------------

::

    y = n!

Parameters
----------------

    :param n: Input value (truncated to integer).
    :type n: scalar, vector, or matrix

Returns
----------------

    :return y: Factorial of each element, n! = n * (n-1) * (n-2) * ... * 1.

    :rtype y: same dimensions as input

Examples
----------------

::

    y = 5!;

::

    y =    120.00000

::

    x = { 0, 1, 2, 3, 4, 5 };
    y = x!;

::

    y =    1.0000000
           1.0000000
           2.0000000
           6.0000000
          24.0000000
         120.0000000

In Expressions
++++++++++++++

::

    // Combinations: n choose k = n! / (k! * (n-k)!)
    n = 5;
    k = 2;
    combinations = n! / (k! * (n-k)!);

::

    combinations =    10.000000

Remarks
-------

- The factorial is defined only for non-negative integers.
- 0! = 1 by definition.
- For large values, the result may overflow to infinity.
- For the gamma function (generalized factorial), use :func:`gamma` where gamma(n+1) = n!.

.. seealso:: Functions :func:`gamma`, :func:`lnfact`
