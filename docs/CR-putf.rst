
putf
==============================================

Purpose
----------------
Writes the contents of a string to a file.

Format
----------------
.. function:: putf(filename, str, start, len, mode, append)

    :param filename: name of output file.
    :type filename: string

    :param str: data to be written to filename. All or part of *str* may be written out.
    :type str: string 

    :param start: beginning position in str of output string.
    :type start: scalar

    :param len: length of output string.
    :type len: scalar

    :param mode: output mode, (0) ASCII or (1) binary.
    :type mode: scalar

    :param append: file write mode, (0) overwrite or (1) append.
    :type append: scalar

    :returns: ret (*scalar*), return code.

        .. csv-table::
            :widths: auto
    
            "0", "normal return"
            "1", "null file name"
            "2", "file open error"
            "3", "file write error"
            "4", "output string too long"
            "5", "null output string, or illegal mode value"
            "6", "illegal append value"
            "16", "(1) append specified but file did not exist; file was created (warning only)"

Remarks
-------

If *mode* is set to (1) binary, a string of length *len* will be written to
filename. If *mode* is set to (0) ASCII, the string will be output up to
length *len* or until :func:`putf` encounters a ``^Z`` (ASCII 26) in *str*. 
The ``^Z`` will not be written to filename.

If *append* is set to (0) overwrite, the current contents of *filename* will
be destroyed. If *append* is set to (1) append, *filename* will be created
if it does not already exist.

If an error occurs, :func:`putf` will either return an error code or terminate
the program with an error message, depending on the `trap` state. If bit 2
(the 4's bit) of the `trap` flag is 0, :func:`putf` will terminate with an error
message. If bit 2 of the `trap` flag is 1, :func:`putf` will return an error code.
The value of the `trap` flag can be tested with `trapchk`.

Source
------

putf.src

.. seealso:: Functions :func:`getf`

