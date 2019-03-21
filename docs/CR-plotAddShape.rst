
plotAddShape
==============================================

Purpose
----------------
Adds an arrow, line, ellipse or rectangle to an existing graph.

Format
----------------
.. function:: plotAddShape(myAnnotation, which_shape, x_start, y_start, x_end, y_end) 
			              plotAddShape(which_shape, x_start, y_start, x_end, y_end)

    :param myAnnotation: an instance of a plotAnnotation structure.
    :type myAnnotation: Optional argument

    :param which_shape: indicating which shape to create, options include:
        ellipseline (to which you may add an arrow head)rectangle
    :type which_shape: String

    :param x_start: the X coordinate for the start of the bounding box for each respective shape.
    :type x_start: Scalar or Nx1 vector

    :param y_start: the Y coordinate for the start of the bounding box for each respective shape.
    :type y_start: Scalar or Nx1 vector

    :param x_end: the X coordinate for the end of the bounding box for each respective shape.
    :type x_end: Scalar or Nx1 vector

    :param y_end: the Y coordinate for the end of the bounding box for each respective shape.
    :type y_end: Scalar or Nx1 vector

Examples
----------------
Example

::

    //Draw simple graph
    x = rndu(10, 1);
    y = rndu(10, 1);
    plotScatter(x, y);
    
    //The rectangle will be drawn between
    //third and sixth points on the plot
    x_start = x[3];
    y_start = y[3];
    x_end = x[6];
    y_end = y[6];
    
    //Shape type will be rectangle
    annotation_type = "rectangle";
    
    //Add rectangle to graph
    plotAddShape(annotation_type, x_start, y_start, x_end, y_end);

.. seealso:: Functions :func:`plotAddTextbox`, :func:`annotationGetDefaults`
