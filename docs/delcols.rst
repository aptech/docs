
delcols
==============================================

Purpose
----------------

Returns a matrix with specified columns removed.

Format
----------------
.. function:: x_trim = delcols(x, c_idx)

    :param x:
    :type x: Matrix or dataframe

    :param c_idx: index of columns to remove from *x*. These may be integers or variable names of a dataframe.
        Negative integers will start from the back. For example,
        -1 will indicate to remove the final column of *x*.
    :type c_idx: Scalar, string or vector

    :return x_trim: equal to input *x* without columns specified by
        input *c_idx*. If no columns remain, *x_trim* will be
        an empty matrix.

    :rtype x_trim: matrix

Examples
----------------

Example 1: Basic matrix usage
++++++++++++++++++++++++++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the second column of 'x'
    x_trim = delcols(x, 2);

After the above code:

::

              1  3  4
    x_trim =  5  7  8
              9 11 12

Example 2: Remove two columns from a matrix
+++++++++++++++++++++++++++++++++++++++++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the second and fourth columns of 'x'
    c_idx = { 2, 4 };

    x_trim = delcols(x, c_idx);

After the above code:

::

              1  3
    x_trim =  5  7
              9 11


Example 3: Negative index example
+++++++++++++++++++++++++++++++++++

::

    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Remove the final column of 'x'
    x_trim = delcols(x, -1);

After the above code:

::

              1  2  3
    x_trim =  5  6  7
              9 10 11


Example 4: Dataframe
+++++++++++++++++++++++++++++++++++

::

    // Load three variables into a dataframe
    fname = getGAUSSHome() $+ "examples/detroit.sas7bdat";
    detroit = loadd(fname, "ft_police + unemployment + hourly_earn");

    // Print the first three observations
    print detroit[1:3,.];

will return the following output:

::

       ft_police     unemployment      hourly_earn 
       260.35000        11.000000        2.9800000 
       269.80000        7.0000000        3.0900000 
       272.04000        5.2000000        3.2300000

::

    // Remove the variable 'ft_police'
    detroit = delcols(detroit, "ft_police");

    // Print the first three observations
    // after removing the variable
    print detroit[1:3,.];

::

    unemployment      hourly_earn 
       11.000000        2.9800000 
       7.0000000        3.0900000 
       5.2000000        3.2300000


.. seealso:: Functions :func:`delif`, :func:`delrows`, :func:`selif`
