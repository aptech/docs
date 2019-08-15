
momentd
==============================================

Purpose
----------------

Computes a moment (*x*'*x*) matrix from a GAUSS data set.

Format
----------------
.. function:: m = momentd(dataset, vars)

    :param dataset: name of data set.
    :type dataset: string

    :param vars: 

        .. list-table::
            :widths: auto
            :header-rows: 1

            * - Type
              - Contents
            * - Kx1 string array
              - names of variables
            * - Kx1 numeric vector
              - indices of columns
            * - string
              - Formula string e.g. ``"PAY + WT"`` or ``". - 1"`` (include all variables besides intercept).
                
                These can be any size subset of the variables in the data set, and can be 
                in any order. If a scalar 0 is passed, all columns of the data set will be used.

    :type vars: Kx1 string array or Kx1 numeric vector or string

    :return m: where :math:`M = K + \_\_con`, the moment matrix
        constructed by calculating :math:`X'X` where *X* is the data, with or without a constant vector of ones.

        Error handling is controlled by the low order bit of the `trap` flag.


        :trap 0: terminate with error message
        :trap 1: return scalar error code in *m*

            .. csv-table::
                :widths: auto

                "33", "too many missings"
                "34", "file not found"

    :rtype m: MxM matrix

Global Input
------------

:__con: (*scalar*), default 1.

    .. csv-table::
        :widths: auto

        "1", "a constant term will be added."
        "0", "no constant term will be added."

:__miss: (*scalar*), default 0.

    .. csv-table::
        :widths: auto

        "0", "there are no missing values (fastest)."
        "1", "do listwise deletion; drop an observation if any missings occur in it."
        "2", "do pairwise deletion; this is equivalent to setting missings to 0 when calculating m."

:__row: (*scalar*), the number of rows to read per iteration of the read loop, default 0.

    If 0, the number of rows will be calculated internally.

    If you get an *Insufficient memory* error, or you want the rounding to be
    exactly the same between runs, you can set the number of rows to read
    before calling :func:`momentd`.

Examples
----------------

Using indices of columns
++++++++++++++++++++++++

::

    fname = getGAUSShome() $+ "examples/freqdata.dat";	
    							
    // Calculate statistics on variables in dataset: PAY and WT
    // Specify the index of PAY and WT
    vars = 2|4;				
    m = momentd(fname, vars);
    
    print  m;

After the above code,

::

    400.00000        787.00000        587.98000 
    787.00000        1805.0000        1161.1400 
    587.98000        1161.1400        900.38540

Using names of variables
++++++++++++++++++++++++

::

    fname = getGAUSShome() $+ "examples/freqdata.dat";				
    // Calculate statistics on variables in dataset: PAY and WT
    // Define the names string array of PAY and WT				
    string vars = {"PAY", "WT"};				
    m = momentd(fname, vars );
    print  m;

After the above code,

::

    400.00000        787.00000        587.98000 
    787.00000        1805.0000        1161.1400 
    587.98000        1161.1400        900.38540

Using formula string
++++++++++++++++++++

::

    fname = getGAUSShome() $+ "examples/freqdata.dat";	
    // Define the formula for PAY and WT, remove the intercept (use - 1 )				
    formula_str = "-1 + PAY + WT";	
    										
    // Calculate statistics on variables in dataset: PAY and WT
    m = momentd(fname, formula_str);
    print  m;

After the above code,

::

    1805.0000        1161.1400 
    1161.1400        900.38540

Remarks
-------

-  The supported dataset types are CSV, Excel, HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), 
   Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).
-  Character vectors are supported for backward compatibility, but it has been deprecated.

Source
------

momentd.src

See also
------------

.. seealso:: `Formula String`

