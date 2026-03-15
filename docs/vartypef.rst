
vartypef
==============================================

Purpose
----------------
Returns a vector of ones and zeros that indicate whether variables in a dataset are character or numeric.

Format
----------------
.. function:: y = vartypef(f)

    :param f: file handle of an open file
    :type f: scalar

    :return y: 1 if variable is numeric, 0 if character.

    :rtype y: Nx1 vector of ones and zeros

Remarks
-------

This function should be used in place of older functions that are based
on the case of the variable names. You should also use the v96 dataset format.

Examples
----------------

::

    // Open a dataset
    open f = mydata.dat;

    // Get variable types: 1=numeric, 0=character
    y = vartypef(f);
    print y;

    f = close(f);

.. seealso:: Functions :func:`colsf`, :func:`rowsf`
