
mergevar
==============================================

Purpose
----------------

Accepts a list of names of global matrices, and concatenates the corresponding matrices horizontally to form a single matrix.

Format
----------------
.. function:: mergevar(vnames)

    :param vnames: 
    :type vnames: string or Kx1 column vector containing the names of K global matrices

    :returns: x (*NxM matrix that contains the concatenated matrices*), where M is the sum of the columns in
        the K matrices specified in  vnames.

Examples
----------------

::

    //Random integers between 1 and 72
    age = ceil(72 * rndu(100, 1));
    
    //Random normal numbers with a mean of 70 and a standard
    //deviation of 10
    income = 10 * rndn(100, 1) + 70;
    
    //Vertically concatenate the strings
    vnames = "age"$|"income";
    
    //Merge the variables into 1 matrix
    agInc = mergevar(vnames);

The column vectors age and income will be concatenated
horizontally to create agInc. The above call to mergevar
is equivalent to:

::

    //Combine the matrices using the horizontal concatenation
    //operator
    agInc = age~income;

Source
++++++

vars.src

.. seealso:: Functions :func:`makevars`
