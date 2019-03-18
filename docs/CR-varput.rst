
varput
==============================================

Purpose
----------------
Allows a matrix, array, string, or string array to be assigned to a global
symbol whose name is given as a string argument.

Format
----------------
.. function:: varput(x,  n)

    :param x: array, string, or string array which is to be assigned to
        the target variable.
    :type x: matrix

    :param n: string containing the name of the global symbol
        which will be the target variable.
    :type n: TODO

    :returns: y (*scalar*), 1 if the operation is successful and 0 if the operation fails.

Examples
----------------

::

    source = rndn(2,2);
    targname = "target";
    
    if not varput(source,targname);
       print "Symbol table full";
       end;
    endif;

.. seealso:: Functions :func:`varget`, :func:`typecv`
