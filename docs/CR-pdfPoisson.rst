
pdfPoisson
==============================================

Purpose
----------------
Computes the Poisson probability  mass  function.

Format
----------------
.. function:: pdfPoisson(x, lambda)

    :param x: Nx1 vector or scalar. x must be a positive whole number.
    :type x: NxK matrix

    :param lambda:  The mean parameter.
    :type lambda: ExE conformable with x

    :returns: p (*NxK matrix or Nx1 vector or scalar*)

Examples
----------------

Basic example
+++++++++++++

::

    p = pdfPoisson(190,200);

After the code above, p is equal to:

::

    0.02243

Vector input
++++++++++++

::

    events = { 170,
               180,
               190,
               200 };
    p = pdfPoisson(events,200);

After the code above, p is equal to:

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
    
    p = pdfPoisson(events,lambda);

After the code above, p is equal to:

::

    0.02304 
    0.02274 
    0.02243 
    0.02214

.. seealso:: Functions :func:`cdfPoisson`, :func:`cdfPoissonInv`, :func:`rndPoisson`
