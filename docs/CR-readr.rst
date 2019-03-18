
readr
==============================================

Purpose
----------------
Reads a specified number of rows of data from a GAUSS data set
(.dat) file or a GAUSS matrix (.fmt) file.

Format
----------------
.. function:: readr(f1, r)

    :param f1: file handle of an open file.
    :type f1: scalar

    :param r: number of rows to read.
    :type r: scalar

    :returns: y (*NxK matrix*), the data read from the file.

Examples
----------------

::

    open dt = dat1.dat;
    m = 0;
     
    do until eof(dt);
       x = readr(dt,400);
       m = m + moment(x,0);
    endo;
     
    dt = close(dt);

This code reads data from a data set 400 rows at a time. The moment
matrix for each set of rows is computed and added to the sum of the
previous moment matrices. The result is the moment matrix for the 
entire data set. eof(dt) returns 1 when the end of the
data set is encountered.

.. seealso:: Functions :func:`open`, :func:`create`, :func:`writer`, :func:`seekr`, :func:`eof`
