
dfLonger
==============================================

Purpose
----------------
Converts a GAUSS dataframe in wide panel format to long panel format.


Format
----------------
.. function:: df_long = dfLonger(df_wide, columns, names_to, values_to [, ctl])

    :param df_wide: A GAUSS dataframe in wide panel format.
    :type df_wide: Dataframe

    :param columns:  The columns that should be used in the conversion.
    :type columns: String array

    :param names_to: The variable name(s) for the new column(s) containing the wide variable names.
    :type names_to: String array

    :param values_to: The name of the new column containing the values.
    :type values_to: String

    :param pctl        An optional :class:`pivotControl` structure with the following members:

        .. list-table::
            :widths: auto

            * - pctl.names_prefix
              - String, the characters, if any, that should be stripped from the front of the wide variable names before they are assigned to a long column.  Default = "", no prefix.
            * - pctl.names_sep_strip
              - String, the character(s), if any, that mark where the ``names_to`` names should be broken up. Default = "", do not break up ``names_to``.
            * - pctl.names_types
              - Matrix, containing the datatypes for the newly formed long columns. Valid options include: META_TYPE_DATE, META_TYPE_NUMBER, META_TYPE_STRING, META_TYPE_CATEGORY.
            * - pctl.values_drop_missing
              - Scalar, 0 or 1. If set to 1, all rows with missing values will be removed. Default = 0.

    :type pctl: struct

    :return df_long: The input data converted to long form.

    :rtype df_long: Dataframe

Examples
----------------

Example 1: Basic default case
+++++++++++++++++++++++++++++++++

Step one, load the data.

::

    // Load data
    file_name = getGAUSSHome("examples/tiny_car_panel.csv");
    df_wide = loadd(file_name);

    print df_wide;

::

           Years     Cars_compact       Cars_truck         Cars_SUV
      1973-01-01        5.0000000                .        3.0000000
      1974-01-01        2.0000000        1.0000000        9.0000000


Step two, get the names of the columns we want to pivot to long format.

::

    // Get all column names and remove the first column name, 'Years'
    columns = getcolnames(df_wide);
    columns = trimr(columns, 1, 0);
    print columns;

::

    Cars_compact
      Cars_truck
        Cars_SUV


Step three, perform the pivot.

::

    names_to = "Class";
    values_to = "Count";

    df_long = dfLonger(df_wide, columns, names_to, values_to);

After the above code,  *df_long* will equal:

::

         Years            Class            Count
    1973-01-01     Cars_compact        5.0000000
    1973-01-01       Cars_truck                .
    1973-01-01         Cars_SUV        3.0000000
    1974-01-01     Cars_compact        2.0000000
    1974-01-01       Cars_truck        1.0000000
    1974-01-01         Cars_SUV        9.0000000



Example 2: Basic case with `names_prefix`
+++++++++++++++++++++++++++++++++++++++++++++

You may notice that the elements in the *Class* variable from our previous example
contain a redundant prefix, *Cars_*. We can remove that by using the :class:`pivotControl` structure
and setting the `names_prefix` member to *Class_*.

::

     // Load data
     file_name = getGAUSSHome("examples/tiny_car_panel.csv");
     df_wide = loadd(file_name);

     print df_wide;

::

           Years     Cars_compact       Cars_truck         Cars_SUV
      1973-01-01        5.0000000                .        3.0000000
      1974-01-01        2.0000000        1.0000000        9.0000000

::

    // Get all column names and remove the first column name, 'Years'
    columns = getcolnames(df_wide);
    columns = trimr(columns, 1, 0);

    names_to = "Class";
    values_to = "Count";

    // Declare pivotControl structure and fill with default values
    struct pivotControl pctl;
    pctl = pivotControlCreate();

    pctl.names_prefix = "Cars_";

    // Call dfLonger with optional control structure
    df_long = dfLonger(df_wide, columns, names_to, values_to, ctl);


This time, our *Class* variable will not contain the redundant prefix as we see below:

::

         Years       Class            Count
    1973-01-01     compact        5.0000000
    1973-01-01       truck                .
    1973-01-01         SUV        3.0000000
    1974-01-01     compact        2.0000000
    1974-01-01       truck        1.0000000
    1974-01-01         SUV        9.0000000


Example 3: Advanced options
+++++++++++++++++++++++++++++++

In this example, we will use the *names_sep_split* member of the :class:`pivotControl` structure to break up the
variable names. We will also use the *names_types* memember to set the types for the newly created long form variables.

::

  // Load the data
  df_wide = loadd(getGAUSSHome("examples/olympic_vault_wide.csv"));
  print df_wide;   

::

         Country     vault_2012_f     vault_2012_m     vault_2016_f     vault_2016_m 
   United States        48.100000        46.600000        46.900000        45.900000 
          Russia        46.400000        46.900000        45.700000        46.000000 
           China        44.300000        48.300000        44.300000        45.000000

::

  // Get the list of variables to pivot
  // all of them except for the first, 'Country'
  columns =  getcolnames(df_wide);
  columns = columns[2:rows(columns)];

  print columns;

::

    vault_2012_f 
    vault_2012_m 
    vault_2016_f 
    vault_2016_m


Next we will declare our :class:`pivotControl` structure and specify that we want to split the pivot variable names at each underscore.

::
  
  // Declare 'pctl' to be a pivotControl structure
  // and fill with default settings
  struct pivotControl pctl;
  pctl = pivotControlCreate();
  
  // Split the variable names from 'columns', i.e. vault_2012_f, etc
  // every time an underscore is encountered
  pctl.names_sep_split = "_";


Looking at the variable names we just printed earlier, we can see that if we split them at each underscore, we will end up with three separate tokens from each name. Below
we specify a *names_to* for each of these tokens.

::

  names_to = "event" $| "year" $| "gender";
  values_to = "score";


Our final setting is to specify the types we want for each of the *names_to* variables.

::
  
  // Make the following variable type conversions:
  // 'event' to a categorical variable.
  // 'year' to be a date variable.
  // 'gender' to be a categorical variable
  pctl.names_types = META_TYPE_CATEGORY | META_TYPE_DATE | META_TYPE_CATEGORY;


Now we call :func:`dfLonger` with the inputs we created and print out the results.

::
  
  df_long = dfLonger(df_wide, columns, names_to, values_to, pctl); 
  print df_long;

::

         Country            event             year           gender            score 
   United States            vault             2012                f        48.100000 
   United States            vault             2012                m        46.600000 
   United States            vault             2016                f        46.900000 
   United States            vault             2016                m        45.900000 
          Russia            vault             2012                f        46.400000 
          Russia            vault             2012                m        46.900000 
          Russia            vault             2016                f        45.700000 
          Russia            vault             2016                m        46.000000 
           China            vault             2012                f        44.300000 
           China            vault             2012                m        48.300000 
           China            vault             2016                f        44.300000 
           China            vault             2016                m        45.000000

We can verify the column types by using the :func:`getcoltypes` function.

::

  print getcoltypes(df_long, "event"$|"year"$|"gender")

::

            type 
        category 
            date 
        category 
 

.. seealso:: Functions :func:`dfwider`
