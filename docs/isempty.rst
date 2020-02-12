
isempty
==============================================

Purpose
----------------

Returns a 1 if its input is an empty matrix, otherwise returns a 0.

Format
----------------
.. function:: ret = isempty(x)

    :param x: data
    :type x: matrix

    :return ret: 1 if *x* is an empty matrix, otherwise 0.

    :rtype ret: scalar

Examples
----------------

Example 1
+++++++++++++

::

    // Create an empty matrix
    x = {};

    ret = isempty(x);

After the above code, *ret* will equal 1.

Example 2
+++++++++++++

::

    // Create a non-empty matrix
    y = 1;

    ret = isempty(y);

After the above code, *ret* will equal 0.

    
Example 3
+++++++++++++

::
    
    // Create an empty matrix
    x = {};

    // Check to see if 'x' is an empty matrix
    if isempty(x);
        print "x is an empty matrix";
    else;
        print "x is not empty";
    endif;

The above code will print:

::

    x is an empty matrix


.. seealso:: Functions :func:`ismiss`, :func:`isinfnanmiss`
