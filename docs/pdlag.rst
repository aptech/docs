pdLag
==============================================

Purpose
----------------
Computes lags of panel data.

Format
----------------
.. function:: l_pd = pdLag(df [, k, by_time, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i x T_i` rows and K columns.
    :type df: Dataframe

    :param k: Optional, time lag to compute. Default is 1.
    :type k: Scalar

    :param by_time: Optional, indicates whether lags should be computed by checking the differences in the date variable or by row position. Default is 0.
    :type by_time: Scalar

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return l_pd: A dataframe containing the lagged panel data.
    :rtype l_pd: Dataframe

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

    // Compute first lag 
    lag_pd = pdLag(pd_smpl);

    // Print differenced data
    print lag_pd;

::

        id             year              emp             wage 
         1       1977-01-01                .                . 
         1       1978-01-01        5.0409999        13.151600 
         1       1979-01-01        5.5999999        12.301800 
         1       1980-01-01        5.0149999        12.839500 
         2       1977-01-01                .                . 
         2       1978-01-01        71.319000        14.790900 
         2       1979-01-01        70.642998        14.103600 
         2       1980-01-01        70.917999        14.953400

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function computes lags for panel data based on the specified time lag (`k`). Lags can be calculated either by row position or by checking differences in the date variable, depending on the `by_time` argument.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains lagged values for the specified variables, with rows where lags cannot be computed excluded.

.. seealso:: :func:`pdDiff`, :func:`pdAllBalanced`, :func:`pdIsBalanced`
