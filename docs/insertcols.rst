
insertcols
==============================================

Purpose
----------------

Inserts one or more new columns into a matrix or dataframe at a specified location.

Format
----------------
.. function:: X_expand = insertcols(X, idx, new_cols)

    :param X: Data.
    :type X: Matrix or dataframe

    :param idx: The index after which to insert the new columns. This may be an integer index or a string variable name.
    :type idx: Scalar, string or vector

    :param new_cols: The new columns to insert into *X*.
    :type new_cols: Scalar, string or vector

    :return X_expand: Equal to input *X* with the new columns added after the position indicated by  
        input *idx*.

    :rtype X_expand: Matrix or dataframe

Examples
----------------

Example 1: Basic matrix usage
++++++++++++++++++++++++++++++++

::

    X = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    new_cols = { 22 33,
                 44 55,
                 66 77 };

    // Insert 'new_cols' ater column 2
    X_expand = insertcols(X, 2, new_cols);

After the above code:

::

              1    2   22   33    3    4 
   X_expand = 5    6   44   55    7    8 
              9   10   66   77   11   12

Example 2: Add a constant term to a matrix
+++++++++++++++++++++++++++++++++++++++++++++++

::

    X = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    // Create vector for constant
    const = ones(rows(X), 1);

    // Insert after '0' column
    idx = 0;
    
    // Insert 'const' vector 
    X_expand = insertcols(X, idx, const);

After the above code:

::

              1    1    2    3    4 
   X_expand = 1    5    6    7    8 
              1    9   10   11   12

:func:`insertcols` will expand a scalar to fill the new column, so the code below will also add a column of ones to the front of a matrix.

::

    // Insert after '0' column
    idx = 0;
    
    // Specify scalar 1 to insert
    const = 1; 
    
    // Expands scalar 'const' 
    // to match size of X and insert at
    // beginning of matrix
    X_expand = insertcols(X, idx, const);


Example 3: Add an indicator variable to a dataframe
+++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example we will create an indicator variable to show whether the original data in one of our columns contained a missing value or not. Then we will impute this value and insert the new column using a variable name as the index.

::

    // Load 3 variables from the dataset
    auto = loadd(getGAUSSHome("examples/auto2.dta"), "make + mpg + rep78");
    
    print auto[1:7,.];

::

              make            mpg          rep78 
       AMC Concord             22        Average 
         AMC Pacer             17        Average 
        AMC Spirit             22              . 
     Buick Century             20        Average 
     Buick Electra             15           Good 
     Buick LeSabre             18        Average 
        Buick Opel             26              .

::
    
    // Create an indicator variable to show whether
    // 'rep78'  observations are missing
    rep78_miss = auto[.,"rep78"] .== miss();
    
    // Add a variable name to our indicator variable
    rep78_miss = asdf(rep78_miss, "rep78_miss");
    
    // Replace the missing values of 'rep78' with the mode
    auto[.,"rep78"] = impute(auto[.,"rep78"], "mode");
    
    // Add the indicator variable after 'mpg'
    auto = insertcols(auto, "mpg", rep78_miss);
    
    print auto[1:7,.];

::

              make            mpg     rep78_miss          rep78 
       AMC Concord             22              0        Average 
         AMC Pacer             17              0        Average 
        AMC Spirit             22              1        Average 
     Buick Century             20              0        Average 
     Buick Electra             15              0           Good 
     Buick LeSabre             18              0        Average 
        Buick Opel             26              1        Average

.. seealso:: Functions :func:`delif`, :func:`delrows`, :func:`selif`
