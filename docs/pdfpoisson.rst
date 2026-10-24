
pdfPoisson
==============================================

Purpose
----------------
Computes the Poisson probability mass function.

Format
----------------
.. function:: p = pdfPoisson(x, lambda)

    :param x: The number of events. An *x* within 1e-9 (relative) of a whole number is treated as that whole number. Any other non-whole *x* returns 0, as does a negative or infinite *x*.
    :type x: NxK matrix, Nx1 vector or scalar

    :param lambda: The mean parameter. ExE conformable with *x*.
    :type lambda: NxK matrix, Nx1 vector or scalar

    :return p: the Poisson probability mass function evaluated at the elements in *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

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

Remarks
-------

An *x* that cannot occur is not an error: it returns 0. A missing value in
either argument returns a missing value.


.. seealso:: Functions :func:`cdfPoisson`, :func:`cdfPoissonInv`, :func:`rndPoisson`
