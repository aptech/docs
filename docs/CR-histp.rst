
histp
==============================================

Purpose
----------------

Computes and graphs a percent frequency histogram of a vector. The percentages in each category are plotted.

Library
-------

pgraph

Format
----------------
.. function:: histp(x, v)

    :param x: data
    :type x: Mx1 vector

    :param v: the breakpoints to be used to compute the frequencies (vector) -or- the number of categories (scalar).
    :type v: Nx1 vector or scalar

    :returns: **b** (*Px1 vector*) - the breakpoints used for each category.

    :returns: **m** (*Px1 vector*) - the midpoints of each category.

    :returns: **freq** (*Px1 vector*) - Computed frequency counts. This is the vector of counts, not percentages.



Remarks
-------

If a vector of breakpoints is specified, a final breakpoint equal to the
maximum value of *x* will be added if the maximum breakpoint value is
smaller.

If a number of categories is specified, the data will be divided into *v*
evenly spaced categories.

Each time an element falls into one of the categories specified in *b*,
the corresponding element of *freq* will be incremented by one. The
categories are interpreted as follows:

::

   freq[1] =          x < b[1]
   freq[2] = b[1]   < x < b[2]
   freq[3] = b[2]   < x < b[3]
     .
     .
     .
   freq[P] = b[P-1] < x < b[P]



Source
------

phist.src

.. seealso:: Functions :func:`hist`, :func:`histf`, :func:`bar`
