
indicesfn
==============================================

Purpose
----------------

Processes a set of variable names or indices and
returns a vector of variable names and a vector of
indices.

Format
----------------
.. function:: { name, indx } = indicesfn(dataset, namein, indxin)

    :param dataset: name of the dataset.
    :type dataset: string

    :param namein: names
        of selected columns in the dataset. If set to a null string, columns are selected using *indxin*
    :type namein: Nx1 string array

    :param indxin: indices of selected columns in the dataset. If set to 0, columns are selected using
        *namein*.
    :type indxin: Nx1 vector

    :return name: the names of the selected columns.

    :rtype name: Nx1 string array

    :return indx: the indices of the selected columns.

    :rtype indx: Nx1 vector

Examples
----------------

Find indices using variable names
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

        // Create filename
        fname = getGAUSSHome $+ "examples/auto.dat";

        // Get variable names
        namein = "mpg" $| "weight";

        /*
        ** If namein is not equal to zero
        ** indxin must be equal to zero
        */
        indxin = 0;

        // Get indices and names of variables
        { varnames, indxs } = indicesfn(fname, namein, indxin);

        // Print variable one name
        print "Variable names:" $varnames;

        // Print index for variable one
        print "Variable indices:" indxs;

This produces the following output:

::

      Variable names:
                 mpg
              weight
      Variable indices:
           3.0000000
           7.0000000

Find variable names using index numbers
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

        // Create filename
        fname = getGAUSSHome $+ "examples/auto.dat";

        /*
        ** If indxin is not equal to zero
        ** namein must be equal to zero
        */
        namein = 0;

        /*
        ** If namein is not equal to zero
        ** indxin must be equal to zero
        */
        indxin = { 3, 7 };

        // Get indices and names of variables
        { varnames, indxs } = indicesfn(fname, namein, indxin);

        // Print variable one name
        print "Variable indices:" indxs;

        // Print index for variable one
        print "Variable names:" $varnames;

This produces the following output:

::

        Variable indices:
           3.0000000
           7.0000000
        Variable names:
                 mpg
              weight

Find all variable names and indices
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

      // Create filename
      fname = getGAUSSHome $+ "examples/auto.dat";

      /*
      ** namein should be
      ** null string for getting all variables
      */
      namein = "";

      /*
      ** Indxin should be zero
      ** for getting all variables
      */
      indxin = 0;

      // Get indices and names of variables
      { varnames, indxs } = indicesfn(fname, namein, indxin);

      // Print variable one name
      print "Variable names:" $varnames;

      // Print index for variable one
      print "Variable indices:" indxs;

This produces the following output :

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
        displacement
          gear_ratio
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

If *namein* is a null string and *indxin* is 0, all columns of the dataset
will be selected.

If an error occurs, *indx* will be set to a scalar error code. The
following error codes are possible:

+---+-----------------------------------------------------+
| 1 | Can't open data file                                |
+---+-----------------------------------------------------+
| 2 | Variable not found                                  |
+---+-----------------------------------------------------+
| 3 | Indices outside of range of columns                 |
+---+-----------------------------------------------------+


Source
------

indices.src

.. seealso:: Functions :func:`indicesf`, :func:`indices`
