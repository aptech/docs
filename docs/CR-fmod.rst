
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

    :type r: max(N,L) by max(K,M) matrix

Remarks
-------

Returns the floating-point remainder *r* of :math:`x/y` such that :math:`x = iy + r`,
where *i* is an integer, *r* has the same sign as *x* and :math:`\|r\| < \|y\|`.

Compare this with ``%``, the modulo division operator. (See `Operators`, Chapter 1.)


Examples
----------------
This example extracts all of the years which are evenly divisible by four, from a vector with all of the years between 1900 and 2000.

::

    /*
    ** Create a vector with all years from 1900 to 2000
    ** i.e. 1900, 1901, 1902...2000
    */
    yrs = seqa(1900, 1, 101);

    // Create an empty matrix into which we can put our output
    y4 = {};

    // Loop through each element in yrs
    for i(1, rows(yrs), 1);
       /*
       ** If the 'i'th element of 'yrs' is evenly divisible by
       ** 4, vertically concatenate it on to the bottom of 'y4'
       */
       if not fmod(yrs[i], 4);
          y4 = y4|yrs[i];
       endif;
    endfor;

    // No digits after the decimal place
    format /rd 8,0;

    /*
    ** Split 'y4' into two columns, each with half of the data
    ** and print the columns next to each other
    */
    print y4[1:13]~y4[14:26];

produces:

::

        1900     1952
        1904     1956
        1908     1960
        1912     1964
        1916     1968
        1920     1972
        1924     1976
        1928     1980
        1932     1984
        1936     1988
        1940     1992
        1944     1996
        1948     2000
