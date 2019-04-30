
plotClearLayout
==============================================

Purpose
----------------
Clears any previously set plot layouts.

Format
----------------
.. function:: plotClearLayout()

Remarks
-------

After calling this function all subsequent graphs will be drawn to fill the entire graph window.

Examples
----------------

::

    //Create a 1x2 Plot Layout and insert a percentage
    //histogram of some random normal numbers in the first cell
    plotLayout(1, 2, 1);
    plotHistP(rndn(1000, 1), 30);
    
    //Insert gamma distributed random numbers into the second cell
    plotLayout(1, 2, 2);
    plotHistP(rndGamma(1000, 1, 3, 2), 30);
    
    //Display the image for 2 seconds
    pause(2);
    
    //Clear the 1x2 layout
    plotClearLayout();
    
    //Plot percentage histogram of beta distributed random
    //numbers. This graph will take up the entire plot window
    //since the 1x2 plot layout has been cleared.
    plotHistP(rndBeta(1000, 1, 2, 1), 30);

.. seealso:: Functions :func:`plotSetBar`, :func:`plotBar`, :func:`plotLayout`, :func:`plotCustomLayout`

