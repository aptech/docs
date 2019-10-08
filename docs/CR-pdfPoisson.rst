
pdfPoisson
==============================================

Purpose
----------------
Computes the Poisson probability mass function.

Format
----------------
.. function:: p = pdfPoisson(x, lambda)

    :param x: *x* must be a positive whole number.
    :type x: NxK matrix, Nx1 vector or scalar

    :param lambda: The mean parameter. ExE conformable with *x*.
    :type lambda: NxK matrix, Nx1 vector or scalar

    :return p: the Poisson probability mass function evaluated at the elements in *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

For invalid inputs, :func:`pdfPoisson` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.


Examples
----------------

Basic example
+++++++++++++

::

    p = pdfPoisson(190, 200);

After the code above, *p* is equal to:

::

    0.02243

Vector input
++++++++++++

::

    events = { 170,
               180,
               190,
               200 };
    p = pdfPoisson(events, 200);

After the code above, *p* is equal to:

::

    0.00285
    0.01056
    0.02243
    0.02820

Vector Inputs
+++++++++++++

::

    events = { 170,
               180,
               190,
               200 };
    lambda = { 180,
               190,
               200,
               210 };

    p = pdfPoisson(events, lambda);

After the code above, *p* is equal to:

::

    0.02304
    0.02274
    0.02243
    0.02214

.. seealso:: Functions :func:`cdfPoisson`, :func:`cdfPoissonInv`, :func:`rndPoisson`
