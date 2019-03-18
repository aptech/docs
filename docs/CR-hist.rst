
hist
==============================================

Purpose
----------------

Computes and graphs a frequency histogram for a vector. The actual frequencies are plotted for each category. Note: this function is for use with the deprecated PQG graphics.
plotHist instead.

Format
----------------
.. function:: hist(x,  v)

    :param x: Mx1 vector of data.
    :type x: TODO

    :param v: the breakpoints to be used to compute the frequencies
        - or -scalar, the number of categories.
    :type v: Nx1 vector

    :returns: b (*Px1 vector*), the breakpoints used for each category.

    :returns: m (*Px1 vector*), the midpoints of each category.

    :returns: freq (*TODO*), Px1 vector of computed frequency counts.

Examples
----------------

::

    library pgraph;
    x = rndn(5000,1);
    { b,m,f } = hist(x,20);

Source
++++++

phist.src

.. seealso:: Functions :func:`histp`, :func:`histf`, :func:`bar`
