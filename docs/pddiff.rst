pdDiff
==============================================

Purpose
----------------
Computes differences of panel data.

Format
----------------
.. function:: delta_pd = pdDiff(df [, k, d, by_time, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i \times T_i` rows and K columns.
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

    // Compute first-order differences with default time lag
    delta_pd = pdDiff(pd_smpl);

    // Print differenced data
    print delta_pd;


The code above will return:

::

        id             year              emp             wage 
         1       1977-01-01                .                . 
         1       1978-01-01       0.55900002      -0.84980011 
         1       1979-01-01      -0.58500004       0.53770065 
         1       1980-01-01      -0.29999971       0.96439934 
         2       1977-01-01                .                . 
         2       1978-01-01      -0.67600250      -0.68730068 
         2       1979-01-01       0.27500153       0.84980011 
         2       1980-01-01        1.1129990       0.53760052

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

This function computes differences for panel data based on the specified time lag (*k*) and order of differencing (*d*). Differences can be calculated either by row position or by checking differences in the date variable, depending on the `by_time` argument.

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains the differenced panel data, excluding rows where differencing cannot be performed (e.g., insufficient lag).

See also:

.. seealso:: :func:`pdLag`
