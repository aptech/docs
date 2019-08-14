
indexcat
==============================================

Purpose
----------------

Returns the indices of the elements of a vector which fall into a specified category

Format
----------------
.. function:: y = indexcat(x, v)

    :param x: data
    :type x: Nx1 vector

    :param v: If scalar, the function returns the indices of all elements of *x* equal to *v*.
        If 2x1, then the function returns the indices of all elements of *x* that fall into the range:

        .. math:: v[1] < x <= v[2]

        If *v* is scalar, it can contain a single missing to specify the missing value as the category.

    :type v: scalar or 2x1 vector

    :returns: **y** (*Lx1 vector*) - Indices of the
        elements of *x* which fall into the category defined
        by *v*. It will contain error code 13 if there are
        no elements in this category.

Examples
----------------

::

    let x = 1.0 4.0 3.3 4.2 6.0 5.7 8.1 5.5;
    let v = 4 6;
    indx = indexcat(x, v);

    inBds = x[indx]

::

           4           4.20
    indx = 5   inBds = 6.00
           6           5.70
           8           5.50

.. seealso:: Functions :func:`contains`, :func:`ismember`, :func:`rowcontains`
