
dstat
==============================================

Purpose
----------------

Computes descriptive statistics.

.. NOTE:: This function is deprecated, use :func:`dstatmt` instead.

Format
----------------
.. function:: { vnam, mean, var, std, min, max, valid, mis } = dstat(dataset, vars)

    :param dataset: name of dataset. If *dataset* is null or 0, *vars* will be assumed
        to be a matrix containing the data.
    :type dataset: string

    :param vars: the variables.

        If *dataset* contains the name of a dataset, *vars* will be interpreted as either:

            * A Kx1 character vector containing the names of variables.
            * A Kx1 numeric vector containing indices of variables.
            * A `formula string`. e.g. :code:`"PAY + WT"` or :code:`". - sex"`.

            These can be any size subset of the variables in the dataset and can be in any order. If a scalar 0 is passed, all columns of the dataset will be used.

        If *dataset* is null or 0, *vars* will be interpreted as a NxK matrix, the data on which to compute the descriptive statistics.

    :type vars: string or string array

    :return vnam: the names of the variables used in the statistics.

    :type vnam: Kx1 character vector

    :return mean: means.

    :type mean: Kx1 vector

    :return var: variance.

    :type var: Kx1 vector

    :return std: standard deviation.

    :type std: Kx1 vector

    :return min: minima.

    :type min: Kx1 vector

    :return max: maxima.

    :type max: Kx1 vector

    :return valid: the number of valid cases.

    :type valid: Kx1 vector

    :return mis: the number of missing cases.

    :type mis: Kx1 vector

Global Input
------------

.. data:: __altnam

    matrix, default 0.

    This can be a Kx1 character vector of alternate variable names for the output.

.. data:: __maxbytes

    scalar, the maximum number of bytes to be read per iteration of the read loop. Default = 1e9.

.. data:: __maxvec

    scalar, the largest number of elements allowed in any one matrix. Default = 20000.

.. data:: __miss

    scalar, default 0.

    .. csv-table::
        :widths: auto

        0, "there are no missing values (fastest)."
        1, "listwise deletion, drop a row if any missings occur in it."
        2, "pairwise deletion."

.. data:: __row

    scalar, the number of rows to read per iteration of the read loop.

    if 0, (default) the number of rows will be calculated using `__maxbytes` and `__maxvec`.

.. data:: __output

    scalar, controls output, default 1.

    .. csv-table::
        :widths: auto

        1, "print output table."
        0, "do not print output."

Examples
----------------

Example 1
+++++++++

::

    // Calculate statistics on all variables in dataset
    file = getGAUSShome() $+ "examples/freqdata.dat";

    // Calculate statistics on all variables in dataset: AGE, PAY, sex and WT
    vars = 0;
    { vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid Missing
    -------------------------------------------------------------------------------
    AGE           -----     -----       -----    1.0000   10.0000       400    0
    PAY          1.9675    0.8019      0.6431    1.0000    3.0000       400    0
    sex           -----     -----       -----     -----     -----       400    0
    WT           1.4699    0.3007      0.0904    1.0000    1.9900       400    0

Example 2
+++++++++

::

    file = getGAUSShome() $+ "examples/freqdata.dat";

    // Calculate statistics on just AGE and PAY
    vars = "AGE" $| "PAY";
    { vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid Missing
    -------------------------------------------------------------------------------
    AGE           -----     -----       -----    1.0000   10.0000       400    0
    PAY          1.9675    0.8019      0.6431    1.0000    3.0000       400    0


Example 3
+++++++++

::

    file = getGAUSShome() $+ "examples/freqdata.dat";

    // Calculate statistics on just AGE and PAY using numerical indices
    vars = { 1, 2 };
    { vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);

After the above code,

::

    ------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum   Valid  Missing
    ------------------------------------------------------------------------------
    AGE           -----     -----       -----    1.0000   10.0000     400    0
    PAY          1.9675    0.8019      0.6431    1.0000    3.0000     400    0


Example 4
+++++++++

::

    file = getGAUSShome() $+ "examples/freqdata.dat";

    // Calculate statistics on just AGE and PAY using __miss
    vars = { 1, 2 };

    // Drop rows with missing values
    __miss = 1;
    { vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);

After the above code,

::

    ------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum   Valid  Missing
    ------------------------------------------------------------------------------
    AGE          5.6784    2.9932      8.9593    1.0000   10.0000     398    2
    PAY          1.9623    0.8006      0.6409    1.0000    3.0000     398    2

Example 5
+++++++++

::

    /*
    ** Calculate statistics using formula string and  __miss
    ** Set up a formula string with all variables exclude "sex"
    */
    vars = ". - sex";

    // Drop rows with missing values
    __miss = 1;
    { vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);

After the above code,

::

    -----------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum   Valid Missing
    -----------------------------------------------------------------------------
    AGE          5.6784    2.9932      8.9593    1.0000   10.0000     398    2
    PAY          1.9623    0.8006      0.6409    1.0000    3.0000     398    2
    WT           1.4713    0.3009      0.0906    1.0000    1.9900     398    2


Example 6
+++++++++++

Descriptive statistics on a matrix.

::

    data = { 1 2, 3 4, 5 6, 7 8 };
    call dstat("", data);

After the above code,

::

    -----------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum   Valid Missing
    -----------------------------------------------------------------------------
    X1                4     2.582       6.667         1         7       4    0
    X2                5     2.582       6.667         2         8       4    0


Example 7
+++++++++++

Specify variable names.

::
    
    // Note the use of the matrix concatenation operator, '|'
    // instead of the string concatenation operator, `$|`,
    // makes this a 2x1 character vector
    __altnam = "ALPHA" | "BETA";
    data = { 1 2, 3 4, 5 6, 7 8 };
    call dstat("", data);

After the above code,

::

    -----------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum   Valid Missing
    -----------------------------------------------------------------------------
    ALPHA             4     2.582       6.667         1         7       4    0
    BETA              5     2.582       6.667         2         8       4    0


Remarks
-------

1. If pairwise deletion is used, the minima and maxima will be the true
values for the valid data. The means and standard deviations will be
computed using the correct number of valid observations for each
variable.

2. The supported dataset types are `CSV`, `XLS`, `XLSX`, `HDF5`, `FMT`, `DAT`, `DTA`.

For HDF5 file, the dataset must include `file schema` and both file name and dataset name must be provided, e.g.
:code:`dstat("h5://C:/gauss/examples/testdata.h5/mydata", formula)`

.. seealso:: `Formula String`

Source
------

dstat.src
