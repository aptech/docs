
strtruncpad
==============================================

Purpose
----------------

Truncates all elements of a string array to the specified number of
characters, adding spaces on the end as needed to achieve the exact
length.

Format
----------------
.. function:: y = strtruncpad(sa, maxlen)

    :param sa: data
    :type sa: NxK string array

    :param maxlen: maximum length.
    :type maxlen: 1xK or 1x1 matrix

    :return y: result.

    :type y: NxK string array

.. seealso:: Functions :func:`strtriml`, :func:`strtrimr`, :func:`strtrunc`, :func:`strtruncl`, :func:`strtruncr`

