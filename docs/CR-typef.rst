
typef
==============================================

Purpose
----------------

Returns the type of data (the number of bytes
per element) in a GAUSS data set.

Format
----------------
.. function:: typef(fp)

    :param fp: file handle of an open file.
    :type fp: scalar

    :returns: y (*scalar*), type of data in GAUSS data set.

Examples
----------------

::

    //Assign a variable to represent each of our file names
    infile = "dat1";
    outfile = "dat2";
    
    //Open the file "dat1" for reading.
    //Note: The ^ before 'infile' tells GAUSS to use the value
    //of the string variable 'infile' (which is 'dat1' in this 
    //case) rather than name of the variable.
    open fin = ^infile;
    
    //Get the names of the variables that are saved in the
    //dataset
    names = getname(infile);
    
    //Create a new data set file using the same variable names
    //as 'dat1', with 1 column per data element and using the 
    //same size data, i.e. the number of bytes per element, as 
    //the data in 'dat1'
    create fout = ^outfile with ^names, 0, typef(fin);

In this example, a file dat2.dat is created which has
the same variables and variable type as the input
file, dat1.dat.  typef is used to return the type of
the input file data for the create statement.

.. seealso:: Functions :func:`colsf`, :func:`rowsf`
