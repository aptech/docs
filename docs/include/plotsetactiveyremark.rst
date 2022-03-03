

The axis updated by this function is determined by the value previously specified by :func:`plotSetActiveY`. The accepted values are ``"left"`` (default), ``"right"``, and ``"both"``.

.. note:: Future calls to :func:`plotSetActiveY` will not retroactively change the values of a previously modified axis.

If you are using :func:`plotSetWhichYAxis` to graph along the ``right`` axis, instantiating your :class:`plotControl` structure in the following manner will have all ``plotSet`` functions apply to the ``right`` y-axis:

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure from relevant profile name/type.
    myPlot = plotGetDefaults("XY");

    // Graph along the right axis.
    plotSetWhichYAxis(&myPlot, "right");

    // All plotSet* functions will modify only the right y-axis until
    // plotSetActiveY is called again with a different value.
    plotSetActiveY(&myPlot, "right");

    ...

    plotXY(myPlot, ...);


