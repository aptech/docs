

The axis updated by this function is determined by the value previously specified by :func:`plotSetActiveX`. The accepted values are ``"bottom"`` (default), ``"top"``, and ``"both"``.

.. note:: Future calls to :func:`plotSetActiveX` will not retroactively change the values of a previously modified axis.

If you are using :func:`plotSetWhichXAxis` to graph along the ``top`` axis, instantiating your :class:`plotControl` structure in the following manner will have all ``plotSet`` functions apply to the ``top`` x-axis:

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure from relevant profile name/type.
    myPlot = plotGetDefaults("XY");

    // Graph along the top axis.
    plotSetWhichXAxis(&myPlot, "top");

    // All plotSet* functions will modify only the top x-axis until
    // plotSetActiveX is called again with a different value.
    plotSetActiveX(&myPlot, "top");

    ...

    plotXY(myPlot, ...);


