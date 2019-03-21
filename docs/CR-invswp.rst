
invswp
==============================================

Purpose
----------------

Computes a generalized sweep inverse.

Format
----------------
.. function:: invswp(x)

    :param x: 
    :type x: NxN matrix

    :returns: y (*NxN matrix*), the generalized inverse of x.



Remarks
-------

This will invert any general matrix. That is, even matrices which will
not invert using inv because they are singular will invert using invswp.

x and y will satisfy the two conditions:

#. xyx = x
#. yxy = y

invswp returns a row and column with zeros when the pivot fails. This is
good for quadratic forms since it essentially removes rows with
redundant information, i.e., the statistices generated will be "correct"
but with reduced degrees of freedom.

The tolerance used to determine if a pivot element is zero is taken from
the crout singularity tolerance. The corresponding row and column are
zeroed out. See **Singularity Tolerance**, Chapter 1.

