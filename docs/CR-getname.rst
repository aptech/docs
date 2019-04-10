
getname
==============================================

Purpose
----------------

Returns a column vector containing the names of the variables in a GAUSS data set.

Format
----------------
.. function:: getname(dset)

    :param dset: the name of the data set from which the function will obtain the variable names
    :type dset: string

    :returns: y (*Nx1 vector*) containing the names of all of the variables in the specified data set.

Remarks
-------

The output, *y*, will have as many rows as there are variables in the data set.


Examples
----------------

::

    y = getname(getGAUSSHome() $+ "examples/freqdata.dat");
    format 8,8;
    print $y;

produces:

::

    AGE 
    PAY 
    sex 
    WT

The above example assumes that the data set *freqdata*
contains the variables: ``TIME, DIST, TEMP, FRICT``.
Note that the extension is not included in the filename
passed to the :func:`getname` function.

.. DANGER:: Review above sentence... extension is included

.. seealso:: Functions :func:`getnamef`, :func:`indcv`

