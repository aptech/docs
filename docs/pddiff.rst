pdDiff
==============================================

Purpose
----------------
Computes differences of panel data.

Format
----------------
.. function:: delta_pd = pdDiff(df [, k, d, by_time, groupvar, datevar])

    :param df: Contains long-form (stacked) panel data with (N_i * T_i) rows, where (N_i * T_i) is the total number of observations across all groups, and K columns representing variables. Must contain at least one categorical or string variable for identifying group membership and at least one date variable.
    :type df: Dataframe

    :param k: Optional, time lag to use for differencing. Default is 1.
    :type k: Scalar

    :param d: Optional, order of differencing. Default is 1.
    :type d: Scalar

    :param by_time: Optional, indicates whether differences should be computed by checking the differences in the date variable or by row position. Default is 0.
    :type by_time: Scalar

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return delta_pd: A dataframe containing the differenced panel data.
    :rtype delta_pd: Dataframe

Examples
----------------

::

    // Example dataframe
    df = asDF("Group Date Variable",
              { "A" 1 10,
                "A" 2 20,
                "A" 3 30,
                "B" 1 15,
                "B" 2 25,
                "B" 3 35 });

    // Compute first-order differences with default time lag
    delta_pd = pdDiff(df);

The code above will return:

::

    Group    Date    Variable
    -------------------------
    A        2       10
    A        3       10
    B        2       10
    B        3       10

Remarks
-------

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

This function computes differences for panel data based on the specified time lag (`k`) and order of differencing (`d`). Differences can be calculated either by row position or by checking differences in the date variable, depending on the `by_time` argument.

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains the differenced panel data, excluding rows where differencing cannot be performed (e.g., insufficient lag).

See also:

.. seealso:: :func:`pdAllBalanced`, :func:`pdSummary`, :func:`pdIsBalanced`
