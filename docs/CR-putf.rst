
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

    :param str: string to be written to filename. All or
        part of str may be written out.
    :type str: TODO

    :param start: beginning position in str of output
        string.
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

