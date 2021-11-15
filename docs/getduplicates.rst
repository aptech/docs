
getduplicates
==============================================

Purpose
----------------

Identifies duplicate observations and prints report.

Format
----------------
.. function:: dup_report = getduplicates(x [, varlist])

    :param x: data
    :type x: matrix or dataframe

    :param varlist: Optional, list of variables to include in the check. Default is across all variables.
    :type varlist: string array

    :return dup_report: Returns a dataframe containing duplicate observations from ``x`` with the row of the observed duplicates in the first column.
    :rtype dup_report: dataframe

Examples
----------------

::

  new;

  // Create file name with full path
  fname = getGAUSSHome() $+ "examples/tips2.csv";

  // Load the dataframe
  tips2 = loadd(fname, "id + total_bill + tip + cat(day) + cat(time)");

  // Locate and print duplicate observations
  print getduplicates(tips2);

After the above code the printed output is

::

    Row Num         id   total_bill       tip       day        time
     20.000      20.00        20.65      3.35       Sat      Dinner
     21.000      20.00        20.65      3.35       Sat      Dinner
     246.00      245.0        18.78      3.00      Thur      Dinner
     247.00      245.0        18.78      3.00      Thur      Dinner

.. seealso:: Functions :func:`dropduplicates`, :func:`isunique`
