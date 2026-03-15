
strtriml
==============================================

Purpose
----------------
Strips all whitespace characters from the left side of each element in a string array.

Format
----------------
.. function:: y = strtriml(sa)

    :param sa: data
    :type sa: NxM string array

    :return y: contains contents in *sa* with all whitespace characters from the left side of each element stripped. 

    :rtype y: NxM string array

Examples
----------------

::

    // Create a string array with leading whitespace
    sa = "   hello" $| "   world";

    // Strip whitespace from the left
    y = strtriml(sa);
    print y;

The code above produces the following output:

::

    hello
    world

Source
------

strfns.src

.. seealso:: Functions :func:`strtrimr`, :func:`strtrunc`, :func:`strtruncl`, :func:`strtruncpad`, :func:`strtruncr`
