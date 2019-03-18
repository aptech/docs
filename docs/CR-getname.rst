
getname
==============================================

Purpose
----------------

Returns a column vector containing the
names of the variables in a GAUSS data set.

Format
----------------
.. function:: getname(dset)

    :param dset: string specifying the name of the data set from which the function will obtain the variable names.
    :type dset: TODO

    :returns: y (*TODO*), Nx1 vector containing the names of all of the variables in the specified data set.

Examples
----------------

::

    y = getname(getGaussHome $+ "examples/freqdata.dat");
    format 8,8;
    print $y;

produces:

::

    AGE 
    PAY 
    sex 
    WT

The above example assumes that the data set olsdat
contains the variables: TIME, DIST, TEMP, FRICT.
Note that the extension is not included in the filename
passed to the getname function.

.. seealso:: Functions :func:`getnamef`, :func:`indcv`
