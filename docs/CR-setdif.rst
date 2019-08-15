
setdif
==============================================

Purpose
----------------

Returns the unique elements in one vector that are not present in a second vector.

Format
----------------
.. function:: y = setdif(v1, v2[, typ])

    :param v1: data
    :type v1: Nx1 vector

    :param v2: data
    :type v2: Mx1 vector

    :param typ: Optional input, type of data.

        .. csv-table::
            :widths: auto
    
            "0", "character, case sensitive."
            "1", "numeric (Default)."
            "2", "character, case insensitive."

    :type typ: scalar

    :return y: containing all unique values
        that are in *v1* and are not in *v2*, sorted in ascending order.

    :rtype y: Lx1 vector

Remarks
-------

Place smaller vector first for fastest operation.

When there are a lot of duplicates, it is faster to remove them first
with :func:`unique` before calling this function.

Examples
----------------

Basic example
+++++++++++++

::

    // Create a vector of years
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
    
    // Set 'y_diff' equal to years in 'y1' and NOT in 'y2'
    y_diff = setdif(y1, y2);

After the code above, *y_diff* will be equal to:

::

    1984
    1996
    2004
    2012

Character data
++++++++++++++

::

    // Create 2 vectors of character data using the
    // numeric concatenation operator
    sp500 = "aapl" | "goog" | "msft" | "xom" | "wfc" | "jnj";
    nasdaq = "aapl" | "msft" | "amzn" | "goog" | "fb" | "gild";
    
    // Set type to 'character, case insensitive'
    typ = 2;
    
    // Find characters in sp500 and NOT in nasdaq
    sp_only = setdif(sp500, nasdaq, 2);
    
    // NOTE: The $ in front of the variable name tell
    // GAUSS to print the variable as character data
    print $sp_only;

The code above will produce the following output:

::

    jnj 
    wfc 
    xom

Source
------

setdif.src

.. seealso:: Functions :func:`setdifsa`, :func:`union`

