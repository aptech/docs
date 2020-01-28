
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

    :param dataset: name of dataset.
    :type dataset: string

    :param ver: the first element is the
        major version number of the program, the second element is the revision number.
        Normally this argument will be the version/revision global (*__??_ver*)
        associated with the module within which :func:`header` is called. This argument will be ignored if set to 0.
    :type ver: 2x1 numeric vector

    :param header: contains one or more of the following letters:

        .. csv-table::
            :widths: auto

            "t", "title is to be printed"
            "l", "lines are to bracket the title"
            "d", "a date and time is to be printed"
            "v", "version number of program is to be printed"
            "f", "file name being analyzed is to be printed"

    :type header: string

    :param title: title for header.
    :type title: string

Examples
----------------

::

        // The procedure name
        proc_name = "myProcedure";

        // The dataset name
        dataset = "mydataset";

        // Version number of program
        ver = 1|1;

        // Define title
        title = "My procedure is the best";

        /*
        ** Specify header design to include
        ** title, brackets, and date and time
        ** and filename
        */
        header = "tlvf"

        headermt(proc_name, dataset, ver, header, title);

This will print to the screen :

    ::

      ===============================================================================
                         My procedure is the best
      ===============================================================================
      myProcedure  Version 1.00 (R1)
      ===============================================================================
                             dataset:  mydataset
      -------------------------------------------------------------------------------

Source
------

gaussmt.src
