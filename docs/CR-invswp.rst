
invswp
==============================================

Purpose
----------------

Computes a generalized sweep inverse.

Format
----------------
.. function:: invswp(x)

    :param x: data
    :type x: NxN matrix

    :returns: **xig** (*NxN matrix*) - the generalized inverse of *x*.


Remarks
-------

This will invert any general matrix. That is, even matrices which will
not invert using :func:`inv` because they are singular will invert using :func:`invswp`.

*x* and *xig* will satisfy the two conditions:

#. :math:`x*xig*x = x`
#. :math:`xig*x*xig = y`

:func:`invswp` returns a row and column with zeros when the pivot fails. This is
good for quadratic forms since it essentially removes rows with
redundant information, i.e., the statistics generated will be "correct"
but with reduced degrees of freedom.

The tolerance used to determine if a pivot element is zero is taken from
the :func:`crout` singularity tolerance. The corresponding row and column are
zeroed out. See **Singularity Tolerance**, Chapter 1.
