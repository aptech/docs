
plotCanvasSize
==============================================

Purpose
----------------

Controls the size of the canvas on which the next plot is drawn.

Format
----------------
.. function:: plotCanvasSize("fill")
              plotCanvasSize(units, size[, dpi])

    :param units: the units of measurement for *size*, *width* and *height*. 
    
        Valid options include:
        
        ===== ============
        "cm"  centimeters
        "in"  inches
        "mm"  millimeters
        "px"  pixels. 
        ===== ============
        
        If the string "fill" is the only input, the graph canvas will stretch to fit the available area.

    :type units: string

    :param size: the *width* and *height* to set the graph canvas in terms of the specified units.
    :type size: 2x1 matrix

    :param dpi: the number of dots per inch. This option applies only to physical measurements, such as centimeters and inches. It will be ignored if the "units" input is set to *pixels*.
    :type dpi: scalar

Remarks
-------

If the only input to :func:`plotCanvasSize` is the string "fill", then the graph
canvas will be expanded to fill the available area.

:func:`plotSetCanvas` controls the size of the entire graph canvas, not just a
set of axes. Therefore when used with :func:`plotLayout` to create subplots,
:func:`plotSetCanvas` will control the size of the bounding box allowed for all
of the subplots together.

After a call to :func:`plotSetCanvas`, all subsequent graphs will be drawn in a
canvas of the size specified even if a new plot tab is created with
:func:`plotOpenWindow`.

Examples
----------------

::

    // Get file name with full path
    dataset = getGAUSSHome() $+ "examples/beef_prices.csv";
    
    // Load variable 'beef_price' from dataset
    // and perform ln transform on variable
    ln_price = loadd(dataset, "ln(beef_price)");
    
    // Set plot canvas to be 640 by 480 pixels
    plotCanvasSize("px", 640 | 480);
    
    // Create x and draw graph in the 640 px by 480 px plot canvas
    x = seqa(1, 1, rows(ln_price));
    plotXY(x, ln_price);

.. seealso:: Functions :func:`plotOpenWindow`, :func:`plotSave`

