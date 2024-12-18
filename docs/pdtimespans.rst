pdTimeSpans
==============================================

Purpose
----------------
Computes the time spans of variables in panel data.

Format
----------------
.. function:: df_tspans = pdTimeSpans(df [, varlist, groupvar, datevar])

    :param df: Contains long-form panel data with (N_i * T_i) rows and K columns.
    :type df: Dataframe

    :param varlist: Optional, string array specifying a subset of variables to include in the summary.
    :type varlist: String array

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return df_tspans: A dataframe containing the time spans for variables specified in ``varlist``.
    :rtype df_tspans: Dataframe

Examples
----------------

::

    // Import data
    fname = getGAUSSHome("examples/pd_ab.gdat");
    pd_ab = loadd(fname);

    // Call timespane and store results in pd_time 
    pd_time = pdTimeSpans(pd_ab);


Remarks
-------

This function calculates the time spans for variables in panel data, indicating the earliest and latest dates each variable is observed within groups. The result also includes the length of the time span for each variable.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If ``varlist`` is not provided, the function computes time spans for all variables in the dataframe except the `groupvar` and `datevar`.
- If ``groupvar`` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If ``datevar`` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe provides the start and end dates, along with the calculated time span, for each variable.

See also:

.. seealso:: :func:`pdSize`, :func:`pdIsBalanced`, :func:`pdAllBalanced`
