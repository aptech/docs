
plotSave
==============================================

Purpose
----------------

Saves the last created graph to a user specified file type.

Format
----------------
.. function:: plotSave(filename[, size[, units[, dpi]]])

    :param filename: name of the file to create with a file type extension.
        Available file extensions include: .jpg, .plot, .png, .pdf, .svg, .tiff 
        
        .. NOTE:: Available file types may vary per system. A list of valid types can be found in the :menuselection:`File --> Export Graph` file dialog window.

    :type filename: string

    :param size: dimensions of the saved graph in specified units. Default *unit* is centimeters. *size* is an optional input when saving a :file:`.plot` file, but is required for all other file types.
    :type size: 2x1 vector

    :param unit: Optional input, type of units dimension is specified in. This value is ignored if the filename extension is ':file:`.plot`'. Valid options include:

        ==== =============
        "cm" Centimeters (Default)
        "mm" Millimeters
        "in" Inches
        "px" Pixels
        ==== =============

    :type unit: string

    :param dpi: Optional input, requested dots per inch when saving file. Defaults to current system dpi. This value is ignored if the filename extension is ':file:`.plot`'.
        *dpi* determines the number of pixels rendered when saving a file in terms of physical dimensions (cm, mm, in). Specifying the *dpi* parameter has no effect if the specified units are pixels (px).

        e.g. if a printing requirement demanded 11"x8.5" (landscape) with 300 dpi then the plot could be made to fit those dimensions exactly with the line:
        
        ::

            plotSave("file.pdf", 11|8.5, "in", 300);

        which would create an output of 3300x2550 pixels with the PDF page size set in the specified physical dimensions.

    :type dpi: scalar

Examples
----------------

Basic save in GAUSS .plot format
++++++++++++++++++++++++++++++++

::

    // Create data
    x = seqa(0.1, 0.1, 10);
    y = cos(x);
    
    // Plot the data
    plotXY(x, y);
    
    // Save the graph as a GAUSS .plot file
    plotSave("mygraph.plot");

Save as 640x480 PNG
+++++++++++++++++++

::

    // Create data
    x = seqa(0.1, 0.1, 10);
    y = cos(x);
    
    // Plot the data
    plotXY(x, y);
    
    // Save the graph as a 640 wide by 480 tall PNG file
    plotSave("mygraph.png", 640 | 480, "px");

Save as 11x8.5 inch PDF at 300 DPI
++++++++++++++++++++++++++++++++++

::

    // Create data
    x = seqa(0.1, 0.1, 10);
    y = cos(x);
    
    // Plot the data
    plotXY(x, y);
    
    plotSave("mygraph.png", 11 | 8.5, "in", 300);

Remarks
-------

The font sizes in the graph will not be scaled with the size change. So
make sure to set the font sizes to the correct size for the final graph
dimensions.

Technical Notes
---------------

The :file:`.plot` file extension is a JSON file that is the native format used
by GAUSS to save graphs.

.. seealso:: Functions :func:`plotCustomLayout`, :func:`plotSetLegend`, :func:`plotCanvasSize`

