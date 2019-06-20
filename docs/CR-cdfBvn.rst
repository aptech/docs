
cdfBvn
==============================================

Purpose
----------------
Computes the cumulative distribution function of the standardized bivariate Normal density (lower tail).

Format
----------------
.. function:: cdfBvn(h, k, r)

    :param h: the upper limits of integration for variable 1.
    :type h: NxK matrix

    :param k: ExE conformable with *h*, the upper limits of integration for variable 2.
    :type k: LxM matrix

    :param r: ExE conformable with *h* and *k*, the correlation coefficients between the two variables.
    :type r: PxQ matrix

    :returns: **p** (*matrix), max(N,L,P) by max(K,M,Q) matrix*), the result of the double integral
        from :math:`-∞` to h and :math:`-∞` to *k* of the standardized bivariate Normal density :math:`f(x, y, r)`.

Remarks
-------

The function integrated is:

.. math:: f(x,y,r) =\frac{e^{−0.5w}}{2\pi\sqrt{−r^2}}

with

.. math:: w⁢ = \frac{x^2 − 2rxy + y^2}{1−r^2}

Thus, *x* and *y* have 0 means, unit variances, and :math:`correlation = r`.

Allowable ranges for the arguments are:

.. math::

   -∞ \leq h \leq +∞ \\
   -∞ \leq k \leq +∞ \\
   -1 \lt r \lt 1

A -1 is returned for those elements with invalid inputs.

To find the integral under a general bivariate density, with *x* and *y*
having nonzero means and any positive standard deviations, use the
transformation equations:

.. math::

   h = (ht - ux)/ sx\\
   k = (kt - uy)\\

where *ux* and *uy* are the (vectors of) means of *x* and *y*, *sx* and *sy* are the
(vectors of) standard deviations of *x* and *y*, and *ht* and *kt* are the
(vectors of) upper integration limits for the untransformed variables,
respectively.

Examples
----------------

::

  // Upper integration bounds of variable 1
  x = rndn(10, 1);

  // Upper integration bounds of variable 2
  y = rndn(10, 1);

  // Correlation parameter
  rho = rndu(10, 1);

  // Call cdfBvn
  p = cdfBvn(x, y, rho);
  print "p =" p;

After above code,

::

  p =
  0.1010
  0.0001
  0.5556
  0.4180
  0.0154
  0.5478
  0.0577
  0.4855
  0.4579
  0.1814

Technical Notes
---------------

The absolute error for :func:`cdfBvn` is approximately :math:`±5.0e-9` for the entire
range of arguments.

References
----------

#. Daley, D.J. ''Computation of Bi- and Tri-variate Normal Integral.''
   Appl. Statist. Vol. 23, No. 3, 1974, 435-38.
#. Owen, D.B. ''A Table of Normal Integrals.'' Commun. Statist.-Simula.
   Computa., B9(4). 1980, 389-419.

.. seealso:: :func:`cdfN`, :func:`cdfTvn`
