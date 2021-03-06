
gdaReadStruct
==============================================

Purpose
----------------

Gets a structure from a GAUSS Data Archive.

Format
----------------
.. function:: { instance, retcode } = gdaReadStruct(filename, varname, structure_type)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of structure instance in the GDA.
    :type varname: string

    :param structure_type: structure type.
    :type structure_type: string

    :return instance: instance of the struct.

    :rtype instance: struct

    :return retcode: 0 if successful, otherwise, any of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "2", "File open error."
            "4", "File read error."
            "5", "Invalid file type."
            "8", "Variable not found."
            "10", "File contains no variables."
            "14", "File too large to be read on current platform."

    :rtype retcode: scalar

Examples
----------------

::

    // Create structure
    struct mystruct {
       matrix x;
       array a;
    };

    struct mystruct msw;
    msw.x = rndn(500, 25);
    msw.a = areshape(rndn(5000, 100), 10|500|100);

    // Create GDA `myfile`
    ret = gdaCreate("myfile.gda", 1);

    /*
    ** Write structure msw to `myfile`
    ** and store as variable ms
    */
    retcode1 = gdaWrite("myfile.gda", msw, "ms");

    // Declare new instance of mystruct, `msr`
    struct mystruct msr;

    // Read ms from GDA tp msr
    { msr, retcode2 } = gdaReadStruct("myfile.gda", "ms", "mystruct");

Remarks
-------

*instance* can be an array of structures.


.. seealso:: Functions :func:`gdaRead`, :func:`gdaReadSparse`, :func:`gdaWrite`
