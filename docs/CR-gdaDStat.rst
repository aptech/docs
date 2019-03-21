
gdaDStat
==============================================

Purpose
----------------

Computes descriptive statistics on multiple Nx1 variables in a GAUSS Data Archive.

Format
----------------
.. function:: gdaDStat(dc0, filename, vars)

    :param dc0: 
    :type dc0: an instance of a dstatmtControl structure with the following members:

    .. csv-table::
        :widths: auto

        "dc0.altnames", "Kx1 string array of alternate variable names for the output. Default = ''''."
        "dc0.maxbytes", "scalar, the maximum number of bytes to be read per iteration of the read loop. Default = 1e9."
        "dc0.maxvec", "scalar, the largest number of elements allowed in any one matrix. Default = 20000."
        "dc0.miss", "scalar, one of the following:"
        "", "0", "There are no missing values (fastest)."
        "", "1", "Listwise deletion, drop a row if any missings occur in it."
        "", "2", "Pairwise deletion."
        "", "Default = 0."
        "dc0.output", "scalar, one of the following:"
        "", "0", "Do not print output table."
        "", "1", "Print output table."
        "", "Default = 1."
        "dc0.row", "scalar, the number of rows of  var to be read per iteration of the read loop.If 0, (default) the number of rows will be calculated using dc0.maxbytes and dc0.maxvec."

    :param filename: name of data file.
    :type filename: string

    :param vars: names of variables
        
        - or -
        
        Kx1 vector, indices of variables.
    :type vars: Kx1 string array

    :returns: dout (*TODO*), an instance of a dstatmtOut structure with the following members:

    .. csv-table::
        :widths: auto

        "dout.vnames", "Kx1 string array, the names of the variables used in the statistics."
        "dout.mean", "Kx1 vector, means."
        "dout.var", "Kx1 vector, variance."
        "dout.std", "Kx1 vector, standard deviation."
        "dout.min", "Kx1 vector, minima."
        "dout.max", "Kx1 vector, maxima."
        "dout.valid", "Kx1 vector, the number of valid cases."
        "dout.missing", "Kx1 vector, the number of missing cases."
        "dout.errcode", "scalar, error code, 0 if successful, or one of the following:"
        "", "1", "No GDA indicated."
        "", "4", "Not implemented for complex data."
        "", "5", "Variable must be type matrix."
        "", "6", "Too many variables specified."
        "", "7", "Too many missings - no data left after packing."
        "", "8", "Name variable wrong size."
        "", "9", "altnames member of dstatmtControl structure wrong size."
        "", "11", "Data read error."

Examples
----------------

::

    struct dstatmtControl dc0;
    struct dstatmtOut dout;
    
    //Set structure to default values
    dc0 = dstatmtControlCreate();
    
    vars = { 1,4,5,8 };
    dout = gdaDStat(dc0,"myfile.gda",vars);

This example computes descriptive statistics on the
first, fourth, fifth and eighth variables in myfile.gda.

Source
++++++

gdadstat.src

.. seealso:: Functions :func:`gdaDStatMat`, :func:`dstatmtControlCreate`

multiple variables GDA descriptive statistics
