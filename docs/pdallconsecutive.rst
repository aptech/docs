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

If your group variable is the first categorical variable in your dataframe and the date variable is a GAUSS date variable and not just a numeric column, you can just pass in the panel dataframe and GAUSS will locate the group and date variables for you.

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

    // Check to see if the panel is consecutive
    is_consecutive = pdallconsecutive(pd_smpl);

    print is_consecutive;

    The above code will return:

::

     1.000

Now, let's take a different sample and check for consecutiveness. 

::

    // Take a small sample for the example
    new_pd_smpl = pd_ab[1:4 8 10:11,.];
    
    // Print our sample
    print new_pd_smpl;

::

            id             year              emp             wage 
             1       1977-01-01        5.0409999        13.151600 
             1       1978-01-01        5.5999999        12.301800 
             1       1979-01-01        5.0149999        12.839500 
             1       1980-01-01        4.7150002        13.803900 
             2       1977-01-01        71.319000        14.790900 
             2       1979-01-01        70.917999        14.953400 
             2       1980-01-01        72.030998        15.491000 

In the new sample, group 2 has a gap in observations. It is missing an observation for 1978.

::

    // Check to see if the  new panel is consecutive
    is_consecutive = pdallconsecutive(new_pd_smpl);

    print is_consecutive;

    The above code will return:  

::

    0.000
    
Remarks
-------

This function evaluates whether all groups in a panel dataset span consecutive time periods. It checks for gaps in the time series of each group and determines if the entire panel is consecutive.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If ``groupvar`` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If ``datevar`` is not provided, the function defaults to the first date variable in the dataframe.

The result is a scalar indicating whether the entire panel dataset is consecutive.

See also:

.. seealso:: :func:`pdIsConsecutive`, :func:`pdAllBalanced`, :func:`pdIsBalanced`
