
sortind, sortindc
==============================================

Purpose
----------------
Returns the sorted index of *x*.

Format
----------------
.. function:: ind = sortind(x)
              ind = sortindc(x)

    :param x: data
    :type x: Nx1 column vector

    :return ind: of *x*.

    :rtype ind: Nx1 vector representing sorted index

Remarks
-------

:func:`sortind` assumes that *x* contains numeric data. :func:`sortindc` assumes that *x*
contains character data.

This function can be used to sort several matrices in the same way that
some other reference matrix is sorted. To do this, create the index of
the reference matrix, then use :func:`submat` to rearrange the other matrices in
the same way.

Examples
----------------

::

    // Create uniform random integers between 0 and 10
    x = round(10*rndu(10, 1);
    
    ind = sortind(x);
    y = x[ind];

After running the above code:

::

          9.00
          8.00
    x  =  0.00
          4.00
          6.00
        
          3.00
          4.00
    ind = 5.00
          2.00
          1.00
          
          0.00
          4.00
    y  =  6.00
          8.00
          9.00

