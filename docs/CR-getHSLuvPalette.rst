
getHSLuvPalette
==============================================

Purpose
----------------
Create a set of evenly spaced circular hues in the HSLuv system.

Format
----------------
.. function:: clrs = getHSLuvPalette(ncolors[, h[, s[, l]]])

    :param ncolors:  The number of colors to create for the palette
    :type ncolors: scalar

    :param h: Optional. first hue. Default value is 0.01
    :type h: scalar

    :param s: Optional. saturation. Default value is 0.9
    :type s: scalar

    :param l: Optional. lightness. Default value is 0.65
    :type l: scalar

    :return clrs: contains the newly created color palette.

    :type clrs: ncolorsx1 string array

Examples
----------------

::

      // Get the first 3 colors HSL colors
      hsluv_clrs = getHSLuvPalette(3);


After the above code, *hsluv_clrs* should equal:

::

    #f77189
    #50b131
    #3ba3ec

.. seealso:: Functions :func:`getColorPalette`, :func:`listColorPalettes`, :func:`getHSLPalette`, :func:`blendColorPalette`
