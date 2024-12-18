pdTimeSpans
==============================================

Purpose
----------------
Computes the time spans of variables in panel data.

Format
----------------
.. function:: df_tspans = pdTimeSpans(df [, varlist, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i x T_i` rows and K columns.
    :type df: Dataframe

    :param varlist: Optional, string array specifying a subset of variables to include in the summary.
    :type varlist: String array

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return df_tspans: A dataframe containing the time spans for variables specified in *varlist*.
    :rtype df_tspans: Dataframe

Examples
----------------

::

    // Import data
    fname = getGAUSSHome("examples/pd_ab.gdat");
    pd_ab = loadd(fname);

    // Take a small sample for the example
    pd_smpl = pd_ab[1:4 8:11,.];
    
    // Print our sample
    print pd_smpl;

::

        id        year        emp       wage 
         1  1977-01-01     5.0410    13.1516 
         1  1978-01-01     5.6000    12.3018 
         1  1979-01-01     5.0150    12.8395 
         1  1980-01-01     4.7150    13.8039 
         2  1977-01-01    71.3190    14.7909 
         2  1978-01-01    70.6430    14.1036 
         2  1979-01-01    70.9180    14.9534 
         2  1980-01-01    72.0310    15.4910  

::

    // Find time spans of variables 
    df_timespans = pdTimeSpans(pd_smpl);

    print df_timespans;

::

            id       Start year         End year        emp Start          emp End       wage Start         wage End 
             1       1977-01-01       1980-01-01       1977-01-01       1980-01-01       1977-01-01       1980-01-01 
             2       1977-01-01       1980-01-01       1977-01-01       1980-01-01       1977-01-01       1980-01-01
Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function calculates the time spans for variables in panel data, indicating the earliest and latest dates each variable is observed within groups. The result also includes the length of the time span for each variable.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If *varlist* is not provided, the function computes time spans for all variables in the dataframe except the *groupvar* and *datevar*.
- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe provides the start and end dates, along with the calculated time span, for each variable.

See also:

.. seealso:: :func:`pdSize`, :func:`pdIsBalanced`, :func:`pdAllBalanced`
