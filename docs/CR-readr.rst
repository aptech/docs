
readr
==============================================

Purpose
----------------
Reads a specified number of rows of data from a GAUSS data set
(*.dat*) file or a GAUSS matrix (*.fmt*) file.

Format
----------------
.. function:: readr(f1, r)

    :param f1: file handle of an open file.
    :type f1: scalar

    :param r: number of rows to read.
    :type r: scalar

    :returns: y (*NxK matrix*), the data read from the file.

Remarks
-------

The first time a :func:`readr` statement is encountered, the first *r* rows will
be read. The next time it is encountered, the next *r* rows will be read
in, and so on. If the end of the data set is reached before *r* rows can
be read, then only those rows remaining will be read.

After the last row has been read, the pointer is placed immediately
after the end of the file. An attempt to read the file in these
circumstances will cause an error message.

To move the pointer to a specific place in the file use :func:`seekr`.


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
entire data set. ``eof(dt)`` returns 1 when the end of the
data set is encountered.

.. seealso:: Functions :func:`open`, :func:`create`, :func:`writer`, :func:`seekr`, :func:`eof`

