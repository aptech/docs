pdBalance
==============================================

Purpose
----------------
Balances an unbalanced panel, ensuring that each group has the same time periods. This can be accomplished by filling in or dropping observations.

Format
----------------
.. function:: df_balanced = pdBalance(df [, balance_type, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i \times T_i` rows and K columns.
    :type df: Dataframe

    :param balance_type: Optional, specifies the method used to balance the panel. Default = ``"fill"``.
    :type balance_type: String

        ================ ==============================================================
        "fill"           Each group will have all time periods. Groups that are missing a time period will have them added and data columns filled with missing values.
        "shared_times"   Time periods that are not shared by all groups will be removed.
        ================ ==============================================================

    :param groupvar: Optional, specifies the name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, specifies the name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return df_balanced: Indicates whether each group in the panel dataset spans the full time range of the dataset. Each group is assigned a value of 1 if it covers the full time span, 0 otherwise.
    :rtype df_balanced: Dataframe

Examples
----------------

Example 1: Basic panel balancing with default ``"fill"`` method.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load panel data and select the data from rows 2, 3, 8 and 9
    pd = loadd(getGAUSSHome("examples/pd_ab.gdat"));
    pd = pd[2:3 8:9,.];

    print pd;

::

              id             year              emp             wage 
               1       1978-01-01        5.5999999        12.301800 
               1       1979-01-01        5.0149999        12.839500 
               2       1977-01-01        71.319000        14.790900 
               2       1978-01-01        70.642998        14.103600

In the printout above, we can see that group 1 has 1978 and 1979, while group 2 has 1977 and 1978.

::

    // Balance the panel using the default 'fill' method
    df_balanced = pdBalance(pd);
    print df_balanced;

After running the above code, each ID in our balanced panel now has all available time periods.

::

              id             year              emp             wage 
               1       1977-01-01                .                . 
               1       1978-01-01        5.5999999        12.301800 
               1       1979-01-01        5.0149999        12.839500 
               2       1977-01-01        71.319000        14.790900 
               2       1978-01-01        70.642998        14.103600 
               2       1979-01-01                .                .

Example 2: Basic panel balancing with default ``"shared_times"`` method.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load panel data and select the data from rows 2, 3, 8 and 9
    pd = loadd(getGAUSSHome("examples/pd_ab.gdat"));
    pd = pd[2:3 8:9,.];

    print pd;

::

              id             year              emp             wage 
               1       1978-01-01        5.5999999        12.301800 
               1       1979-01-01        5.0149999        12.839500 
               2       1977-01-01        71.319000        14.790900 
               2       1978-01-01        70.642998        14.103600

In the printout above, we can see that the only date that both group 1 and group 2 have is 1978.

::

    // Balance the panel using the 'shared_times' method
    df_balanced = pdBalance(pd, "shared_times");
    print df_balanced;

After running the above code, only the observations whose time periods were present for both ID's have been kept.

::

              id             year              emp             wage 
               1       1978-01-01        5.5999999        12.301800 
               2       1978-01-01        70.642998        14.103600


Example 3: Panel balancing with multiple date and group variables
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

By default, :func:`pdBalance` assumes that the first categorical variable in the dataframe is the group variable and that
the first date variable is the date variable describing the panel.

This example shows how to specify which variables to treat as the group and date variable.

::

    // Load panel data and select the data from rows 2, 3, 8 and 9
    pd = loadd(getGAUSSHome("examples/pd_ab.gdat"));
    pd = pd[2:3 8:9,.];

    // Create a categorical variable indicating the sector
    sector = reshape("Healthcare", rows(pd), 1);
    sector = asdf(sector, "sector");

    // Create a date vector indicating the time data was collected
    collect_date = reshape(asdate("2025-03-26"), rows(pd), 1);
    collect_date = asdf(collect_date, "collected");

    // Add new date and categorical variable to the front
    // of our panel dataframe
    pd = collect_date ~ sector ~ pd;

    print pd;

::

       collected           sector       id             year              emp             wage 
      2025-03-26       Healthcare        1       1978-01-01        5.5999999        12.301800 
      2025-03-26       Healthcare        1       1979-01-01        5.0149999        12.839500 
      2025-03-26       Healthcare        2       1977-01-01        71.319000        14.790900 
      2025-03-26       Healthcare        2       1978-01-01        70.642998        14.103600


We still want to use `id` and `year` as the group and date variables. However, by default :func:`pdbalance` will 
assume that the first categorical variable, `sector`, is the group variable and that the first date variable, 
`collected` is the date variable. 

::

    // Balance the panel using the 'fill' method and
    // specifying the group and date variables to use
    df_balanced = pdBalance(pd, "fill", "id", "year");
    print df_balanced;

After running the above code, each ID in our balanced panel now has all available time periods.

::

       collected           sector       id             year              emp             wage 
               .                .        1       1977-01-01                .                . 
      2025-03-26       Healthcare        1       1978-01-01        5.5999999        12.301800 
      2025-03-26       Healthcare        1       1979-01-01        5.0149999        12.839500 
      2025-03-26       Healthcare        2       1977-01-01        71.319000        14.790900 
      2025-03-26       Healthcare        2       1978-01-01        70.642998        14.103600 
               .                .        2       1979-01-01                .                .


Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

This function evaluates whether each group in a panel dataset spans the maximum time range observed across all groups. 

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains each group and a corresponding indicator (`1` or `0`) to represent whether the group covers the full time span.

.. seealso:: :func:`pdAllBalanced`, :func:`pdSummary`
