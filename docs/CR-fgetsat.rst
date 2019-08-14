
fgetsat
==============================================

Purpose
----------------

Reads lines of text from a file into a string array without retaining newlines.

Format
----------------
.. function:: sa = fgetsat(fh, numl)

    :param fh: file handle of a file opened with :func:`fopen`.
    :type fh: scalar

    :param numl: number of lines to read.
    :type numl: scalar

    :returns: **sa** (*Nx1 string array*) - Contains the text read from the file lines specified by the file handle *fh*. :math:`N <= numl`.



Remarks
-------

The :func:`fgetsat` procedure operates identically to :func:`fgetsa`, except that newlines are not
retained as text is read into *sa*.

In general, you don't want to use :func:`fgetsat` on files opened in binary mode
(see :func:`fopen`). The :func:`fgetsat` procedure drops the newlines, but it does NOT drop the
carriage returns that precede them on some platforms. Printing out such
a string array can produce unexpected results.

.. seealso:: Functions :func:`fgetsa`, :func:`fgetst`, :func:`fopen`
