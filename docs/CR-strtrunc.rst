
strtrunc
==============================================

Purpose
----------------

Truncates all elements of a string array to not longer than the specified number of characters.

Format
----------------
.. function:: y = strtrunc(sa, maxlen)

    :param sa: data
    :type sa: NxK string array

    :param maxlen: maximum length.
    :type maxlen: 1xK or 1x1 matrix

    :return y: contains contents of *sa* truncated to length specified by *maxlen*.

    :rtype y: NxK string array

Examples
----------------

::

    string s = { "best", "linear", "unbiased", "estimator" };
    ss = strtrunc(s, 6);

After the code above, the variables ``s`` and ``ss`` are equal to:

::

            best
          linear
    s = unbiased
       estimator

            best
          linear
    ss =  unbias
          estima

.. seealso:: Functions :func:`strtriml`, :func:`strtrimr`, :func:`strtruncl`, :func:`strtruncpad`, :func:`strtruncr`
