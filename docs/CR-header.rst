
header
==============================================

Purpose
----------------

Prints a header for a report.

Format
----------------
.. function:: header(prcnm, dataset, ver)

    :param prcnm: name of procedure that calls :func:`header`.
    :type prcnm: string

    :param dataset: name of data set.
    :type dataset: string

    :param ver: the first element is the major version number of the program, the
        second element is the revision number. Normally this argument will be the version/revision global (*__??_ver*)
        associated with the module within which header is called. This argument will be ignored if set to 0.
    :type ver: 2x1 numeric vector

Examples
----------------

::

    // The procedure name
    proc_name = "myProcedure";

    // The dataset name
    dataset = "mydataset";

    // Version number of program
    ver = 1|1;

    header(proc_name, dataset, ver);

This will print to the screen :

::

  ===============================================================================
  myProcedure  Version 1.00 (R1)                            7/26/2019  12:37 pm
  ===============================================================================
                           Data Set:  mydataset
  -------------------------------------------------------------------------------

Source
------

gauss.src

Global Input
------------

:__header: string, containing one or more of the following letters:

    .. csv-table::
        :widths: auto

        "t", "title is to be printed"
        "l", "lines are to bracket the title"
        "d", "a date and time is to be printed"
        "v", "version number of program is to be printed"
        "f", "file name being analyzed is to be printed"

:__title: string, title for header.
