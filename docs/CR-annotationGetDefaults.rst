
annotationGetDefaults
==============================================

Purpose
----------------
Fills in an instance of a plotAnnotation structure with default values.

Format
----------------
.. function:: annotationGetDefaults()

    :returns: myAnnotation (*TODO*), An instance of a plotAnnotation structure with all members set to defaults.

Examples
----------------

::

    // Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    struct plotAnnotation myAnnotation;
    
    // Fill in 'myAnnotation' with default values
    myAnnotation = annotationGetDefaults();

.. seealso:: Functions :func:`plotAddShape`, :func:`plotAddTextbox`, :func:`annotationSetLineColor`, :func:`annotationSetBkd`
