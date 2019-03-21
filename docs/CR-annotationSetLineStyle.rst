
annotationSetLineStyle
==============================================

Purpose
----------------
Sets the line style for textbox, rectangle or ellipse borders as well as the style for lines and arrows.

Format
----------------
.. function:: annotationSetLineStyle(&myAnnotation, style)

    :param &myAnnotation: A pointer to an instance of a :class:`plotAnnotation` structure.
    :type &myAnnotation: struct

    :param style: line style. Valid options include:

        .. csv-table::
            :widths: auto

            "1","solid"
            "2","dash"
            "3","dot"
            "4","dash-dot"
            "5","dash-dot-dot"

    :type style: matrix

Examples
----------------

Basic usage
+++++++++++

::

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    // Set line style to 'dot'
    line_style = 3;
    annotationSetLineStyle(&myAnnotation,line_style);

Full example creating an ellipse with a dash border
+++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create and plot some simple data
    x = seqa(0.1, 0.2, 10);
    y = 3 .* sin(x) + rndu(10, 1);
    plotXY(x, y);
    
    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    // Set line style to dash (for ellipse border in this case)
    annotationSetLineStyle(&myAnnotation, 2);
    
    /*
    ** Add ellipse to 'xy' plot from above
    ** using settings from 'myAnnotation'
    */
    plotAddShape(myAnnotation, "ellipse", 0.4, 1.5, 1, 2.9);

.. seealso:: Functions :func:`plotAddTextbox`, :func:`plotAddArrow`, :func:`plotAddShape`, :func:`annotationGetDefaults`

