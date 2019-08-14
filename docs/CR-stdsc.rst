
stdsc
==============================================

Purpose
----------------
Computes the standard deviation of the elements in each column of a matrix.

Format
----------------
.. function:: y = stdsc(x)

    :param x: data
    :type x: NxK matrix

    :returns: y (*Kx1 vector*), the standard deviation of each column of *x*.

Remarks
-------

This function essentially computes:

::

   sqrt(1/(N)*sumc((x-meanc(x)')2))

Thus, the divisor is :math:`N` rather than :math:`N-1`, where :math:`N` is the number of
elements being summed. See :func:`stdc` for the alternate definition.


Examples
----------------

::

    // Create 3 columns of random normal numbers
    y = rndn(8100,3);
    
    // Calculate the standard deviation of each column
    std = stdsc(y);

The return, in variable *std* is equal to:

::

    1.00095980 
    0.99488832 
    1.00201375

.. seealso:: Functions :func:`stdc`, :func:`astds`, :func:`meanc`

