
upper
==============================================

Purpose
----------------
Converts a string, matrix of character data, or string array to uppercase.

Format
----------------
.. function:: y = upper(x)

    :param x: the character data to be converted to uppercase.
    :type x: string,  NxK matrix, dataframe, or string array 

    :return y: containing the uppercase equivalent of the data in *x*.

    :rtype y: string or NxK matrix or string array

Examples
----------------

::

    // Load example dataframe
    rep78 = loadd(getGAUSSHome("examples/auto2.dta"), "rep78");

    print rep78[1:4];

::

           rep78 
         Average 
         Average 
               . 
         Average


::

   rep78_u = upper(rep78);
   print rep78_u[1:4];

::

           rep78 
         AVERAGE 
         AVERAGE 
               . 
         AVERAGE

::

    // Create a lowercase string
    x = "uppercase";
    
    // Convert the string to upper case
    y = upper(x);
    
    // Adding the '$' tells GAUSS to treat the data as character
    // data
    print $y;

This code produces:

::

    UPPERCASE

.. seealso:: Functions :func:`lower`

