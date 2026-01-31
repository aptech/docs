
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

    :return y: Indices of the
        elements of *x* which fall into the category defined
        by *v*. It will contain error code 13 if there are
        no elements in this category.

    :rtype y: Lx1 vector

Examples
----------------

::

    x = { 1.0, 4.0, 3.3, 4.2, 6.0, 5.7, 8.1, 5.5 };
    v = { 4, 6 };
    indx = indexcat(x, v);

    inBds = x[indx]

::

           4           4.20
    indx = 5   inBds = 6.00
           6           5.70
           8           5.50

Example 2: Finding rows by string value in a dataframe
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create sample dataframe
    sales = asdf(seqa(100, 50, 5), "sales");
    region = asdf("North" $| "South" $| "North" $| "East" $| "South", "region");
    df = region ~ sales;

    print df;

::

          region            sales
           North        100.00000
           South        150.00000
           North        200.00000
            East        250.00000
           South        300.00000

::

    // Find indices of all "South" regions
    south_idx = indexcat(df[., "region"], "South");

    print south_idx;

::

    2.0000000
    5.0000000

::

    // Use indices to extract matching rows
    south_data = df[south_idx, .];

    print south_data;

::

          region            sales
           South        150.00000
           South        300.00000

.. seealso:: Functions :func:`contains`, :func:`ismember`, :func:`rowcontains`
