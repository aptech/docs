pdAllBalanced
==============================================

Purpose
----------------
Checks if a panel dataset is balanced and returns 1 if balanced, 0 otherwise.

Format
----------------
.. function:: isBalanced = pdAllBalanced(df [, groupvar, datevar])

    :param df: Contains long-form (stacked) panel data with (N_i * T_i) rows, where (N_i * T_i) is the total number of observations across all groups, and K columns representing variables. Must contain at least one categorical or string variable for identifying group membership and at least one date variable.
    :type df: Data frame

    :param groupvar: Optional, specifies the name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, specifies the name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return isBalanced: Indicates if the panel dataset is balanced. Returns 1 if balanced, 0 otherwise.
    :rtype isBalanced: Scalar

Examples
----------------

::

    // Example dataframe
    df = asDF("Group Date Variable",
              { "A" 1 10,
                "A" 2 20,
                "B" 1 30,
                "B" 2 40 });

    // Check if the panel is balanced
    isBalanced = pdAllBalanced(df);

The code above will return:

::

    1

Remarks
-------

A balanced panel dataset contains the same number of observations for each group. :func:`pdAllBalanced` examines the provided dataset to determine if it meets this condition.

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

For datasets that are not balanced, :func:`pdAllBalanced` returns 0.

See also:

.. seealso:: :func:`pdSummary`, :func:`pdSize`
