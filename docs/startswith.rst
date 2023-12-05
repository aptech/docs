
startsWith
==============================================

Purpose
----------------

Returns a 1 if a string starts with a specified pattern.

Format
----------------
.. function:: mask = startsWith(str, pat)

    :param str: The data to be searched.
    :type str: Nx1 string array or dataframe of type category or string

    :param pat: The pattern to search for in the beginning of *str*.
    :type pat: String or dataframe of type category or string

    :return mask: A matrix of the same size as *str* with a 1 in any element that starts with the value of *pat*, otherwise 0.
    :rtype mask: Nx1 vector

Examples
----------------

Example 1
+++++++++++

The following example searches for all observations of the variable *make* in the ``auto2.dta`` dataset that starts with ``"Buick"`` .

::
 
     // Load 3 variables from the dataset
     fname = getGAUSSHome("examples/auto2.dta");
     auto = loadd(fname, "make + price + mpg");
    
     // Specify pattern to search for
     pat = "Buick";
     
     // Find all makes that include 'Buick'
     mask = startsWith(auto[., "make"], pat);
    
     // Select observations if the corresponding
     // row of mask equals 1. 
     auto_buicks = selif(auto, mask);
  
     print auto_buicks;

This prints the following:

::
   
              make            price              mpg
     Buick Century        4816.0000        20.000000
     Buick Electra        7827.0000        15.000000
     Buick LeSabre        5788.0000        18.000000
        Buick Opel        4453.0000        26.000000
       Buick Regal        5189.0000        20.000000
     Buick Riviera        10372.000        16.000000
     Buick Skylark        4082.0000        19.000000
    

Example 2: Select rows based on the starting text from 2 columns 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example, we will select all rows where the first columns starts with *Buick* and the second column starts with *Ave*.

::

    // Load 2 variables from the dataset
    fname = getGAUSSHome("examples/auto2.dta");
    auto = loadd(fname, "make + rep78");
    
    // Select the first 7 observations
    auto = auto[1:7,.]; 
    
    print auto;

::

              make            rep78 
       AMC Concord          Average 
         AMC Pacer          Average 
        AMC Spirit                . 
     Buick Century          Average 
     Buick Electra             Good 
     Buick LeSabre          Average 
        Buick Opel                .

This time our pattern input needs to be a  1x2 string array with one search pattern for each column.

::
    
    // Specify one string to search
    // for in each column
    pat = "Buick" $~ "Ave";
    
    // Find all makes that include 'Buick'
    // and all rep78's that include 'Ave'.
    mask = startsWith(auto, pat);
    
    print mask;

::

       0.0000000        1.0000000 
       0.0000000        1.0000000 
       0.0000000        0.0000000 
       1.0000000        1.0000000 
       1.0000000        0.0000000 
       1.0000000        1.0000000 
       1.0000000        0.0000000
    
As we can see above, our *mask* contains two columns that tell us which observations matched our search. Before we can use :func:`selif` to select the 
matching rows, we need to convert *mask* to a column vector with a 1 in the case where both columns matched. We will do that by summing across the rows and then using the dot equality operator to see which rows were summed to equal two.
    
::

    mask2 = sumr(mask) .== 2;
    
    // Seliect 'Buick' observations
    // that are in average condition
    avg_buicks = selif(auto, mask2);

    print avg_buicks;

::

            make            rep78 
   Buick Century          Average 
   Buick LeSabre          Average


.. seealso:: Functions :func:`strindx`
