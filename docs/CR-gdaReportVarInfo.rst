
gdaReportVarInfo
==============================================

Purpose
----------------

Gets information about all of the variables in a GAUSS Data 
Archive and returns it in a string array formatted for printing.

Format
----------------
.. function:: gdaReportVarInfo(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: vinfo (*Nx1 string array*) containing variable information.

Remarks
-------

If you just want to print the information to the window, call
gdaReportVarInfo without assigning the output to a symbol name:

::

                   gdaReportVarInfo(filename);


Examples
----------------

::

    x1 = rndn(100,50);
    x2 = rndn(75,5);
    a = areshape(rndn(10000,1),10|100|10);
    fname = "myfile.gda";
    ret = gdaCreate(fname,1);
    ret = gdaWrite(fname,x1,"x1");
    ret = gdaWrite(fname,x2,"x2");
    ret = gdaWrite(fname,a,"a1");
    gdaReportVarInfo(fname);

produces:

::

    Index Name Type cOrders
      1   x1  matrix 100x50
      2   x2  matrix 75x5
      3   a1  array 10x100x10

Source
------

gdafns.src

.. seealso:: Functions :func:`gdaGetVarInfo`, :func:`gdaGetNames`, :func:`gdaGetTypes`, :func:`gdaGetOrders`
