pdIsConsecutive
==============================================

Purpose
----------------
Checks if each group in a panel dataset covers consecutive time periods.

Format
----------------
.. function:: groupIsConsecutive = pdIsConsecutive(df [, groupvar, datevar])

    :param df: Contains long-form (stacked) panel data with (N_i * T_i) rows, where (N_i * T_i) is the total number of observations across all groups, and K columns representing variables. Must contain at least one categorical or string variable for identifying group membership and at least one date variable.
    :type df: Dataframe

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return groupIsConsecutive: Indicates whether each group covers consecutive time periods. Each group is assigned a value of 1 if it is consecutive, 0 otherwise.
    :rtype groupIsConsecutive: Dataframe

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
    is_consecutive = pdisconsecutive(pd_smpl);

    print is_consecutive;

    The above code will return:

::

        id      consecutive 
         1        1.0000000 
         2        1.0000000

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

    // Check to see if the new panel is consecutive
    is_consecutive = pdisconsecutive(new_pd_smpl);

    print is_consecutive;

    The above code will return:  

:: 

            id      consecutive 
             1        1.0000000 
             2        0.0000000 

Remarks
-------

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If ``groupvar`` is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If ``datevar`` is not provided, the function defaults to the first date variable in the dataframe.

The resulting dataframe contains an indicator for each group showing whether it spans consecutive time periods.

See also:

.. seealso:: :func:`pdAllConsecutive`, :func:`pdAllBalanced`, :func:`pdIsBalanced`, :func:`pdSummary`
