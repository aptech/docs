
blendColorPalette
==============================================

Purpose
----------------
Create a new palette that blends between a list of colors. 

Format
----------------
.. function:: blendColorPalette(colors, n_colors)

    :param colors:  List of existing colors.
    :type colors: Nx1 string array

    :param n_colors:  The number of colors to create for the new palette.
    :type n_colors: scalar

    :returns: color_blend (*n_colorsx1 string array*) containing color palette.

Remarks
----------------
*n_colors* must be greater than the length of the *colors* vector.

.. seealso:: :func:`getColorPalette`, :func:`listColorPalettes`, :func:`getHSLPalette`, :func:`getHSLuvPalette`
