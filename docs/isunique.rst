
isunique
==============================================

Purpose
----------------

Returns a 1 if the data contains all unique observations, otherwise returns a 0.

Format
----------------
.. function:: ret = isunique(x [, varlist])

    :param x: data
    :type x: matrix or dataframe

    :param varlist: Optional, list of variables to include in the check. Default is across all variables.
    :type varlist: string array

    :return ret: 1 if ``x`` contains unique observations across the specific ``varlist``, otherwise 0.
    :rtype ret: scalar

Examples
----------------

Example 1
+++++++++++++

::

  new;

  // Create file name with full path
  fname = getGAUSSHome() $+ "examples/tips2.dta";

  // Load the dataframe
  tips2 = loadd(fname, "id + total_bill + tip + cat(sex) + cat(smoker) + cat(day) + cat(time) + size");

  // Check if all observations of the id variable are unique
  if isunique(tips2, "id");
    print "ID variable is unique.";
  else;
    print "ID variable contains duplicates.";
  endif;

After the above code the printed output is

::

  ID variable contains duplicates.


Example 2
+++++++++++++
Now we will check to see if just the ``id`` is duplicated or if all variables are duplicated.

::


  // Check if dataframe has duplicates observations
  // across all variables
  if isunique(tips2);
    print "Dataframe is unique.";
  else;
    print "Dataframe contains duplicates.";
  endif;

After the above code the printed output is

::

  Dataframe contains duplicates.

.. seealso:: Functions :func:`dropduplicates`, :func:`getduplicates`
