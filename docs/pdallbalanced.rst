pdAllBalanced
==============================================

Purpose
----------------
Checks if a panel dataset is strongly balanced and returns 1 if balanced, 0 otherwise.

Format
----------------
.. function:: isBalanced = pdAllBalanced(df [, groupvar, datevar])

    :param df: Contains long-form panel data with :math:`N_i \times T_i` rows and K columns.
    :type df: Dataframe

    :param groupvar: Optional, specifies the name of the variable used to identify group membership for panel observations. Defaults to the first categorical or string variable in the dataframe.
    :type groupvar: String

    :param datevar: Optional, specifies the name of the variable used to identify dates for panel observations. Defaults to the first date variable in the dataframe.
    :type datevar: String

    :return isBalanced: Indicates if the panel dataset is balanced. Returns 1 if balanced, 0 otherwise.
    :rtype isBalanced: Scalar

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

    // Check to see if the panel is balanced
    is_balanced = pdallbalanced(pd_smpl);

    print is_balanced;


The above code will return:

::

     1.000

Remarks
-------

This function takes long-form panel data. To transform wide data to long-form data see :func:`dfLonger`.

This function assumes panel is sorted by group and date. Note that panel data can be sorted using :func:`pdSort`.

A strongly balanced panel dataset contains the same time points for each group. :func:`pdAllBalanced` examines the provided dataset to determine if it meets this condition.

- If *groupvar* is not provided, the function defaults to the first categorical or string variable in the dataframe.
- If *datevar* is not provided, the function defaults to the first date variable in the dataframe.

For datasets that are not strongly balanced, :func:`pdAllBalanced` returns 0.

See also:

.. seealso:: :func:`pdbalance`, :func:`pdSummary`, :func:`pdSize`
