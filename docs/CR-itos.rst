
itos
==============================================

Purpose
----------------

Converts a scalar or matrix to the string representation of an integer.

Format
----------------
.. function:: itos(x)

    :param x: scalar or NxK matrix.
    :type x: TODO

    :returns: y (*TODO*), string or string array containing the string representation of the elements of x.

Examples
----------------

x = 4;
str = itos(x);
print "x = " x;
print "str = " str;

x = 
   1.000000

str = 
   1
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for i(1, 4, 1);
    print "iteration "$+itos(i);
endfor;
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. seealso:: Functions :func:`ftos`, :func:`stof`
