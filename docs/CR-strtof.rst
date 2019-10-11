
strtof
==============================================

Purpose
----------------
Converts a string array to a numeric matrix.

Format
----------------
.. function:: x = strtof(sa)

    :param sa: numeric data
    :type sa: NxK string array

    :return x: 

    :rtype x: NxK matrix

Examples
----------------

::

    // Create a string array
    string sa = { "1.1" "2.2" "3.3", 
                  "4.4" "5.5" "6.6" };
    num = strtof(sa);

After the code above, *num* is a numeric matrix with the following values:

::

    1.100  2.200 3.300
    4.400  5.500 6.600

Remarks
-------

Elements with more than one numerical character separated by a delimiter
such as a comma or a space will be interpreted as complex data. For
example, the string:
::

   "1.2 1.9"

will be converted into the number:

::

   1.2 + 1.9i

Parentheses surrounding the numerical elements in the string will be
ignored as will be a following *i*. The following strings will be
interpreted as the same by :func:`strtof`.

::

   "(2.31 4.72)""2.31 4.73""2.31,4.73i"

.. seealso:: Functions :func:`strtofcplx`, :func:`ftostrC`

