

mvnTestControlCreate
==============================================

Purpose
----------------

Creates an :class:`mvnTestControl` structure with default values for use with :func:`mvnTest`.

Format
----------------
.. function:: ctl = mvnTestControlCreate()

    :return ctl: instance of :class:`mvnTestControl` structure with default values:

        .. csv-table::
            :widths: auto

            "ctl.output", "1, print results."
            "ctl.miss", "0, error if missing values present."
            "ctl.method", "``""hz""``, use Henze-Zirkler test."

    :rtype ctl: struct

Examples
----------------

::

    // Create control structure with defaults
    struct mvnTestControl ctl;
    ctl = mvnTestControlCreate();

    // Modify as needed
    ctl.method = "all";
    ctl.miss = 1;  // enable listwise deletion

    // Use with mvnTest
    out = mvnTest(X, ctl);

.. seealso:: Functions :func:`mvnTest`

