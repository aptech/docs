
getf
==============================================

Purpose
----------------

Loads an ASCII or binary file into a string.

Format
----------------
.. function:: str_contents = getf(filename, mode)

    :param filename: any valid file name.
    :type filename: string

    :param mode: 1 or 0 which determines if the file is to be loaded in ASCII mode (0) or binary mode (1)
    :type mode: scalar

    :return str_contents: contains the file contents.

    :rtype str_contents: string

Remarks
-------

If the file is loaded in ASCII mode, it will be tested to see if it
contains any end of file characters. These are ``^Z`` (ASCII 26). The file
will be truncated before the first ``^Z``, and there will be no ``^Z``'s in the
string. This is the correct way to load most text files because the ``^Z``'s
can cause problems when trying to print the string to a printer.

If the file is loaded in binary mode, it will be loaded just like it is
with no changes.


Examples
----------------

Suppose you have a file which writes the results of its calculations to a file in a report format. For this example, we will use the code snippet below:

::

    // Generate random x1 and y1
    x1 = rndn(100, 5);
    y1 = rndu(100, 1);

    /*
    ** Set output file on and set
    ** name to `regression_results`
    */
    output file = regression_results.txt reset;

    // Run OLS
    call ols("", y1, x1);

    // Turn output off
    output off;

    // Generate random x2 and y2
    x2 = rndn(100, 5);
    y2 = rndu(100, 1);

    /*
    ** Set output file on and set
    ** name to `ols_results`
    */
    output file = ols_results.txt reset;

    // Run OLS
    call ols("", y2, x2);

    // Turn output off
    output off;

Running the code above will create a file named :file:`regression_results.txt` and a file named :file:`ols_results.txt` in your current working directory. You can retrieve the output from either of these files with the :func:`getf` command.

::

    str_contents = getf("regression_results.txt", 1);
    print str_contents;

You can take this further and create a procedure that will load a list of output files for you. It can then print the output from each file as you are ready to read it.

::

    declare string array fileList = { "regression_results.txt", "ols_results.txt" };
    showOutput(fileList);

    proc (0) = showOutput(fileList);
       local k;

       for i(1, rows(fileList), 1);

          print "Press any key to view the next file:";

          /*
          ** Wait for user input and assign the first key stroke
          ** to 'k'
          */
          k = keyw;
          print getf(fileList[i], 1);

       endfor;
    endp;

.. seealso:: Functions `load`, `save`, `let`, :func:`con`
