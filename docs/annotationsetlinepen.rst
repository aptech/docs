
annotationSetLinePen
==============================================

Purpose
----------------
Sets the line width and optionally color and style for textboxes, rectangle or ellipse borders as well as lines and arrows.

Format
----------------
.. function:: annotationSetLinePen(&myAnnotation, width [, clr, style])

    :param myAnnotation: A pointer to an instance of a :class:`plotAnnotation` structure
    :type myAnnotation: struct

    :param width: the width of the line in pixels.
    :type width: scalar

    :param clr: Optional argument, name or RGB value of the new color(s) for the line(s).
    :type clr: string or Nx1 string array

    :param style: Optional argument, the style(s) of the pen for the line(s). Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: Scalar or Nx1 matrix


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
    
    // Set line width to 1 pixel, but leave
    // color and style as they were
    annotationSetLinePen(&myAnnotation, 1);

::

    // Set line width to 2 pixels, and
    // color to black 
    annotationSetLinePen(&myAnnotation, 2, "black");

::

    // Set line width to 2 pixels,
    // color to black, and style to dot (3)
    annotationSetLinePen(&myAnnotation, 2, "black", 3);


Full example setting width of rectangle border
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create and plot some simple data
    x = seqa(-1.5, 0.1, 31);
    y = cos(x);
    plotXY(x, y);
    
    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    // Set line width to black and 1 pixel (for rectangle border in this case)
    annotationSetLinePen(&myAnnotation, 1, "black");
    
    /*
    ** Add rectangle to 'xy' plot from above
    ** using settings from 'myAnnotation'
    */
    x_start = -pi ./ 4;
    y_start = 0.07;
    x_end = pi ./ 4;
    y_end = 0.71;
    
    plotAddShape(myAnnotation, "rectangle", x_start, y_start, x_end, y_end);

.. seealso:: Functions :func:`plotAddTextbox`, :func:`plotAddArrow`, :func:`plotAddShape`, :func:`annotationGetDefaults`

