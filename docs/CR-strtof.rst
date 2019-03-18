
strtof
==============================================

Purpose
----------------
Converts a string array to a numeric matrix.

Format
----------------
.. function:: strtof(sa)

    :param sa: NxK string array containing numeric data.
    :type sa: TODO

    :returns: x (*TODO*), NxK matrix.

Examples
----------------

::

    //Create a string array
    string sa = { "1.1" "2.2" "3.3", 
                  "4.4" "5.5" "6.6" };
    num = strtof(sa);

After the code above, num is a numeric matrix with the following values:

::

    1.100  2.200 3.300
    4.400  5.500 6.600

.. seealso:: Functions :func:`strtofcplx`, :func:`ftostrC`
