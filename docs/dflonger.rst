
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

    :param pctl        An optional pivotControl structure with the following members:

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

    df_long = dfLonger(df_wide, columns, names_to, values_to);

::

         Years            Class            Count
    1973-01-01     Cars_compact        5.0000000
    1973-01-01       Cars_truck                .
    1973-01-01         Cars_SUV        3.0000000
    1974-01-01     Cars_compact        2.0000000
    1974-01-01       Cars_truck        1.0000000
    1974-01-01         Cars_SUV        9.0000000



Example 2: Basic case with 'names_prefix'
+++++++++++++++++++++++++++++++++++++++++++++

You may notice that the elements in the 'Class' variable from our previous example
contain a redundant prefix, 'Cars_'. We can remove that by using the pivotControl structure
and setting the 'names_prefix' member to 'Class_'.

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

 This time, our 'Class' variable will not contain the redundant prefix as we see below:

::

         Years       Class            Count
    1973-01-01     compact        5.0000000
    1973-01-01       truck                .
    1973-01-01         SUV        3.0000000
    1974-01-01     compact        2.0000000
    1974-01-01       truck        1.0000000
    1974-01-01         SUV        9.0000000


.. seealso:: Functions :func:`dfwider`
