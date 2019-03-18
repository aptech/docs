
fgetsat
==============================================

Purpose
----------------

Reads lines of text from a file into a string array.

Format
----------------
.. function:: fgetsat(f,  numl)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param numl: number of lines to read.
    :type numl: scalar

    :returns: sa (*Nx1 string array*), N <=  numl.

