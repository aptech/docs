
gdaDStatMat
==============================================

Purpose
----------------

Computes descriptive statistics on a selection of columns from a matrix located in a GAUSS Data Archive.

Format
----------------
.. function:: gdaDStatMat(dc0, filename, gmat, colind, vnamevar)

    :param dc0: an instance of a :class:`dstatmtControl` structure with the following members:

        .. list-table::
            :widths: auto

            * - *dc0.altnames*
              - Kx1 string array of alternate variable names for the output. Default = ``""``. If set, it must have the same number of rows as *colind*.
            * - *dc0.maxbytes*
              - scalar, the maximum number of bytes to be read per iteration of the read loop. Default = 1e9.
            * - *dc0.maxvec*
              - scalar, the largest number of elements allowed in any one matrix. Default = 20000.
            * - *dc0.miss*
              - scalar, one of the following:

                  :0: There are no missing values (fastest).
                  :1: Listwise deletion, drop a row if any missings occur in it.
                  :2: Pairwise deletion.

                Default = 0.

            * - *dc0.output*
              - scalar, one of the following:

                  :0: Do not print output table.
                  :1: Print output table.

                Default = 1.

            * - *dc0.row*
              - scalar, the number of rows of *vnamevar* to be read per iteration of the read loop. If 0, (default) the number of rows will be calculated using *dc0.maxbytes* and *dc0.maxvec*.

    :type dc0: struct

    :param filename: name of data file.
    :type filename: string

    :param gmat: name of matrix or index of matrix.
    :type gmat: string or scalar

    :param colind: indices of columns in variable to use.
    :type colind: Kx1 vector

    :param vnamevar: name of the string containing the variable names in the matrix or
        index of the string containing the variable names in the matrix.
    :type vnamevar: string or scalar

    :returns: **dout** (*struct*) - instance of :class:`dstatmtOut` struct with the following members:

        .. list-table::
            :widths: auto

            * - *dout.vnames*
              - Kx1 string array, the names of the variables used in the statistics.
            * - *dout.mean*
              - Kx1 vector, means.
            * - *dout.var*
              - Kx1 vector, variance.
            * - *dout.std*
              - Kx1 vector, standard deviation.
            * - *dout.min*
              - Kx1 vector, minima.
            * - *dout.max*
              - Kx1 vector, maxima.
            * - *dout.valid*
              - Kx1 vector, the number of valid cases.
            * - *dout.missing*
              - Kx1 vector, the number of missing cases.
            * - *dout.errcode*
              - scalar, error code, 0 if successful, otherwise one of the following:

                  :1: No GDA indicated.
                  :3: Variable must be Nx1.
                  :4: Not implemented for complex data.
                  :5: Variable must be type matrix.
                  :7: Too many missings, no data left after packing.
                  :9: *altnames* member of :class:`dstatmtControl` structure wrong size.
                  :11: Data read error.

Remarks
-------

Set *colind* to a scalar 0 to use all of the columns in *vnamevar*.

*vnamevar* must either reference an Mx1 string array variable containing
variable names, where M is the number of columns in the data set
variable, or be set to a scalar 0. If *vnamevar* references an Mx1 string
array variable, then only the elements indicated by *colind* will be used.
Otherwise, if *vnamevar* is set to a scalar 0, then the variable names :code:`"X1, X2, ..., XK"` for
the output will be generated automatically, unless the
alternate variable names are set explicitly in the *dc0.altnames* member of
the :class:`dstatmtControl` structure.

If pairwise deletion is used, the minima and maxima will be the true
values for the valid data. The means and standard deviations will be
computed using the correct number of valid observations for each
variable.


Examples
----------------
In order to create a real, working example that you can use, you must first create a sample GAUSS Data Archive with the code below.

::

    // Create an example GAUSS Data Archive
    ret = gdaCreate("myfile.gda", 1);

    // Add a variable 'A' which is a 10x5 random normal matrix
    ret = gdaWrite("myfile.gda", rndn(10, 5), "A");

    // Add a variable 'COLS' which is a 5x1 string array
    string vnames = { "X1", "X2", "X3", "X4", "X5" };
    ret = gdaWrite("myfile.gda", vnames, "COLS");

This code above will create a GAUSS Data Archive containing two variables, the GAUSS matrix ``A``
containing the data and ``COLS`` which contains the names for the columns of the matrix ``A`` which
are the model variables (``X1, X2,...``).

The code below computes the statistics on each of the columns of the matrix ``A``.

::

    /*
    ** Declare instance of the
    ** dstatmtControl structure
    */
    struct dstatmtControl dc0;
    dc0 = dstatmtControlCreate;

    // Indices of variables to evaluate
    colind = { 1, 2, 3, 4, 5 };

    // Declare output structure
    struct dstatmtout dout;
    dout = gdaDStatMat(dc0, "myfile.gda", "A", colind, "COLS" );

The final input to *gdaDStatMat* above tells the function the names to use for the columns of ``A``. In this example, you can reference the ``COLS`` variable by name as you see in the example below. Alternatively, you can access this variable by index. Since ``COLS`` is the second variable in the GAUSS Data Archive created at the start of this example, the following is equivalent to the last line above:

::

    dout = gdaDStatMat(dc0, "myfile.gda", "A", colind, 2 );

If you wanted to calculate the statistics on just the first, third and fifth columns of *A*:

::

    colind = { 1, 3, 5 };
    dout = gdaDStatMat(dc0, "myfile.gda", "A", colind, "COLS" );

Notice in these lines above that ``COLS`` still contains all of the variable names i.e. ``X1, X2, X3, X4, X5``. ``COLS`` should always contain the full list of all variables in the matrix ``A``.

Source
------

gdadstat.src

.. seealso:: Functions :func:`gdaDStat`, :func:`dstatmtControlCreate`
