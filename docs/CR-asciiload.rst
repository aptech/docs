
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

    :returns: y (Nx1 vector)

Remarks
-------

.. NOTE:: This function is deprecated. Use :func:`csvReadM` instead.

The file extension must be included in the file name.

Numbers in ASCII files must be delimited with spaces, commas, tabs, or
newlines.

This command loads as many elements as possible from the file into an
Nx1 vector. This allows you to verify if the load was successful by
calling :code:`rows(y)` after :func:`asciiload` to see how many elements were actually
loaded. You may then reshape the Nx1 vector to the desired form. You
could, for instance, put the number of rows and columns of the matrix
right in the file as the first and second elements and reshape the
remainder of the vector to the desired form using those values.

Examples
----------------

To load the file `myfile.asc`, containing the following data:

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

All of the above commands will set *y* to be equal to:

::

    2.805
     16.568
     -4.871
      3.399
     17.361
    -12.725

.. seealso:: Functions :func:`csvReadM`, `load`, :func:`dataload`

