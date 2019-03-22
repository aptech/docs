
getHSLPalette
==============================================

Purpose
----------------
Create a set of evenly spaced colors in HSL hue space. The h, s, and l arguments must all be between 0 and 1.

Format
----------------
.. function:: getHSLPalette(ncolors, h, s, l)

    :param ncolors:  The number of colors to create for the palette.
    :type ncolors: scalar

    :param h:  first hue. Default value is 0.01.
    :type h: scalar

    :param s:  saturation. Default value is 0.6.5
    :type s: scalar

    :param l:  lightness. Default value is 0.6.
    :type l: scalar

    :returns: clrs (*ncolorsx1 string array*) containing the newly created color palette.

