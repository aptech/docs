
hist
==============================================

Purpose
----------------

Computes and graphs a frequency histogram for a vector. The actual frequencies are plotted for each category. Note: this function is for use with the deprecated PQG graphics.
plotHist instead.

Format
----------------
.. function:: hist(x, v)

    :param x: 
    :type x: Mx1 vector of data

    :param v: the breakpoints to be used to compute the frequencies
        - or -scalar, the number of categories.
    :type v: Nx1 vector

    :returns: b (*Px1 vector*), the breakpoints used for each category.

    :returns: m (*Px1 vector*), the midpoints of each category.

    :returns: freq (*Px1 vector*) of computed frequency counts.

Remarks
-------

If a vector of breakpoints is specified, a final breakpoint equal to the
maximum value of x will be added if the maximum breakpoint value is
smaller.

If a number of categories is specified, the data will be divided into v
evenly spaced categories.

Each time an element falls into one of the categories specified in b,
the corresponding element of freq will be incremented by one. The
categories are interpreted as follows:

::

   freq[1] =          x < b[1]
   freq[2] = b[1]   < x < b[2]
   freq[3] = b[2]   < x < b[3]
     .
     .
     .
   freq[P] = b[P-1] < x < b[P]


Examples
----------------

::

    library pgraph;
    x = rndn(5000,1);
    { b,m,f } = hist(x,20);

Source
------

phist.src

.. seealso:: Functions :func:`histp`, :func:`histf`, :func:`bar`
