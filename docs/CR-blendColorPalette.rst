
blendColorPalette
==============================================

Purpose
----------------
Create a new palette that blends between a list of colors. *ncolors* must be greater than the length of the *colors* vector.

Format
----------------
.. function:: blendColorPalette(colors, ncolors)

    :param colors:  List of existing colors.
    :type colors: Nx1 string array

    :param ncolors:  The number of colors to create for the new palette.
    :type ncolors: scalar

    :returns: color_blend (*Ncolorsx1 string array*) containing color palette.

.. seealso:: :func:`getColorPalette`, :func:`listColorPalettes`, :func:`getHSLPalette`, :func:`getHSLuvPalette`
