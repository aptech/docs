
fseek
==============================================

Purpose
----------------
Positions the file pointer in a file.

Format
----------------
.. function:: fseek(f, offs, base)

    :param f: file handle of a file opened with fopen.
    :type f: scalar

    :param offs: offset (in bytes).
    :type offs: scalar

    :param base: base position.
    :type base: scalar

    .. csv-table::
        :widths: auto

        "0", "beginning of file."
        "1", "current position of file pointer."
        "2", "end of file."

    :returns: ret (*scalar*), 0 if successful, 1 if not.

