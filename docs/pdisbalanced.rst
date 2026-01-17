pdIsBalanced
==============================================

Purpose
----------------
Checks if each group in a panel dataset covers the maximum time span.

Format
----------------
.. function:: groupIsBalanced = pdIsBalanced(df [, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i \times T_i` rows and K columns.
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

    // Load panel data and take the first 10 rows
    pd = loadd(getGAUSSHome("examples/pd_ab.gdat"));
    pd = pd[1:10,.];

    print pd;

::

              id             year              emp             wage 
               1       1977-01-01        5.0409999        13.151600 
               1       1978-01-01        5.5999999        12.301800 
               1       1979-01-01        5.0149999        12.839500 
               1       1980-01-01        4.7150002        13.803900 
               1       1981-01-01        4.0929999        14.289700 
               1       1982-01-01        3.1659999        14.868100 
               1       1983-01-01        2.9360001        13.778400 
               2       1977-01-01        71.319000        14.790900 
               2       1978-01-01        70.642998        14.103600 
               2       1979-01-01        70.917999        14.953400 

::

    // Check to see if each group is balanced
    is_balanced = pdIsBalanced(pd);
    print is_balanced;

The code above will return:

::

              id         balanced 
               1        1.0000000 
               2        0.0000000


Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

This function evaluates whether each group in a panel dataset spans the maximum time range observed across all groups. 

- If `groupvar` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If `datevar` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains each group and a corresponding indicator (`1` or `0`) to represent whether the group covers the full time span.

.. seealso:: :func:`pdAllBalanced`, :func:`pdbalance`, :func:`pdSummary`
