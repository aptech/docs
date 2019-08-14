
digamma
==============================================

Purpose
----------------

Computes the digamma function.

Format
----------------
.. function:: y = digamma(x)

    :param x: Values at which to compute the digamma function.
    :type x: MxN matrix or N-dimensional array

    :returns: **y** (*MxN matrix or N-dimensional array*) - digamma.

Examples
----------------

::

  // Define x matrix
  x = { 2, 6, 3, 49, 5 };

  // Find digamma function
  y = digamma(x);

After this code:

::

  y =  0.42278434
       1.7061177
       0.92278434 
       3.8815815
       1.5061177

Remarks
-------

The :func:`digamma` function is the first derivative of the log of the :func:`gamma`
function with respect to its argument.
