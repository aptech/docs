
endp
==============================================

Purpose
----------------

Closes a procedure or keyword definition.

Format
----------------
.. function:: endp

Examples
----------------

::

    proc regress(y,x);
       retp(inv(x'x)*x'y);
    endp;
     
    x = { 1 3 2, 7 4 9, 1 1 6, 3 3 2 };
    y = { 3, 5, 2, 7 };
     
    b = regress(y,x);

After executing the above code:

::

    0.1546 
    b = 1.5028 
       -0.1284

.. seealso:: Functions :func:`proc`, :func:`keyword`, :func:`retp`
