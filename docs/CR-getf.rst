
getf
==============================================

Purpose
----------------

Loads an ASCII or binary file into a string.

Format
----------------
.. function:: getf(filename, mode)

    :param filename: any valid file name.
    :type filename: string

    :param mode: 
    :type mode: scalar 1 or 0 which determines if the file is to be loaded in ASCII mode (0) or binary mode (1)

    :returns: y (string), containing the file.

Examples
----------------
Suppose you have a file which writes the results of its calculations to a file in a report format. For this example, we will use the code snippet below:

::

    x1 = rndn(100,5);
    y1 = rndu(100,1);
    
    output file = regression_results.txt reset;
    call ols("", y1, x1);
    output off;
    
    x2 = rndn(100,5);
    y2 = rndu(100,1);
    
    output file = ols_results.txt reset;
    call ols("", y2, x2);
    output off;

Running the code above will create a file named "regression_results.txt" and a file named "ols_results.txt" in your current working directory. You can retrieve the output from either of these files with the 
getf command.

::

    str = getf("regression_results.txt",1);
    print str;

You can take this further and create a procedure that will load a list of output files for you. It can then print the output from each file as you are ready to read it.

::

    declare string array fileList = { "regression_results.txt", "ols_results.txt" };
    showOutput(fileList);
    
    proc (0) = showOutput(fileList);
       local k;
       for i(1, rows(fileList), 1);
          print "Press any key to view the next file:";
          //wait for user input and assign the first key stroke
          //to 'k'
          k = keyw;
          print getf(fileList[i],1);
       endfor;
    endp;

.. seealso:: Functions :func:`load`, :func:`save`, :func:`let`, :func:`con`
