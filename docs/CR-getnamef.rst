
getnamef
==============================================

Purpose
----------------

Returns a string array containing the names of the variables in a GAUSS dataset.

Format
----------------
.. function:: var_names = getnamef(fh)

    :param fh: file handle of an open dataset
    :type fh: scalar

    :return var_names: contains the names of all of the variables in the specified dataset.

    :rtype var_names: Nx1 string array

Remarks
-------

The output, *y*, will have as many rows as there are variables in the dataset.


Examples
----------------

::

    // Specify file name
    file = getGAUSSHome()$+ "examples/freqdata.dat";

    // Open the dataset
    open fh = ^file for read;

    /*
    ** Create a string array with the variable names from the
    ** dataset
    */
    var_names = getnamef(fh);

    // Print variables 
    print var_names;

produces:

::

    AGE
    PAY
    sex
    WT

The above example assumes that the dataset ``freqdata``
contains the variables: ``AGE, PAY, sex, WT``.
Note the use of :func:`vartypef` to determine the types of these variables.

.. seealso:: Functions :func:`getname`, :func:`getHeaders`, :func:`indcv`, :func:`vartypef`
