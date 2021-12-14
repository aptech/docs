
dropduplicates
==============================================

Purpose
----------------

Drops duplicate observations from data.

Format
----------------
.. function:: x_new = dropduplicates(x [, varlist])

    :param x: data
    :type x: matrix or dataframe

    :param varlist: Optional, list of variables to include in the check for duplicates. Default is across all variables.
    :type varlist: string array

    :return dup_report: Returns a dataframe with duplicate observations from ``x`` removed.
    :rtype dup_report: dataframe

Examples
----------------

::

  new;

  // Create file name with full path
  fname = getGAUSSHome() $+ "examples/tips2.dta";

  // Load the dataframe
  tips2 = loadd(fname);

  // Locate and remove the duplicate observations
  tips_no_dups = dropduplicates(tips2);

.. seealso:: Functions :func:`getduplicates`, :func:`isunique`
