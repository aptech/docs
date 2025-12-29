
endsWith
==============================================

Purpose
----------------

Returns a 1 if a string ends with a specified pattern.

Format
----------------
.. function:: mask = endsWith(str, pat)

    :param str: The data to be searched.
    :type str: Nx1 string array or dataframe of type category or string

    :param pat: The pattern to search for at the end of *str*.
    :type pat: String or dataframe of type category or string

    :return mask: A matrix of the same size as *str* with a 1 in any element that ends with the value of *pat*, otherwise 0.
    :rtype mask: Nx1 vector

Examples
----------------

Example 1
+++++++++++

The following example searches for all observations of the variable *make* in the ``auto2.dta`` dataset that end with ``"bird"`` .

::
 
     // Load 3 variables from the dataset
     fname = getGAUSSHome("examples/auto2.dta");
     auto = loadd(fname, "make + price + mpg");
    
     // Specify pattern to search for
     pat = "bird";
     
     // Find all makes that end with 'bird'
     mask = endsWith(auto[., "make"], pat);
    
     // Select observations if the corresponding
     // row of mask equals 1. 
     auto_birds = selif(auto, mask);
  
     print auto_birds;

This prints the following:

::
   
            make            price              mpg 
  Pont. Firebird        4934.0000        18.000000 
   Pont. Sunbird        4172.0000        24.000000 


Example 2: Select rows based on the ending text from 2 columns 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example, we will select all rows where the first column ends with *Apple* and the second column ends with *Cheese*.

::

    // Create 2, 4x1 string arrays
    fruit = "Red Apple" $| "Grapefruit" $| "Green Apple" $| "Green Apple";
    snack = "Cheddar Cheese" $| "Havarti Cheese" $| "Walnuts" $| "Swiss Cheese";
    
    // Combine the string arrays into a dataframe
    food = asdf(fruit $~ snack, "fruit", "snack");
    
    print food;
::

           fruit            snack 
       Red Apple   Cheddar Cheese 
      Grapefruit   Havarti Cheese 
     Green Apple          Walnuts 
     Green Apple     Swiss Cheese

This time our pattern input needs to be a  1x2 string array with one search pattern for each column.

::
    
    // Specify one string to search
    // for in each column
    pat = "Apple" $~ "Cheese";
    
    // Find all fruits that end with 'Apple'
    // and all snacks that end with 'Cheese'.
    mask = endsWith(food, pat);

    print mask;
::

       1.0000000        1.0000000 
       0.0000000        1.0000000 
       1.0000000        0.0000000 
       1.0000000        1.0000000

As we can see above, our *mask* contains two columns that tell us which observations matched our search. Before we can use :func:`selif` to select the 
matching rows, we need to convert *mask* to a column vector with a 1 in the case where both columns matched. We will do that by summing across the rows and then using the dot equality operator to see which rows were summed to equal two.
    
::

    mask2 = sumr(mask) .== 2;
    
    // Select observations where the fruit ends with 'Apple'
    // and the snack ends with 'Cheese'
    apple_cheese = selif(food, mask2);

    print apple_cheese;

::

           fruit            snack 
       Red Apple   Cheddar Cheese 
     Green Apple     Swiss Cheese

.. seealso:: Functions :func:`startsWith`, :func:`strindx`, :func:`strsect`, :func:`strtrim`
