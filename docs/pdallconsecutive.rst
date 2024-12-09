pdAllConsecutive
==============================================

Purpose
----------------
Checks if all groups in a panel dataset are consecutive.

Format
----------------
.. function:: allConsecutive = pdAllConsecutive(df [, groupvar, datevar])

    :param df: Contains long-form (stacked) panel data with (N_i * T_i) rows, where (N_i * T_i) is the total number of observations across all groups, and K columns representing variables. Must contain at least one categorical or string variable for identifying group membership and at least one date variable.
    :type df: Dataframe

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return allConsecutive: Indicates whether all groups in the panel dataset cover consecutive time periods. Returns 1 if the entire panel is consecutive, 0 otherwise.
    :rtype allConsecutive: Scalar

Examples
----------------

::

    // Example dataframe
    df = asDF("Group Date Variable",
              { "A" 1 10,
                "A" 2 20,
                "A" 3 30,
                "B" 1 15,
                "B" 3 25,
                "B" 4 35 });

    // Check if all groups have consecutive time periods
    allConsecutive = pdAllConsecutive(df);

The code above will return:

::

    0

Remarks
-------

This function evaluates whether all groups in a panel dataset span consecutive time periods. It checks for gaps in the time series of each group and determines if the entire panel is consecutive.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

The result is a scalar indicating whether the entire panel dataset is consecutive.

See also:

.. seealso:: :func:`pdIsConsecutive`, :func:`pdAllBalanced`, :func:`pdIsBalanced`
