
reclassifyCuts
==============================================

Purpose
----------------
Replaces values of a matrix or array within specified ranges

Format
----------------
.. function:: reclassifyCuts(x, cut_pts, close_right)

    :param x: string array or NxKxP array to be recoded (changed)
    :type x: NxK matrix

    :param cut_pts: bounds of the specified ranges
    :type cut_pts: kx1 vector

    :param close_right: optional argument, 1 if the cut_pts should be the right end-point of the interval, or 0 if the values in cut_pts should start the next interval
    :type close_right: Scalar

    :returns: x_new (*Matrix*), multi-dimensional array or string array with the same dimensions as the input x, containing the recoded values of
        x

Examples
----------------

Basic sequence
++++++++++++++

::

    // Create column vector to place in categories
    x = {  0,
          0.1,
          0.2,
          0.3,
          0.4,
          0.5,
          0.6,
          0.7 };
    
    // Cut points for data in 'x'
    cut_pts = { 0.2,
                0.5 };
    
    // Class 0: 	  x <= 0.2
    // Class 1: 0.2 < x <= 0.5
    // Class 2: 0.5 < x
    r_open = reclassifyCuts(x, cut_pts);
    
    // Class 0: 	  x < 0.2
    // Class 1: 0.2 < x < 0.5
    // Class 2: 0.5 < x 
    r_closed = reclassifyCuts(x, cut_pts, 1);
    				
    print "x = " x; 
    print;								
    print "r_open = " r_open;
    print;
    print "r_closed = " r_closed;				
    print;
    print "cut_pts = " cut_pts;

After the code above:

::

    x = 
    0.00 
    0.10 
    0.20 
    0.30 
    0.40 
    0.50 
    0.60 
    0.70 
    
    r_open = 
    0.00 
    0.00 
    0.00 
    1.0 
    1.0 
    1.0 
    2.0 
    2.0 
    
    r_closed = 
    0.00 
    0.00 
    1.0 
    1.0 
    1.0 
    2.0 
    2.0 
    2.0 
    
    cut_pts = 
    0.20 
    0.50

Classifying blood pressure data
+++++++++++++++++++++++++++++++

::

    // Create a column of blood pressure data
    bp = {  87, 
           154,
           127,
           112,  
           159,
            90, 
           151,
           109,
           125,
           107 };
    
    // Assign cut points
    cut_pts = { 120, 140 };
    
    // Create categorical variable
    bp_category = reclassifyCuts(bp, cut_pts);
    				
    print "bp = " bp;
    print;
    print "bp_category = " bp_category;				
    print;
    print "cut_pts = " cut_pts;

After the code above:

::

    bp = 
    87.00 
    154.0 
    127.0 
    112.0 
    159.0 
    90.00 
    151.0 
    109.0 
    125.0 
    107.0 
    
    bp_category = 
    0.0000 
    2.000 
    1.000 
    0.0000 
    2.000 
    0.0000 
    2.000 
    0.0000 
    1.000 
    0.0000 
    
    cut_pts = 
    120.0 
    140.0

We can take the categorical data output from reclassifyCuts and use the reclassify function to change the numeric categories to string categories like this:

::

    // Starting categories
    from = { 0, 1, 2 };
    
    // New categories
    to = "normal" $| "prehypertension" $| "hypertension";
    
    bp_category = reclassify(bp_category, from, to);
    print "bp_category = " bp_category;

After the code above:

::

    bp_category = 
    normal 
    hypertension 
    prehypertension 
    normal 
    hypertension 
    normal 
    hypertension 
    normal 
    prehypertension 
    normal

Source
------

datatran.src

.. seealso:: Functions :func:`code`, :func:`recode`, :func:`reclassify`, :func:`substute`, :func:`rescale`
