
setdif
==============================================

Purpose
----------------

Returns the unique elements in one vector that are not present in a second vector.

Format
----------------
.. function:: setdif(v1,  v2,  typ)

    :param v1: Nx1 vector.
    :type v1: TODO

    :param v2: Mx1 vector.
    :type v2: TODO

    :param typ: scalar, type of data.
    :type typ: Optional input

    .. csv-table::
        :widths: auto

        "0     character, case sensitive."
        "1      numeric (Default)."
        "2     character, case insensitive."

    :returns: y (*TODO*), Lx1 vector containing all unique values
        that are in  v1 and are not in
        v2, sorted in ascending order.

Examples
----------------

Basic example
+++++++++++++

::

    //Create a vector of years
    y1 = { 1980,
           1984,
           1988,
           1992,
           1996,
           2000,
           2004,
           2008,
           2012,
           2016 };
    
    y2 = { 1980,
           1988,
           1992,
           2000,
           2008,
           2016 };
    
    //Set 'y_diff' equal to years in 'y1' and NOT in 'y2'
    y_diff = setdif(y1, y2);

After the code above, y_diff will be equal to:

::

    1984
    1996
    2004
    2012

Character data
++++++++++++++

::

    //Create 2 vectors of character data using the
    //numeric concatenation operator
    sp500 = "aapl" | "goog" | "msft" | "xom" | "wfc" | "jnj";
    nasdaq = "aapl" | "msft" | "amzn" | "goog" | "fb" | "gild";
    
    //Set type to 'character, case insensitive'
    typ = 2;
    
    //Find characters in sp500 and NOT in nasdaq
    sp_only = setdif(sp500, nasdaq, 2);
    
    //NOTE: The $ in front of the variable name tell
    //GAUSS to print the variable as character data
    print $sp_only;

The code above will produce the following output:

::

    jnj 
    wfc 
    xom

Remarks
+++++++

Place smaller vector first for fastest operation.

When there are a lot of duplicates, it is faster to remove them first
with unique before calling this function.

Source
++++++

setdif.src

.. seealso:: Functions :func:`setdifsa`, :func:`union`
