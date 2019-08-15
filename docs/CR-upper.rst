
upper
==============================================

Purpose
----------------
Converts a string, matrix of character data, or string array to uppercase.

Format
----------------
.. function:: y = upper(x)

    :param x: the character data to be converted to uppercase.
    :type x: string or NxK matrix, or string array 

    :return y: containing the uppercase equivalent of the data in *x*.

    :rtype y: string or NxK matrix or string array

Remarks
-------

If *x* is a numeric matrix, *y* will contain garbage. No error message will
be generated since GAUSS does not distinguish between numeric and character data in matrices.


Examples
----------------

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

