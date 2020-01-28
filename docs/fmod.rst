
fmod
==============================================

Purpose
----------------

Computes the floating-point remainder of :math:`x/y`.

Format
----------------
.. function:: r = fmod(x, y)

    :param x:
    :type x: NxK matrix

    :param y: ExE conformable with *x*.
    :type y: LxM matrix

    :return r: The floating point remainders of :math:`x/y`.

    :rtype r: max(N,L) by max(K,M) matrix

Examples
----------------

Example 1: Basic usage
+++++++++++++++

::

   x = { 1.3 2.5,
         4.2 6.0 };

   a = fmod(x, 0.5);
   b = fmod(x, 2);

After the above code, *a* and *b* will equal:

::

    a = 0.3 0  b = 1.3 0.5
        0.2 0      0.2   0

This example extracts all of the years which are evenly divisible by four, from a vector with all of the years between 1900 and 2000.

Example 2: Find years divisible by 4
++++++++++++++++++++++++++++++++++++

::

    /*
    ** Create a vector with all years from 1900 to 2000
    ** i.e. 1900, 1901, 1902...2000
    */
    yrs = seqa(1900, 1, 101);

    // Create a vector with 0 if the element
    // is evenly divisible by 4
    mask = fmod(yrs, 4);

    // Return all rows where 'mask' is equal to 0
    // (or delete all rows if they are non-zero)
    yrs_4 = delif(yrs, mask);

    // Print the first 10 rows
    print yrs_4[1:10];

produces:

::

        1900
        1904
        1908
        1912
        1916
        1920
        1924
        1928
        1932
        1936

Remarks
-------

Returns the floating-point remainder *r* of :math:`x/y` such that :math:`x = iy + r`,
where *i* is an integer, *r* has the same sign as *x* and :math:`\|r\| < \|y\|`.

Compare this with ``%``, the modulo division operator. (See `Operators <OP-Operators.html>`_.)


