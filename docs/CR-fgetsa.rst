
fgetsa
==============================================

Purpose
----------------

Reads lines of text from a file into a string array.

Format
----------------
.. function:: fgetsa(f, numl)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param numl: number of lines to read.
    :type numl: scalar

    :returns: sa (*Nx1 string array*), N <=  numl.



Remarks
-------

fgetsa reads up tonuml lines of text. If fgetsa reaches the end of the
file before reading numl lines, sa will be shortened. Lines are read in
the same manner as fgets, except that no limit is placed on the size of
a line. Thus, fgetsa always returns complete lines of text. Newlines are
retained. If numl is 1, fgetsa returns a string. (This is one way to
read a line from a file without placing a limit on the length of the
line.)

If the file is already at end-of-file when you call fgetsa, your program
will terminate with an error. Use eof in conjunction with fgetsa to
avoid this. If the file was opened for update (see fopen) and you are
switching from writing to reading, don't forget to call fseek or fflush
first, to flush the file's buffer.

If you pass fgetsa the handle of a file opened with open (i.e., a data
set or matrix file), your program will terminate with a fatal error.

