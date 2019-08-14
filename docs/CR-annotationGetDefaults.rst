
annotationGetDefaults
==============================================

Purpose
----------------
Fills in an instance of a :class:`plotAnnotation` structure with default values.

Format
----------------
.. function:: myAnnotation = annotationGetDefaults()

    :return myAnnotation: An instance of a :class:`plotAnnotation` structure with all members set to defaults.

    :type myAnnotation: struct

Remarks
-------

:class:`plotAnnotation` structures are used with the `annotationSet` functions to
programmatically control the attributes of the annotations that you add
to graphs.

To see a full example of adding an annotation to a graph, see the
command reference page for :func:`plotAddLine`, :func:`plotAddShape` or :func:`plotAddTextbox`

Examples
----------------

::

    // Declare 'myAnnotation' to be an instance of a plotAnnotation structure
    struct plotAnnotation myAnnotation;

    // Fill in 'myAnnotation' with default values
    myAnnotation = annotationGetDefaults();

.. seealso:: Functions :func:`plotAddShape`, :func:`plotAddTextbox`, :func:`annotationSetLineColor`, :func:`annotationSetBkd`
