pdSize
==============================================

Purpose
----------------
Provides size description of a panel dataset including the number of groups, number of time observations for each group.

Format
----------------
.. function:: { num_grps, T, balanced } = pdSize(df, groupvar)

    :param df: Dataframe containing panel data with (N_i * T_i) rows (observations) and K columns (variables).
    :type df: (N_i*T_i)xK dataframe

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

::

    /*
    ** Example for summarizing panel data
    */
    cls;

    // Import data
    fname = getGAUSSHome("examples/nlswork.dta");
    nlswork = loadd(fname);

    // Check size of panel 
    { num_grps, T, _isbalanced } = pdSize(nlswork, "idcode");


The code above prints the following to screen:

::

    ==========================================================================================
    Group ID:               idcode                                    Balanced:             No
    Valid cases:             13452                                    Missings:          15082
    N. Groups:                4711                                  T. Average:          6.057
    ==========================================================================================

See also:

.. seealso:: :func:`pdSummary`
