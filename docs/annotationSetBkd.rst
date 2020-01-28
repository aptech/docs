
annotationSetBkd
==============================================

Purpose
----------------
Sets the background color and opacity level for a textbox, rectangle or ellipse.

Format
----------------
.. function:: annotationSetBkd(&myAnnotation, color, opacity)

    :param &myAnnotation:
    :type &myAnnotation: A pointer to an instance of a :class:`plotAnnotation` structure.

    :param color: color name or hex HTML color code.
    :type color: string

    :param opacity: opacity percentage. Valid range is between 0 and 1.
    :type opacity: scalar

Examples
----------------

Using a color string
++++++++++++++++++++

::

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();

    // Set background to light gray with 40% opacity
    annotationSetBkd(&myAnnotation, "light gray", 0.4);


Full example using an HTML color code
+++++++++++++++++++++++++++++++++++++

::

    // Create and plot some simple data
    x = seqa(1, 1, 10);
    y = rndu(10, 1);
    plotXY(x, y);

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation
    ** structure and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();

    // Set background to white with 80% opacity
    annotationSetBkd(&myAnnotation, "#FFFFFF", 0.8);

    // Add rectangle to 'xy' plot from above
    // using settings from 'myAnnotation'
    plotAddShape(myAnnotation, "rectangle", 1, 0.2, 3, 0.5);

.. seealso:: Functions :func:`plotAddTextbox`, :func:`plotAddShape`, :func:`annotationGetDefaults`
