
subscat
==============================================

Purpose
----------------
Changes the values in a vector depending on the category a particular element falls in.

Format
----------------
.. function:: subscat(x, breaks, levels)

    :param x: 
    :type x: Nx1 vector

    :param breaks: containing breakpoints
        specifying the ranges within which substitution
        is to be made. This MUST be sorted in ascending
        order.
        breaks can contain a missing value as a separate category
        if the missing value is the first element in  breaks.If breaks is a scalar, all matches must be exact for a substitution to be made.
    :type breaks: Px1 numeric vector

    :param levels: containing values to be substituted.
    :type levels: Px1 vector

    :returns: y (*Nx1 vector*), with the elements in  levels substituted for
        the original elements of x according to which of
        the regions the elements of x fall into:
        x ≤ breaks[1] → levels[1]
        breaks[1] < x ≤ breaks[2] → levels[2]
        ...
        breaks[p - 1] < x ≤ breaks[p] → levels[p]
        x > breaks[p] → the original value of x
        If missing is not a category specified in  breaks,
        missings in x are passed through without change.

Examples
----------------

//BMI Data
bmi = { 36, 
        19, 
        24, 
        38, 
        34, 
        16, 
        26, 
        37, 
        20, 
        34 };

//Set the breakpoints for the new categories
breaks = { 18.5, 25, 30, 40 };

//The categorical levels
levels = { 0, 1, 2, 3 };

bmi_levels = subscat(bmi, breaks, levels);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The above code assigns the following values:

::

    bmi = 36   bmi_levels = 3 
          19                1 
          24                1 
          38                3 
          34                3 
          16                0 
          26                2 
          37                3 
          20                1 
          34                3

This example combines 2 levels in a categorical label into one category.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create categorical vector with 3 levels
    x = { 1, 
          1, 
          2,
          2,
          1, 
          1,
          2, 
          0, 
          2, 
          0 }; 
    
    // Assign all instances of 2 to 1, merging the second and third categories
    x = subscat(x, 2, 1);

After the code above, x is equal to:

::

    1 
    1 
    1 
    1 
    1 
    1 
    1 
    0 
    1 
    0

Replacing instances of one particular value with another value can also be accomplished with reclassify and substute

Remarks
-------

reclassifyCuts offers functionality similar to subscat, but:

-  Also assigns values to data past the final breakpoint.
-  Offers the option of whether the breakpoints are open or closed on
   the right(e.g., < or ≤).
-  Assigns the input to two categories in the case of a single
   breakpoint, (e.g., level_1 < break < level_2). Whereas, subscat tests
   for equality in the case of a single breakpoint.

.. seealso:: Functions :func:`reclassify`, :func:`reclassifyCuts`, :func:`substute`
