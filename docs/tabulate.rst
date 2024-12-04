
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
        E.g ``"df1 ~ df2 + df3"``, ``"df1"`` categories will be reported in rows, separate columns will be returned for each category in ``"df2"`` and ``"df3"``.

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
            * - tbctl.rowPercent
              - Scalar, indicates whether to report row percentages. Set to 1 to report row percentages. Default = 0.
            * - tbctl.columnPercent
              - Scalar, indicates whether to report column percentages. Set to 1 to report column percentages. Default = 0.
    :type tbctl: Struct

    :return df_long: The input data converted to long form.
    :rtype df_long: Dataframe
    
Examples
----------------

Basic usage with a dataframe and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++
            
::

  // Load data
  fname = getGAUSSHome("examples/tips2.dta");
  tips2 = loadd(fname);

  // Two-way table
  call tabulate(tips2, "sex ~ smoker");

This reports the two-way frequency table:

::

    ============================================================
              sex                   smoker                 Total
    ============================================================
                              No            Yes


           Female             55             33               88 
             Male             99             60              159 

            Total            154             93              247
    ============================================================
  
Tabulate can also generate multiple two-way frequency tables using the same data:

::

    // Generate separate tables for sex vs smoker
    // and sex vs time
    call tabulate(tips2, "sex ~ smoker + time");

::

    ============================================================
              sex                   smoker                 Total
    ============================================================
                              No            Yes


           Female             55             33               88 
             Male             99             60              159 

            Total            154             93              247
    ============================================================
              sex                    time                  Total
    ============================================================
                           Lunch         Dinner


           Female             35             53               88 
             Male             33            126              159 

            Total             68            179              247
    ============================================================

Basic usage with a filename and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++
The same tables can be directly generate from the filename

::

   // Load data
   fname = getGAUSSHome("examples/tips2.dta");

   // Two-way table
   call tabulate(fname, "sex ~ smoker");
    
::

    ============================================================
              sex                   smoker                 Total
    ============================================================
                              No            Yes


           Female             55             33               88 
             Male             99             60              159 

            Total            154             93              247
    ============================================================

Tabulate separate dataframe vectors and assign the return value
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

   // Load all variables from the dataset
   tips = loadd(getGAUSShome("examples/tips2.dta"));
   
   // Create separate vectors for each variable
   day = tips[.,"day"];
   time_ = tips[.,"time"];
   
   // Compute the frequency table and assign the result to 't'
   t = tabulate(day, time_);

After running the above code, *t* will contain a dataframe with the frequencies. The totals will not be included:

::

   print t;

::

       day       time_Lunch      time_Dinner 
      Thur        61.000000        2.0000000 
       Fri        7.0000000        12.000000 
       Sat        0.0000000        89.000000 
       Sun        0.0000000        76.000000


Handling unrepresented categories
+++++++++++++++++++++++++++++++++++++

In this example, we will load some data and then take a sample that does not contain any observations of a particular category level.

::

    // Load two variables from the dataset
    tips = loadd(getGAUSShome("examples/tips2.dta"), "smoker + day");
    
    // Take the first 50 observations as a sample
    tips = tips[1:50,.];
    
    // Compute and print the frequency table
    call tabulate(tips, "day ~ smoker");

In this case, the following will be printed:

::

    ============================================================
                day                   smoker               Total
    ============================================================
                                No            Yes
    
    
               Thur              0              0              0 
                Fri              0              0              0 
                Sat             23              0             23 
                Sun             27              0             27 
    
              Total             50              0             50
    ============================================================

In some situations, you may not want to report these unrepresented categories. In that case, you can use the ``unusedLevels`` member of the ``tabControl`` structure to supress those levels.

::

    struct tabControl tbctl;
    tbctl = tabControlCreate();

    // Supress unrepresented categories
    tbctl.unusedLevels = 0;

    // Compute and print the frequency table
    call tabulate(tips, "day ~ smoker", tbctl);


This time the report will omit the unrepresented levels.

::

    =============================================
                day         smoker          Total
    =============================================
                                No
    
    
                Sat             23             23 
                Sun             27             27 
    
              Total             50             50
    =============================================

Reporting row or column percentages
+++++++++++++++++++++++++++++++++++++
The :class:`tabControl` structure members *tbCtl.rowPercent* and *tbCtl.columnPercent* can be used to compute the row percentages or column perecentages, respectively.

::

    struct tabControl tbctl;
    tbctl = tabControlCreate();

    // Report row percentages
    tbctl.rowPercent = 1;

    // Compute and print the frequency table
    call tabulate(tips, "day ~ smoker", tbctl);

This will now report row percentages.

::

  ============================================================
              day                   smoker               Total
  ============================================================
                              No            Yes

              Thur          73.0           27.0            100 
              Fri           21.1           78.9            100 
              Sat           52.8           47.2            100 
              Sun           75.0           25.0            100 

  ============================================================
Table reports row percentages.

.. seealso:: Functions :func:`frequency`, :func:`plotFreq`
