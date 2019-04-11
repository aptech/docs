
fonts
==============================================

Purpose
----------------

Loads fonts to be used in the graph. 

.. NOTE:: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: fonts(str)

    :param str:  The following fonts are available:

        .. csv-table::
            :widths: auto
    
            "Simplex", "standard sans serif font."
            "Simgrma", "Simplex greek, math."
            "Microb", "bold and boxy."
            "Complex", "standard font with serif."

    :type str: string or character vector containing the names of fonts to be used in the plot

Remarks
-------

The first font specified will be used for the axes numbers.

If *str* is a null string, or :func:`fonts` is not called, Simplex is loaded by
default.

For more information on how to select fonts within a text string, see
`Publication Quality Graphics`, Chapter 1.



Source
------

pgraph.src

.. seealso:: Functions :func:`title`, :func:`xlabel`, :func:`ylabel`, :func:`zlabel`

