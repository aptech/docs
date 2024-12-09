pdIsConsecutive
==============================================

Purpose
----------------
Checks if each group in a panel dataset covers consecutive time periods.

Format
----------------
.. function:: groupIsConsecutive = pdIsConsecutive(df [, groupvar, datevar])

    :param df: A dataframe containing long-form (stacked) panel data with (N_i * T_i) rows, where (N_i * T_i) is the total number of observations across all groups, and K columns representing variables. Must contain at least one categorical or string variable for identifying group membership and at least one date variable.
    :type df: Dataframe

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return groupIsConsecutive: A dataframe indicating whether each group covers consecutive time periods. Each group is assigned a value of 1 if it is consecutive, 0 otherwise.
    :rtype groupIsConsecutive: Dataframe

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

    // Check if each group has consecutive time periods
    groupIsConsecutive = pdIsConsecutive(df);

The code above will return:

::

    Group    IsConsecutive
    ----------------------
    A        1
    B        0

Remarks
-------

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains an indicator for each group showing whether it spans consecutive time periods.

See also:

.. seealso:: :func:`pdAllConsecutive`, :func:`pdAllBalanced`, :func:`pdIsBalanced`, :func:`pdSummary`
