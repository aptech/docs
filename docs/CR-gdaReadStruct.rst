
gdaReadStruct
==============================================

Purpose
----------------

Gets a structure from a GAUSS Data Archive.

Format
----------------
.. function:: gdaReadStruct(filename, varname, structure_type)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of structure instance in the GDA.
    :type varname: string

    :param structure_type: structure type.
    :type structure_type: string

    :returns: instance (*struct*) instance of the struct.

    :returns: **retcode** (*scalar*) - 0 if successful, otherwise, any of the following error codes:

        .. csv-table::
            :widths: auto

            "1", "Null file name."
            "2", "File open error."
            "4", "File read error."
            "5", "Invalid file type."
            "8", "Variable not found."
            "10", "File contains no variables."
            "14", "File too large to be read on current platform."

Remarks
-------

*instance* can be an array of structures.


Examples
----------------

::

    struct mystruct {
       matrix x;
       array a;
    };

    struct mystruct msw;
    msw.x = rndn(500,25);
    msw.a = areshape(rndn(5000,100),10|500|100);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite("myfile.gda",msw,"ms");
    struct mystruct msr;
    { msr, ret } = gdaReadStruct("myfile.gda","ms","mystruct");

.. seealso:: Functions :func:`gdaRead`, :func:`gdaReadSparse`, :func:`gdaWrite`
