
writer
==============================================

Purpose
----------------
Writes a matrix to a GAUSS data set.

Format
----------------
.. function:: writer(fh, x)

    :param fh: handle of the file that data is to be written to.
    :type fh: TODO

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*TODO*), scalar specifying the number of rows of data
        actually written to the data set.

Examples
----------------

::

    create fp = data with x,10,8;
    
    if fp == -1;
       errorlog "Can't create output file";
       end;
    endif;
    
    c = 0;
    do until c >= 10000;
       y = rndn(100,10);
       k = writer(fp,y);
    
       if k /= rows(y);
         errorlog "Disk Full";
         fp = close(fp);
         end;
       endif;
    
       c = c+k;
    endo;
    
    fp = close(fp);

In this example, a 10000x10 data set of Normal random numbers is written to a data set called data.dat. The
variable names are X01 - X10.

.. seealso:: Functions :func:`open`, :func:`close`, :func:`create`, :func:`readr`, :func:`saved`, :func:`seekr`
