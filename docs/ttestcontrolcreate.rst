

ttestControlCreate
==============================================

Purpose
----------------

Creates a :class:`ttestControl` structure with default values for use with :func:`ttest`.

Format
----------------
.. function:: ctl = ttestControlCreate()

    :return ctl: instance of :class:`ttestControl` structure with default values:

        .. csv-table::
            :widths: auto

            "ctl.output", "1, print results."
            "ctl.paired", "0, independent samples."
            "ctl.alternative", "0, two-sided test."
            "ctl.mu", "0, null hypothesis difference."
            "ctl.varEqual", "0, Welch t-test (unequal variances)."
            "ctl.confLevel", "0.95, 95% confidence interval."
            "ctl.miss", "0, error if missing values present."

    :rtype ctl: struct

Examples
----------------

::

    // Create control structure with defaults
    struct ttestControl ctl;
    ctl = ttestControlCreate();

    // Modify for paired test
    ctl.paired = 1;

    // Use with ttest
    out = ttest(before, after, ctl);

.. seealso:: Functions :func:`ttest`

