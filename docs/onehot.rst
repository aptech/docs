oneHot
=========

Purpose
--------------------
Returns a matrix of one-hot (indicator) variables from a vector or dataframe column.

Format
--------------------
.. function::  X_oh = oneHot(X)

    :param X: The independent variable(s).
    :type X:  Nx1 vector, or dataframe

    :return X_oh: An ``nobs x nclasses`` dataframe with indicator variables for each class in ``X``.

Examples
------------

::

    // Create a categorical dataframe column
    s = "good" $| "fair" $| "poor" $| "fair";
    X = asdf(s, "rating");
    
    print X;

::

          rating 
            good 
            fair 
            poor 
            fair 

::

    // Create one-hot matrix
    X_oh = oneHot(X);
    print X_oh;

::

     rating_fair      rating_good      rating_poor 
           0.000            1.000           0.000 
           1.000            0.000           0.000 
           0.000            0.000           1.000 
           1.000            0.000           0.000 

::

    y = { 2, 2, 1, 3, 3 };
    
    y_oh = oneHot(y);

After the above code:

::

       X_1      X_2      X_3
    0.0000   1.0000   0.0000
    0.0000   1.0000   0.0000
    1.0000   0.0000   0.0000
    0.0000   0.0000   1.0000
    0.0000   0.0000   1.0000


Remarks
--------------------

#. Each column will be asigned a variable name that is the original variable name (or ``X`` if the variable passed in is not a dataframe) plus an underscore and the category. Examples are shown above.

.. seealso:: Functions  :func:`design`, :func:`getcollabels`, :func:`recodecatlabels`

