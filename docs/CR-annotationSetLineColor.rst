
annotationSetLineColor
==============================================

Purpose
----------------
Sets the line color for textbox, rectangle or ellipse borders as well as the color for lines and arrows.

Format
----------------
.. function:: annotationSetLineColor(&myAnnotation, color)

    :param &myAnnotation: A pointer to an instance of a :class:`plotAnnotation` structure.
    :type &myAnnotation: struct

    :param color: named color or HTML hexadecimal color code. Note that HTML color codes must start with a `#`.
    :type color: string

Examples
----------------

Basic usage with named color
++++++++++++++++++++++++++++

::

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    // Set line color
    annotationSetLineColor(&myAnnotation, "blue");

Basic usage with HTML color code
++++++++++++++++++++++++++++++++

::

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    // Set line color
    annotationSetLineColor(&myAnnotation, "#CCCCCC");
    
Full example adding a red arrow to a graph
++++++++++++++++++++++++++++++++++++++++++

::

    // Create and plot some simple data
    x = seqa(0.1, 0.1, 30);
    y = cos(x);
    plotXY(x, y);
    
    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    // Set line color for arrow
    annotationSetLineColor(&myAnnotation, "red");
    
    /*
    ** Add arrow to 'xy' plot from above
    ** using settings from 'myAnnotation'
    */
    x_start = 0.15;
    y_start = 0.2;
    x_end = 1;
    y_end = 0.5;
    head_size = 15;
    plotAddArrow(myAnnotation, x_start, y_start, x_end, y_end, head_size);

.. seealso:: Functions :func:`plotAddTextbox`, :func:`plotAddArrow`, :func:`plotAddShape`, :func:`annotationGetDefaults`

