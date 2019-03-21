
headermt
==============================================

Purpose
----------------

Prints a header for a report.

Format
----------------
.. function:: headermt(prcnm, dataset, ver, header, title)

    :param prcnm: name of procedure that calls header.
    :type prcnm: string

    :param dataset: name of data set.
    :type dataset: string

    :param ver: the first element is the
        major version number of the program, the second element is the revision number.
        Normally this argument will be the version/revision global (__??_ver)
        associated with the module within which header is called. This argument will be ignored if set to 0.
    :type ver: 2x1 numeric vector

    :param header: containing one or more of the following letters:
    :type header: string

    .. csv-table::
        :widths: auto

        "t", "title is to be printed"
        "l", "lines are to bracket the title"
        "d", "a date and time is to be printed"
        "v", "version number of program is to be printed"
        "f", "file name being analyzed is to be printed"

    :param title: title for header.
    :type title: string



Source
------

gaussmt.src

