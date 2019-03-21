
cdfRayleighInv
==============================================

Purpose
----------------

Computes the Rayleigh inverse cumulative distribution function.

Format
----------------
.. function:: cdfRayleighInv(p, b)

    :param p: must be greater than 0 and less than 1.
    :type p: NxK matrix or Nx1 vector or scalar

    :param b: Shape parameter, ExE conformable with *p*. *b* must be greater than 0.
    :type b: NxK matrix or Nx1 vector or scalar

    :returns: x (*NxK matrix or Nx1 vector or scalar*)

Remarks
-------

::

   cdfRayleighInv(cdfRayleigh(x,b), b) = x

.. seealso:: :func:`pdfRayleigh`, :func:`cdfRayleigh`

