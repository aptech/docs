
sortind, sortindc
==============================================

Purpose
----------------
Returns the sorted index of x.

Format
----------------
.. function:: sortind(x) 
			  sortindc(x)

    :param x: Nx1 column vector.
    :type x: TODO

    :returns: ind (*TODO*), Nx1 vector representing sorted index of x.

Examples
----------------

::

    //Create uniform random integers between 0 and 10
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

