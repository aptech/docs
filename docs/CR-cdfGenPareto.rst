
cdfGenPareto
==============================================

Purpose
----------------
Computes the cumulative distribution function for the Generalized Pareto distribution.

Format
----------------
.. function:: cdfGenPareto(x, a, o, k)

    :param x: 
    :type x: NxK matrix or Nx1 vector or scalar

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix or Nx1 vector or scalar

    :param o: Scale parameter, ExE conformable with *x*. *o* must be greater than 0.
    :type o: NxK matrix or Nx1 vector or scalar

    :param k: Shape parameter, ExE conformable with *x*.
    :type k: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)


Remarks
-------

The cumulative distribution function for the Generalized Pareto
distribution is defined as:

.. DANGER:: FIx equation missing here.

.. seealso:: :func:`pdfGenPareto`

