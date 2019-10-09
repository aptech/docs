
modec
==============================================

Purpose
----------------

Computes the mode of every column of a matrix.

Format
----------------
.. function:: m = modec(x)

    :param x: data
    :type x: NxK matrix

    :return m: contains the mode of every column of *x*.

    :rtype m: Kx1 matrix

Examples
----------------

Basic example
+++++++++++++++

::

    // Create a 5x1 column vector
    x = { 3,
          4,
          4,
          3,
          3 };

    // Compute the mode of this column
    m = modec(x);

After the code above, *m* is equal to:

::

    3

Multi-column mode from credit dataset
+++++++++++++++++++++++++++++++++++++++

This example will load the variables, *Cards*, *Age* and *Education* from the dataset :file:`credit.dat` and find the mode of each variable.

::

    // Create the file name with full path 
    fname = getGAUSSHome() $+ "examples/credit.dat";
    
    // Load three variables by name 
    X = loadd(fname, "Cards + Age + Education");
    
    // Compute the mode of each of the
    // three columns in 'X'
    m = modec(X);

After the code above, *m* will equal:

::

    2
   44
   16

Which tells us that for our sample, the most common: 

* number of credit cards owned is 2.
* age is 44 years old.
* number of years of education is 16.

Remarks
------------

* If two more more numbers are tied for the most appearances, then :func:`modec` will select the smallest of them. 
* To find the mode of the entire matrix, use the :func:`vecr` command to turn the function into a column vector before calling `modec`.

    ::

        m = modec(vecr(x));

* To find out how many times each value is present, use :func:`counts`.
* To compute the mode for subgroups of a variable, use :func:`aggregate`.

  


.. seealso:: Functions :func:`meanc`, :func:`stdc`
