
tabulate
==============================================

Purpose
----------------

Generates and returns two-way tables of frequencies.

Format
----------------
.. function:: table_df = tabulate(data, formula [, tbCtl])
              table_df = tabulate(filename, formula [, tbCtl])
              table_df = tabulate(df1, df2 [, tbCtl])
              
    :param data: Contains variables specified in *formula*.
    :type data: NxK dataframe

    :param formula: formula string.
        E.g ``"df ~ df2 + df3"``, ``"df1"`` categories will be reported in rows, separate columns will be returned for each category in ``"df1"`` and ``"df2"``.

    :type formula: string

    :param filename: Name of file storing variables specifiec in *formula*.
    :type filename: string
            
    :param df1: Contains variable whose categories will be reported in the rows of the frequency table. 
    :type df1: Nx1 dataframe
            
    :param df2: Contains variables whose categories will be reported in the cols of the frequency table. 
    :type df2: NxK dataframe

    :param tbctl: An optional :class:`tabControl` structure with the following members:

        .. list-table::
            :widths: auto

            * - tbctl.exclude
              - String, the categories to be excluded from table counts. Totals will not include observations in excluded categories. 
            * - tbctl.unusedLevels
              - Scalar, indicates whether to include unused levels in table. Set to 0 to remove unused levels from the table. Default = 1.
          
    :type tbctl: Struct

    :return df_long: The input data converted to long form.
    :rtype df_long: Dataframe
    
Examples
----------------

Basic usage with a dataset and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++
            
::

  // Load data
  fname = getGAUSSHome("examples/tips2.dta");
  tips2 = loadd(fname);

  // One-way table
  call tabulate(tips2, "sex ~ smoker");

::

This reports the one-way frequency table:

::

Tabulate can also generate a two-way frequency table using the same data:

::

    // Two-way table
    call tabulate(tips2, "sex ~ smoker + time");

::

Basic usage with a filename and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++
The same tables can be directly generate from the filename

::

   // Load data
   fname = getGAUSSHome("examples/tips2.dta");

   // One-way table
   call tabulate(fname, "sex ~ smoker");
    

.. seealso:: Functions :func:`frequency`, :func:`plotFreq`
