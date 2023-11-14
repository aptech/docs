
dfWider
==============================================

Purpose
----------------
Converts a GAUSS dataframe in long panel format to wide panel format.


Format
----------------
.. function:: df_wide = dfWider(df_long, names_from, values_from [, pctl])

    :param df_long: A GAUSS dataframe in long panel format.
    :type df_long: Dataframe

    :param names_from: The name(s) of the columns from which the new column names will be created.
    :type names_from: String array

    :param values_from: The values with which to fill the newly created columns.
    :type values_from: String array

    :param pctl: An optional pivotControl structure with the following members:

        .. list-table::
            :widths: auto

            * - pctl.names_prefix
              - String, the characters, if any, that should be added to the front of the newly created variable names.  Default = "", no prefix.
            * - pctl.names_sep_combine
              - String, the characters, if any, that should be added between the tokens when creating the new variable names. Default = "_". NOTE: This can ONLY be used if *names_from* contains multiple variable names.
            * - pctl.id_cols
              - String array, containing the names of the variables that should be used to determine a unique observation. Default = "", meaning the combination of all variables other than those specified by *names_from* and *values_from* will be used.

    :type pctl: Struct

    :return df_wide: The input data converted to wide form.

    :rtype df_wide: Dataframe

Examples
----------------

Example 1
+++++++++++++

::

  // Load long form data
  fname = getGAUSSHome("examples/eagle_nests_long.csv");
  df_long = loadd(fname);

  print df_long;

::

                region                 year            num_nests
               Pacific                 2007               1039.0
               Pacific                 2009              2587.0
             Southwest                 2007                51.0
             Southwest                 2009                176.0
       Rocky Mountains                 2007                200.0
       Rocky Mountains                 2009               338.0

::

  // Specify columns to pull new column names from 
  names_from = "year";
  
  // Specify columns to pull new column values from
  values_from = "num_nests";
  
  // Convert to wide form
  df_wide = dfWider(df_long, names_from, values_from);

  print df_wide;

::

                region                 2007                 2009
               Pacific               1039.0               2587.0
       Rocky Mountains                200.0                338.0
             Southwest                 51.0                176.0


Example 2: Using id_cols and names_prefix
++++++++++++++++++++++++++++++++++++++++++

Let's continue with the data from the previous example, but add a new variable, *report_id*.

::

    // Create new report_id variable
    report_id = { 
        61178,
        73511,
        26219,
        14948,
        67679,
        71635 
     };

    // Add report_id to the front of df_long
    df_long = asdf(report_id, "report_id") ~ df_long;
    print df_long;

::

        report_id          region            year       num_nests
            61178         Pacific            2007            1039
            73511         Pacific            2009            2587
            26219       Southwest            2007              51
            14948       Southwest            2009             176
            67679 Rocky Mountains            2007             200
            71635 Rocky Mountains            2009             338


By default, dfWider will use all variables that are not in either *names_from* or *values_from*
to uniquely identify the observations. This worked well in our previous example, but with the *report_id*
variable, every observation is considered unique. This results in output that is not very useful.

::

  print dfWider(df_long, "year", "num_nests");

::

        report_id          region            2007            2009
            14948       Southwest               .             176
            26219       Southwest              51               .
            61178         Pacific            1039               .
            67679 Rocky Mountains             200               .
            71635 Rocky Mountains               .             338
            73511         Pacific               .            2587


We can use the pivotControl structure to tell :func:`dfWider` to only use the  *region* variable to uniquely identify the observations. And just to show you how it works, we'll also add a prefix to our new year variable names.

::

  // Declare 'pctl' to be a pivotControl structure
  // and fill with default settings
  struct pivotControl pctl;
  pctl = pivotControlCreate();

  // Specify `region` as id col
  pctl.id_cols = "region";
  
  // Specify names prefix
  pctl.names_prefix = "year_";
  
  // Pivot data
  print dfWider(df_long, "year", "num_nests", pctl);

::

           region       year_2007       year_2009
          Pacific            1039            2587
  Rocky Mountains             200             338
        Southwest              51             176


.. seealso:: Functions :func:`dflonger`
