
histp
==============================================

Purpose
----------------

Computes and graphs a percent frequency histogram of a vector. The percentages in each category are plotted.

Format
----------------
.. function:: histp(x, v)

    :param x: Mx1 vector of data.
    :type x: TODO

    :param v: the breakpoints to be used to compute the frequencies
        - or -scalar, the number of categories.
    :type v: Nx1 vector

    :returns: b (*Px1 vector*), the breakpoints used for each category.

    :returns: m (*Px1 vector*), the midpoints of each category.

    :returns: freq (*TODO*), Px1 vector of computed frequency counts. This is the vector of counts, not percentages.

