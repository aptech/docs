
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
  fname = __FILE_DIR $+ "tips2.csv";

  // Load the dataframe
  tips2 = loadd(fname, "id + total_bill + tip + cat(day) + cat(time)");

  // Locate duplicate observations
  getduplicates(tips2);

After the above code the printed output is

::

   Row Num               id       total_bill              tip              day             time
 20.000000        20.000000        20.650000        3.3500000              Sat           Dinner
 21.000000        20.000000        20.650000        3.3500000              Sat           Dinner
 246.00000        245.00000        18.780000        3.0000000             Thur           Dinner
 247.00000        245.00000        18.780000        3.0000000             Thur           Dinner

.. seealso:: Functions :func:`dropduplicates`, :func:`isunique`
