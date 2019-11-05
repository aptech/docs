
type
==============================================

Purpose
----------------
 Returns the symbol table type (matrix, string, etc) of its input argument.

Format
----------------
.. function:: t = type(x)

    :param x: local or global symbol, can be an expression.
    :type x: any

    :return t: argument type.

        .. csv-table::
            :widths: auto

            "6", "matrix"
            "13", "string"
            "15", "string array"
            "17", "structure"
            "21", "array"
            "23", "structure pointer"
            "38", "sparse matrix"

    :rtype t: scalar

Examples
----------------

Example 1
+++++++++

::

    // Create a matrix
    x = { 1 2,
          3 4 };

    // Find type of 'x'
    x_type = type(x);

After the above code, ``x_type`` will equal: 6, indicating that ``x`` is a matrix.

Example 2
+++++++++

::

    // Create a string
    x = "myfile.dat";

    // Find type of 'x'
    x_type = type(x);

After the above code, ``x_type`` will equal: 13, indicating that ``x`` is a string.

Remarks
-------

:func:`type` is often used to verify that inputs to a user defined procedure are
valued. For example, if an input is a file name, then it must be a string:

::

   proc (1) = myProc(fname);
       if type(fname) != 13;
           errorlog "Input 'fname' must be a string";
           end;
       endif;
   endp;

:func:`type` returns the type of a single symbol. The related function :func:`typecv`
will take a character vector of symbol names and return a vector of
either their types or the missing value code for any that are undefined.
:func:`type` works for the symbol types listed above; :func:`typecv` works for
user-defined procedures, keywords and functions as well. :func:`type` works for
global or local symbols; :func:`typecv` works only for global symbols.

.. seealso:: Functions :func:`typecv`, :func:`typef`
