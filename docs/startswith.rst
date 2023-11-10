
startsWith
==============================================

Purpose
----------------

Returns a 1 if a string starts with a specified pattern.

Format
----------------
.. function:: mask = startsWith(str, pat)

    :param str: the data to be searched. 
    :type str: Nx1 string array or dataframe of type category or string

    :param pat: the pattern to search for in the beginning of *str*.
    :type pat: String or dataframe of type category or string

    :return mask: A matrix of the same size as *str* with a 1 in any element that starts with the value of *pat*, otherwise 0.
    :rtype mask: Nx1 vector

Examples
----------------
The following example searches for all observations of the variable *make* in the ``auto2.dta`` dataset that starts with either ``"Buick"`` or ``"MFC"``.

::
  
   // Load data
   data = loadd(getGAUSSHome("examples/auto2.dta"));
   
   // Specify pattern to search for
   pat = "Buick";
    
   // Find all makes that include `Buick`
   mask = startsWith(data[., "make"], pat);
   
   // Print *make*, *price*, and *mpg*
   // for `Buicks` observations
   head(selif(data[., "make" "price" "mpg"], mask));

This prints the following:

::
    
            make            price              mpg 
   Buick Century        4816.0000        20.000000 
   Buick Electra        7827.0000        15.000000 
   Buick LeSabre        5788.0000        18.000000 
      Buick Opel        4453.0000        26.000000 
     Buick Regal        5189.0000        20.000000 
     
.. seealso:: Functions :func:`strindx`
