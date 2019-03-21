
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

    :returns: c (matrix), max(N,L,P) by max(K,M,Q) matrix, the result of the double integral
        from :math:`-∞` to h and :math:`-∞` to *k* of the standardized bivariate Normal density :math:`f(x, y, r)`.

Remarks
-------

The function integrated is:

.. math:: f(x,y,r) =e−0.5w2π−r2          

with

.. math:: w⁢ = x2−2rxy+y21−r2          

Thus, *x* and *y* have 0 means, unit variances, and :math:`correlation = r`.

Allowable ranges for the arguments are:

.. math::

   -∞ ≤ h ≤ +∞
   -∞ ≤ k ≤ +∞
   -1 < r < 1

A -1 is returned for those elements with invalid inputs.

To find the integral under a general bivariate density, with *x* and *y*
having nonzero means and any positive standard deviations, use the
transformation equations:

.. math::  

   h = (ht - ux) ./ sx;
   k = (kt - uy)

where *ux* and *uy* are the (vectors of) means of *x* and *y*, *sx* and *sy* are the
(vectors of) standard deviations of *x* and *y*, and *ht* and *kt* are the
(vectors of) upper integration limits for the untransformed variables,
respectively.


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

