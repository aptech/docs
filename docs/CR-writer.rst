
writer
==============================================

Purpose
----------------
Writes a matrix to a GAUSS data set.

Format
----------------
.. function:: writer(fh, x)

    :param fh: handle of the file that data is to be written to
    :type fh: scalar

    :param x: data
    :type x: NxK matrix

    :returns: y (*scalar*) specifying the number of rows of data actually written to the data set.

Remarks
-------

The file must have been opened with `create`, `open` for append, or `open` for update.

The data in *x* will be written to the data set whose handle is *fh*
starting at the current pointer position in the file. The pointer
position in the file will be updated, so the next call to :func:`writer` will
put the next block of data after the first block. (See `open` and `create`
for the initial pointer positions in the file for reading and writing.)

*x* must have the same number of columns as the data set. :func:`colsf` returns
the number of columns in a data set.

:func:`writer` returns the number of rows actually written to the data set. If *y*
does not equal ``rows(x)``, the disk is probably full.

If the data set is not double precision, the data will be rounded as it
is written out.

If the data contain character elements, the file must be double
precision or the character information will be lost.

If the file being written to is the 2-byte integer data type, then
missing values will be written out as -32768. These will not
automatically be converted to missings on input. They can be converted
with the :func:`miss` function:

::

    x = miss(x,-32768);

Trying to write complex data to a data set that was originally created
to store real data will cause a program to abort with an error message.
(See `create` for details on creating a complex data set.)


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

In this example, a 10000x10 data set of Normal random numbers is written to a data set called *data.dat*. 
The variable names are ``X01 - X10``.

.. seealso:: Functions `open`, `close`, `create`, :func:`readr`, :func:`saved`, :func:`seekr`

