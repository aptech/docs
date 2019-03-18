
getnamef
==============================================

Purpose
----------------

Returns a string array containing the names of the variables in a GAUSS data set.

Format
----------------
.. function:: getnamef(f)

    :param f: file handle of an open data set
    :type f: scalar

    :returns: y (*TODO*), Nx1 string array containing the names of all of the variables in the specified data set.

Examples
----------------

::

    file = getgausshome()$+ "examples/freqdata.dat";				
    //Open the dataset
    open f = ^file for read;
    
    //Create a string array with the variable names from the 
    //dataset
    y = getnamef(f);
    
    //Check which variables are character and which are numeric
    t = vartypef(f);
    
    print y;

produces:

::

    AGE 
    PAY 
    sex 
    WT

The above example assumes that the data set freqdata
contains the variables: AGE, PAY, sex, WT.
Note the use of vartypef to determine the types of these variables.

.. seealso:: Functions :func:`getname`, :func:`getHeaders`, :func:`indcv`, :func:`vartypef`
