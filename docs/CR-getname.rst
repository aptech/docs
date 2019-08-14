
getname
==============================================

Purpose
----------------

Returns a column vector containing the names of the variables in a GAUSS data set.

Format
----------------
.. function:: y = getname(dset)

    :param dset: the name of the data set from which the function will obtain the variable names
    :type dset: string

    :return var_names: contains the names of all of the variables in the specified data set.

    :type var_names: Nx1 vector

Remarks
-------

The output, *var_names*, will have as many rows as there are variables in the data set.


Examples
----------------

::

    /*
    ** Get the variable names from
    ** the file `freqdata` stored in the GAUSS
    ** examples directory
    */
    var_names = getname(getGAUSSHome() $+ "examples/freqdata.dat");

    // Print format
    format 8,8;

    // Print variable names
    print $var_names;

produces:

::

    AGE
    PAY
    sex
    WT


.. seealso:: Functions :func:`getnamef`, :func:`indcv`
