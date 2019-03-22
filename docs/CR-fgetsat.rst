
fgetsat
==============================================

Purpose
----------------

Reads lines of text from a file into a string array.

Format
----------------
.. function:: fgetsat(f, numl)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param numl: number of lines to read.
    :type numl: scalar

    :returns: sa (*Nx1 string array*), N <=  numl.



Remarks
-------

fgetsat operates identically to fgetsa, except that newlines are not
retained as text is read into sa.

In general, you don't want to use fgetsat on files opened in binary mode
(see fopen). fgetsat drops the newlines, but it does NOT drop the
carriage returns that precede them on some platforms. Printing out such
a string array can produce unexpected results.

.. seealso:: Functions :func:`fgetsa`, :func:`fgetst`, :func:`fopen`
