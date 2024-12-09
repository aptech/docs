pdIsBalanced
==============================================

Purpose
----------------
Checks if each group in a panel dataset covers the maximum time span.

Format
----------------
.. function:: groupIsBalanced = pdIsBalanced(df [, groupvar, datevar])

    :param df: Contains long-form (stacked) panel data with (N_i * T_i) rows, where (N_i * T_i) is the total number of observations across all groups, and K columns representing variables. Must contain at least one categorical or string variable for identifying group membership and at least one date variable.
    :type df: Dataframe

    :param groupvar: Optional, specifies the name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, specifies the name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return groupIsBalanced: Indicates whether each group in the panel dataset spans the full time range of the dataset. Each group is assigned a value of 1 if it covers the full time span, 0 otherwise.
    :rtype groupIsBalanced: Dataframe

Examples
----------------

::

    // Example dataframe
    df = asDF("Group Date Variable",
              { "A" 1 10,
                "A" 2 20,
                "B" 1 30,
                "B" 3 40 });

    // Check if each group covers the maximum time span
    groupIsBalanced = pdIsBalanced(df);

The code above will return:

::

    Group    IsBalanced
    -------------------
    A        1
    B        0

Remarks
-------

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

This function evaluates whether each group in a panel dataset spans the maximum time range observed across all groups. 

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains each group and a corresponding indicator (`1` or `0`) to represent whether the group covers the full time span.

See also:

.. seealso:: :func:`pdAllBalanced`, :func:`pdSummary`