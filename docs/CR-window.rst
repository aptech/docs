
window
==============================================

Purpose
----------------
Partitions the window into tiled regions (graphic panels) of equal size. NOTE: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: window(row, col, typ)

    :param row: number of rows of graphic panels.
    :type row: scalar

    :param col: number of columns of graphic panels.
    :type col: scalar

    :param typ: graphic panel attribute type. If 1, the graphic
        panels will be transparent, if 0, the graphic panels will be
        nontransparent (blanked).
    :type typ: scalar



Remarks
-------

The graphic panels will be numbered from 1 to (row) x (col) starting
from the left topmost graphic panel and moving right.

See makewind for creating graphic panels of a specific size and
position. (For more information, see **Graphic Panels**, Section 1.1.



Source
------

pwindow.src

.. seealso:: Functions :func:`endwind`, :func:`begwind`, :func:`setwind`, :func:`nextwind`, :func:`getwind`, :func:`makewind`
