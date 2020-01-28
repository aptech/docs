
indices
==============================================

Purpose
----------------

Processes a set of variable names or indices and returns a vector of variable names and a vector of indices.

Format
----------------
.. function:: { name, indx } = indices(dataset, vars)

    :param dataset: the name of the dataset.
    :type dataset: string

    :param vars: a character vector of names or a numeric vector of column indices.
        If scalar 0, all variables in the dataset will be selected.
    :type vars: Nx1 vector

    :return varnames: the names associated with *vars*.

    :rtype varnames: Nx1 character vector

    :return indx: the column indices associated with *vars*.

    :rtype indx: Nx1 numeric vector

Examples
----------------

Find indices for selection of variables
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create character vector of variable names
  vars = { mpg, weight };

  // Create filename
  filename = getGAUSSHome $+ "examples//auto.dat";

  // Get indices and names of variables
  {varnames, ind } = indices(filename, vars);

  // Print variables names
  print "Variable names:" $varnames;

  // Print variable indices
  print "Variable indices:" ind;

This produces the following output:

::

    Variable names:
             mpg
          weight
    Variable indices:
       3.0000000
       7.0000000

Find indices for all variables
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    /*
    ** Set vars equal to zero to get
    ** indices for all variables
    */
    vars =0;

    // Create filename
    filename = getGAUSSHome $+ "examples//auto.dat";

    // Get indices and names of variables
    {varnames, ind } = indices(filename, vars);

    // Print variables names
    print "Variable names:" $varnames;

    // Print variables indices
    print "Variable indices:" ind;

This produces the following output

::

  Variable names:
            make
           price
             mpg
           rep78
        headroom
           trunk
          weight
          length
            turn
        displace
        gear_rat
         foreign
  Variable indices:
       1.0000000
       2.0000000
       3.0000000
       4.0000000
       5.0000000
       6.0000000
       7.0000000
       8.0000000
       9.0000000
       10.000000
       11.000000
       12.000000

Remarks
-------

If an error occurs, :func:`indices` will either return a scalar error code or
terminate the program with an error message, depending on the `trap`
state. If the low order bit of the `trap` flag is 0, :func:`indices` will
terminate with an error message. If the low order bit of the `trap` flag
is 1, :func:`indices` will return an error code. The value of the `trap` flag can
be tested with `trapchk`; the return from :func:`indices` can be tested with
:func:`scalerr`. You only need to check one argument; they will both be the
same. The following error codes are possible:

+---+-----------------------------------------------------+
| 1 | Can't open dataset.                                 |
+---+-----------------------------------------------------+
| 2 | Index of variable out of range, or undefined data   |
|   | set variables.                                      |
+---+-----------------------------------------------------+


Source
------

indices.src
