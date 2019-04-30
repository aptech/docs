
unique
==============================================

Purpose
----------------
Sorts and removes duplicate elements from a vector.

Format
----------------
.. function:: unique(x, flag)

    :param x: NxM character data, or NxM string array.
    :type x: NxM numeric matrix

    :param flag: scalar, 1 if numeric data, 0 if character data. Default is 1.
        String array does not need a flag.
    :type flag: Optional input

    :returns: y (*Mx1 vector*), sorted x with
        the duplicates removed.

Examples
----------------

Numeric
+++++++

::

    // Create a column vector with duplicate elements
    years = { 1632, 
              2012, 
              1709, 
              1812, 
              1709, 
              1989, 
              1830, 
              1875, 
              1912, 
              1912, 
              1924, 
              1960 };
    
    // Sort 'years' and remove any duplicate elements
    years_unique = unique(years);

After the code above, the variables years and years_unique are assigned as follows:

::

    1632
             2012                  1632
             1709                  1709
             1812                  1812
             1709                  1830
    years =  1989   years_unique = 1875
             1830                  1912
             1875                  1924
             1912                  1960
             1912                  1989
             1924                  2012
             1960

Numeric Matrix
++++++++++++++

::

    // Create a numeric matrix with duplicate elements
    years = { 1632          2012, 
              1709           1812, 
              1709           1989, 
              1830           1875, 
              1912           1912, 
              1924           1960 };
    
    // Sort 'years' and remove any duplicate elements
    years_unique = unique(years);
    print "years: " years;
    print;
    print "years_unique:" years_unique;

After the code above, the variables years and years_unique are assigned as follows:

::

    years: 
    1632.0000        2012.0000 
    1709.0000        1812.0000 
    1709.0000        1989.0000 
    1830.0000        1875.0000 
    1912.0000        1912.0000 
    1924.0000        1960.0000 
    				
    years_unique:
    1632.0000 
    1709.0000 
    1812.0000 
    1830.0000 
    1875.0000 
    1912.0000 
    1924.0000 
    1960.0000 
    1989.0000 
    2012.0000

Character data
++++++++++++++

::

    // Create column character vector, by using
    // numeric concatenation operator
    levels = "high" | "medium" | "medium" | "low" | 
             "high" | "medium" | "medium"; 
    
    // Set flag to indicate data is character data
    flag = 0;
    
    
    // Sort 'levels' alphabetically and
    // remove any duplicate elements
    levels_unique = unique(levels, flag);
    
    
    // Note the $ used before the variable which
    // tells GAUSS to print as characters
    print $levels_unique;

The code above will produce the following output:

::

    high
       low
    medium

You can reorder these levels with an indexing operation, for example:

::

    levels = levels_unique[2 3 1];
    print levels;

will produce the following output:

::

    low
    medium 
      high

: String array vector
+++++++++++++++++++++

::

    // Create column string array
    string levels = { "high",  "medium", "medium",  "low", 
             "high", "medium", "medium"}; 
    
    // Sort 'levels' alphabetically and
    // remove any duplicate elements
    levels_unique = unique(levels);
    
    print levels_unique;

The code above will produce the following output:

::

    high
       low
    medium

: String array matrix
+++++++++++++++++++++

::

    // Create 3x2 string array 
    
    string levels = { "apple"      "watermelon", 
                      "banana"     "banana", 
                      "watermelon" "apple" }; 
    
    // Sort 'levels' alphabetically and
    // remove any duplicate elements
    levels_unique = unique(levels);
    				
    print"levels: " levels;
    print;
    print"levels_unique:" levels_unique;

The code above will produce the following output:

::

    levels: 
    apple       		watermelon 
    banana           	banana 
    watermelon            	apple 
    
    levels_unique:
    apple 
    banana 
    watermelon

.. seealso:: Functions :func:`sortc`, :func:`uniquesa`, :func:`uniqindx`
