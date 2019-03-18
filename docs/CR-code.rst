
code
==============================================

Purpose
----------------

Allows a new variable to be created (coded) with different
values depending upon which one of a set of logical
expressions is true.

Format
----------------
.. function:: code(logical,  new_vals)

    :param logical: NxK matrix of 1's and 0's. Each column of this matrix
        is created by a logical expression using ''dot'' conditional and boolean operators. Each of these expressions should
        return a column vector result. The columns are horizontally concatenated to produce logical. If more than
        one of these vectors contains a 1 in any given row, the code function will terminate with an error message.
    :type logical: TODO

    :param new_vals: (K+1)x1 vector containing the values to be
        assigned to the new variable.
    :type new_vals: TODO

    :returns: y (*TODO*), Nx1 vector containing the new values.

Examples
----------------

Suppose we have a vector of blood pressure data that we want to separate into two classes. Class 1 will contain the observations with a blood pressure value below 120. The others will belong to class 2.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Blood pressure data
    x = { 91,
         121,
          99,
         135,
         110,
         155 };
    
    //Values for the classes
    new_val = { 1,
                2 };      
    
    //Create a vector containing a 1 for every element
    //which is less than 120, or a 0 otherwise
    logical = x .<  120;
    
    //Create a new vector which contains the class
    //assignment for each element in 'x'
    x_class = code(logical, new_val);

After the code above:

::

    x = 91   logical =  1   x_class = 1 
       121              0             2 
        99              1             1 
       135              0             2 
       110              1             1 
       155              0             2

Continuing with the blood pressure example from above, we will now create a new categorical variable with 3 levels. Level 1 will contain observations less than or equal to 100. Level 2 will contain observations greater than 100 and less than or equal to 120. Level 3 will contain observations greater than 120.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Blood pressure data
    x = { 91,
         121,
          99,
         135,
         110,
         155 };
    
    //Values for the classes
    new_val = { 1,
                2,
                3 };
    
    //Create a vector containing a 1 for every element
    //which is 100 or less, or a 0 otherwise
    logical_1 = x .<= 100;
    
    //Create a vector containing a 1 for every element
    //which is between 100 and 120, or a 0 otherwise
    logical_2 = x .> 100 .and x .<=  120;
    
    //Form a 2 column logical vector using
    //horizontal concatenation
    logical = logical_1 ~ logical_2;
    
    //Create a new vector which contains the class
    //assignment for each element in 'x'
    x_class = code(logical, new_val);

After the code above:

::

    x =  91    logical = 1 0     x_class = 1
        121              0 0               3
         99              1 0               1
        135              0 0               3
        110              0 1               2
        155              0 0               3

Remarks
+++++++

For every row in logical, if a 1 is in the first column, the first
element of new_vals is used. If a 1 is in the second column, the second
element of new_vals is used, and so on. If there are only zeros in the
row, the last element of new_vals is used. This is the default value.

If there is more than one 1 in any row of logical, the function will
terminate with an error message.

Source
++++++

datatran.src

.. seealso:: Functions :func:`recode`, :func:`reclassifyCuts`, :func:`reclassify`, :func:`substute`, :func:`rescale`, :func:`dummy`
