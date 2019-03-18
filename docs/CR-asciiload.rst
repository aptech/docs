
asciiload
==============================================

Purpose
----------------
Loads data from a delimited ASCII text file into an Nx1 vector. NOTE: This function is deprecated. Use csvReadM instead.

Format
----------------
.. function:: asciiload(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: y (*TODO*), Nx1 vector.

Examples
----------------
To load the file myfile.asc, containing the following data:

::

    2.805  16.568
     -4.871   3.399
     17.361 -12.725

you may use any of the following commands:

::

    /*
    ** This statement assumes 'myfile.asc' is in the current
    ** working directory
    */
    y = asciiload("myfile.asc");

::

    /*
    ** This code assumes that 'myfile.asc' is
    ** located in the C:\gauss17 directory
    ** Note the double backslashes for path separators
    */
    fpath = "C:/gauss17/myfile.asc";
    y = asciiload(fpath);

::

    path = "C:/gauss/";
    fname = "myfile.asc";
    
    /*
    ** The '$+' operator adds two strings together into one
    ** string
    */
    y = asciiload(path $+ fname);

All of the above commands will set y to be equal to:

::

    2.805
     16.568
     -4.871
      3.399
     17.361
    -12.725

.. seealso:: Functions :func:`csvReadM`, :func:`load`, :func:`dataload`
