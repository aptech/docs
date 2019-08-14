
getHSLPalette
==============================================

Purpose
----------------
Create a set of evenly spaced colors in HSL hue space. The *h*, *s*, and *l* arguments must all be between 0 and 1.

Format
----------------
.. function:: clrs = getHSLPalette(ncolors[, h[, s[, l]]])

    :param ncolors: The number of colors to create for the palette.
    :type ncolors: scalar

    :param h: Optional input, first hue. Default value is 0.01.
    :type h: scalar

    :param s: Optional input, saturation. Default value is 0.65.
    :type s: scalar

    :param l: Optional input, lightness. Default value is 0.6.
    :type l: scalar

    :return clrs: contains the newly created color palette.

    :type clrs: ncolorsx1 string array

Examples
----------------

::

    // Get the first 3 colors HSL colors
    hsl_clrs = getHSLPalette(3);


After the above code, *hsl_clrs* should equal:


::

    #db5f57
    #57db5f
    #5f57db

.. seealso:: Functions :func:`getColorPalette`, :func:`listColorPalettes`, :func:`getHSLuvPalette`, :func:`blendColorPalette`
