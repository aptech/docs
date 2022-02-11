
annotationSetTextAlign
==============================================

Purpose
----------------
Sets the alignment for the text inside of textbox annotations. To control the anchoring position of a textbox relative to the datapoint position, use reference the optional argument in :func:`plotAddTextbox` itself. This setting only works for the ``"Plain"`` and ``"HTML"`` interpreters.

Format
----------------
.. function:: annotationSetTextAlign(&myAnnotation, alignment)

    :param &myAnnotation: A pointer to an instance of a :class:`plotAnnotation` structure.
    :type &myAnnotation: struct

    :param alignment: text alignment. Valid options include:

        - ``"left"`` (Default)
        - ``"right"``
        - ``"center"``
        - ``"justify"``

    :type alignment: string

Examples
----------------

Basic usage
+++++++++++

::

    plotXY(seqa(-5,1,10), rndi(10,1, -10|10));
    plotAddVLine(0);
    plotAddHLine(0);

    /*
    ** Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    ** and fill it in with default values
    */
    struct plotAnnotation myAnnotation;
    myAnnotation = annotationGetDefaults();

    // Set text alignment to center
    annotationSetTextAlign(&myAnnotation, "center");

    // Plot an origin label at the center with centered text.
    plotAddTextbox(myAnnotation, "Origin", 0, 0, "center");

.. seealso:: Functions :func:`plotAddTextbox`, :func:`plotAddArrow`, :func:`plotAddShape`, :func:`annotationGetDefaults`

