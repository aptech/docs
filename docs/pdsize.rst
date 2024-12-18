pdSize
==============================================

Purpose
----------------
Provides size description of a panel dataset including the number of groups, number of time observations for each group.

Format
----------------
.. function:: { num_grps, T, balanced } = pdSize(df, groupvar)

    :param df: Contains long-form panel data with :math:`N_i x T_i` rows and K columns.
    :type df: Dataframe

    :param groupvar: A column vector indicating group membership for panel observations.
    :type groupvar: String

    :return num_grps: Number of groups in the panel.        
    :rtype num_grps: Scalar

    :return T: Containing number of time observations for each group. 
    :rtype T: Vector

    :return balanced: Indicator if panel is balanced, report 1 for balanced data, 0 othewise.
    :rtype: Scalar

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

    
    // Check size of panel 
    { num_grps, T_2, _isbalanced } = pdSize(pd_smpl);

    The above code will return:

::

    ============================================================
    Group ID:              id          Balanced:             Yes
    Valid cases:            8          Missings:               0
    N. Groups:              2          T. Average:         4.000
    ============================================================
    id                        T[i]     Start Date       End Date
    ------------------------------------------------------------

    1                            4     1977-01-01     1980-01-01 
    2                            4     1977-01-01     1980-01-01 
    ============================================================

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

See also:

.. seealso:: :func:`pdsummary`, :func:`pdTimeSpans`
