pdSummary
==============================================

Purpose
----------------
Generates summary statistics for panel data, including overall, between-group, and within-group statistics.

Format
----------------
.. function:: pdOut = pdSummary(df [, varlist, missings, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i x T_i` rows and K columns.
    :type df: Dataframe

    :param varlist: Optional, A list of variables to include in the summary. Default is all variables.
    :type varlist: 1xP string array

    :param missings: Optional, scalar, indicator that missings are present in data. Missing values must be removed for procedure. Setting to 0 will speed up procedure but should be used only if certain that no missings are present. Default = 1. 
    :type missings: Scalar

    :param groupvar: Optional, specifies the name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, specifies the name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return pdOut: A dataframe containing summary statistics:
        
        - Overall statistics: mean, standard deviation, minimum, and maximum for each variable.
        - Between-group statistics: mean, standard deviation, minimum, and maximum.
        - Within-group statistics: mean, standard deviation, minimum, and maximum.
  
    :rtype pdOut: Dataframe

Examples
----------------

::

    // Import data
    fname = getGAUSSHome("examples/pd_ab.gdat");
    pd_ab = loadd(fname);

    // Get summary statistics
    pd_summary = pdSummary(pd_ab);

::


    ==========================================================================================
    Group ID:                             id          Balanced:                             No
    Valid cases:                        1031          Missings:                              0
    N. Groups:                           140          T. Average:                        7.364
    ==========================================================================================
    Variable               Measure           Mean      Std. Dev.        Minimum        Maximum
    ------------------------------------------------------------------------------------------
    emp                    Overall          7.892         15.935          0.104        108.562 
                           Between              .         16.169          0.130        102.190 
                            Within              .          2.210        -14.812         34.763 
    wage                   Overall         23.919          5.648          8.017         45.232 
                           Between              .          5.184          8.713         36.060 
                            Within              .          2.068         11.722         40.935 
    ==========================================================================================

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

A strongly balanced panel dataset contains the same time points for each group. :func:`pdAllBalanced` examines the provided dataset to determine if it meets this condition.

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

See also:

.. seealso:: :func:`pdsize`, :func:`pdTimeSpans`
