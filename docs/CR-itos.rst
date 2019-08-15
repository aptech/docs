
itos
==============================================

Purpose
----------------

Converts a scalar or matrix to the string representation of an integer.

Format
----------------
.. function:: str = itos(x)

    :param x:  data
    :type x: scalar or NxK matrix

    :return str_int: or string array containing the string representation of the elements of x.

    :rtype str_int: string

Examples
----------------

::

  // Set x
  x = 4;

  // Convert integer to string
  str_int = itos(x);

  // Print results
  print "x = " x;
  print "str_int = " str_int;

After this code:

::

  x =
     4.000000

  str_int =
      4

.. seealso:: Functions :func:`ftos`, :func:`stof`
