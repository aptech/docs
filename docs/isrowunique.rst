
isrowunique
==============================================

Purpose
----------------

Checks each row and returns a 1 for the row if the permutation of values has been seen previously, otherwise returns a 0.

Format
----------------
.. function:: ret = isrowunique(x)

    :param x: data
    :type x: N x M matrix or dataframe

    :param varlist: Optional, list of variables to include in the check. Default is to check across all variables.
    :type varlist: string array

    :return ret: 1 if a row in ``x`` contains a unique permutation of data, 0 for the row otherwise.
    :rtype ret: N x 1 Vector

Examples
----------------

::

    // Create data
    x = { 1 1 1,
          1 2 1,
          1 1 1,
          1 2 2,
          2 1 1,
          1 2 2 };

    // Check if permutations in rows
    // are unique
    ur = isrowunique(x);
    print ur;

::

    1.0000000
    1.0000000
    0.0000000
    1.0000000
    1.0000000
    0.0000000


We can print the unique observations like this:

::

    print selif(x, ur);


::

    1.00  1.00 1.00
    1.00  2.00 1.00
    1.00  2.00 2.00
    2.00  1.00 1.00

    

.. seealso:: Functions :func:`isunique`, :func:`dropduplicates`, :func:`getduplicates`
