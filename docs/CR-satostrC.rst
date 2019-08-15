
satostrC
==============================================

Purpose
----------------

Copies from one string array to another using a C language format specifier string for each element.

Format
----------------
.. function:: y = satostrC(sa, fmt)

    :param sa: data
    :type sa: NxM string array

    :param fmt: 1x1, 1xM, or Mx1 format specifier for each element copy.
    :type fmt: string or string array

    :return y: 

    :rtype y: NxM formatted string array

Examples
----------------

Basic example
+++++++++++++

::

    // Create a 3x1 column vector
    length = { 12, 25, 18 };
    
    // Convert numeric data to a string array
    length = ntos(length);
    
    // Add '(cm)' after each number
    fmt = "%s (cm)";
    
    length_fmt = satostrc(length, fmt);

After the code above, *length_fmt* will equal:

::

    "12 (cm)" 
    "25 (cm)" 
    "18 (cm)"

Different formats for each column
+++++++++++++++++++++++++++++++++

::

    // Create numeric matrices
    year = { 2012, 2013, 2014 };
    beef = { 187.9, 183.6, 224.1 };
    fish = { 4.8, 6.8, 6.6 };
    						
    // Create a 3x3 matrix using horiztonal concatenation
    commodity_prices = year ~ beef ~ fish;
    
    //%s indicates the location of the contents of the original string
    fmt = "Year %s" $~ "%s cts/lb" $~ "%s $/kg";
    
    // Convert the numeric matrix to a string
    commodity_prices = ntos(commodity_prices);
    
    // Apply formatting
    commodity_prices_fmt = satostrC(commodity_prices, fmt);

After the code above, *commodity_prices_fmt* should be equal to:

::

    "Year 2012"   "187.9 cts/lb"     "4.8 $/kg" 
    "Year 2013"   "183.6 cts/lb"     "6.8 $/kg" 
    "Year 2014"   "224.1 cts/lb"     "6.6 $/kg"

Source
------

strfns.src

.. seealso:: Functions :func:`strcombine`

