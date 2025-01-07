pdSort
==============================================

Purpose
----------------
Sorts panel data by group and then by date variable.

Format
----------------
.. function:: pd_sorted = pdSort(df [, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i \times T_i` rows and K columns.
    :type df: Dataframe

    :param groupvar: Optional, name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return pd_sorted: A dataframe containing the sorted panel data.
    :rtype pd_sorted: Dataframe

Examples
-----------

::

    // Import data
    fname = getGAUSSHome("examples/pd_ab.gdat");
    pd_ab = loadd(fname);
    
    // Take out of order sample
    pd_smpl = pd_ab[3 10 8 4 2 9,.];
    print pd_smpl;

::

              id             year              emp             wage 
               1       1979-01-01        5.0149999        12.839500 
               2       1979-01-01        70.917999        14.953400 
               2       1977-01-01        71.319000        14.790900 
               1       1980-01-01        4.7150002        13.803900 
               1       1978-01-01        5.5999999        12.301800 
               2       1978-01-01        70.642998        14.103600


::

    // Sort sample
    pd_srted = pdSort(pd_smpl);

    print pd_srted;

::

              id             year              emp             wage 
               1       1978-01-01        5.5999999        12.301800 
               1       1979-01-01        5.0149999        12.839500 
               1       1980-01-01        4.7150002        13.803900 
               2       1977-01-01        71.319000        14.790900 
               2       1978-01-01        70.642998        14.103600 
               2       1979-01-01        70.917999        14.953400

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function sorts panel data by the specified *groupvar* and *datevar*, ensuring the data is arranged in the correct order for panel data analysis. 

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

Sorting panel data is essential for consistent results in other panel data functions, such as :func:`pdLag`, :func:`pdDiff`, and :func:`pdTimeSpans`.

.. seealso:: :func:`sortc`, :func:`sortmc`
