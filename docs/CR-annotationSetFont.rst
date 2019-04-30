
annotationSetFont
==============================================

Purpose
----------------
Sets the font properties of a plotAnnotation structure for controlling text boxes added to a graph.

Format
----------------
.. function:: annotationSetFont(&myAnnotation, fontname, fontsize, fontcolor)

    :param &myAnnotation: A :class:`plotAnnotation` structure pointer.
    :type &myAnnotation: struct

    :param fontname: the name of the font.
    :type fontname: string

    :param fontsize: the size of the font in points.
    :type fontsize: scalar

    :param fontcolor: a color or HTML hexidecimal color code.
    :type fontcolor: string

Remarks
-------

:func:`annotationSetFont` does not currently support surface plots.

Examples
----------------

Basic usage
+++++++++++

::

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation
    ** structure and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();
    
    annotationSetFont(&myAnnotation, "arial", 14, "black");

Customized textbox
++++++++++++++++++

::

    // Create a simple plot on which to add a textbox
    x = seqa(pi, 0.1, 50);
    plotXY(x, sin(x) + rndu(50, 1));
    
    /*
    ** Declare instance of plotAnnotation structure
    ** and fill in with default values
    */
    struct plotAnnotation myTextbox;
    myTextbox = annotationGetDefaults();
    
    // Set font to dark-gray, 14pt times
    annotationSetFont(&myTextbox, "times", 14, "dark gray");
    
    // Create text for textbox
    box_text = "Trend change in Q2";
    
    // The top-left corner of the text box
    // will start at the point (3.5,1.5)
    x_start = 3.5;
    y_start = 1.5;
    
    // Add textbox to last draw graph
    plotAddTextbox(myTextbox, box_text, x_start, y_start);

.. seealso:: Functions :func:`plotAddShape`, :func:`plotAddTextbox`, :func:`annotationGetDefaults`

