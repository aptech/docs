
gdaGetVarInfo
==============================================

Purpose
----------------

Gets information about all of the variables in a GAUSS Data 
Archive and returns it in an array of gdavartable 
structures.

Format
----------------
.. function:: gdaGetVarInfo(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: vtab (*TODO*), Nx1 array of gdavartable
        structures, where N is the number of variables in
        filename, containing the following members:

    .. csv-table::
        :widths: auto

        "vtab[i].name", "string, name of variable."
        "vtab[i].type", "scalar, type of variable."
        "vtab[i].orders", "Mx1 vector or scalar, orders of the variable."

Examples
----------------

::

    //Execute structure definition
    #include gdafns.sdf
    struct gdavartable vtab;
    
    vtab = gdaGetVarInfo("myfile.gda");

Source
++++++

gdafns.src

.. seealso:: Functions :func:`gdaReportVarInfo`, :func:`gdaGetNames`, :func:`gdaGetTypes`, :func:`gdaGetOrders`
