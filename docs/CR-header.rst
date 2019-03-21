
header
==============================================

Purpose
----------------

Prints a header for a report.

Format
----------------
.. function:: header(prcnm, dataset, ver)

    :param prcnm: name of procedure that calls header.
    :type prcnm: string

    :param dataset: name of data set.
    :type dataset: string

    :param ver: the first element is the major version number of the program, the
        second element is the revision number. Normally this argument will be the version/revision global (__??_ver)
        associated with the module within which header is called. This argument will be ignored if set to 0.
    :type ver: 2x1 numeric vector

