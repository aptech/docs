pdSort
==============================================

Purpose
----------------
Sorts panel data by group and then by date variable.

Format
----------------
.. function:: pd_sorted = pdSort(df [, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i x T_i` rows and K columns.
    :type df: Dataframe

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return pd_sorted: A dataframe containing the sorted panel data.
    :rtype pd_sorted: Dataframe

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function sorts panel data by the specified *groupvar* and *datevar*, ensuring the data is arranged in the correct order for panel data analysis. 

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

Sorting panel data is essential for consistent results in other panel data functions, such as :func:`pdLag`, :func:`pdDiff`, and :func:`pdTimeSpans`.

.. seealso:: :func:`sort`, :func:`sortmc`
