
makewind
==============================================

Purpose
----------------

Creates a graphic panel of specific size and position and adds it to the list of graphic panels. Note: This function is for the deprecated PQG graphics. For similar functionality, see plotLayout and plotCustomLayout.

Format
----------------
.. function:: makewind(xsize, ysize, xshft, yshft, typ)

    :param xsize: horizontal size of the graphic panel in inches.
    :type xsize: scalar

    :param ysize: vertical size of the graphic panel in inches.
    :type ysize: scalar

    :param xshft: horizontal distance from left edge of
        window in inches.
    :type xshft: scalar

    :param yshft: vertical distance from bottom edge of
        window in inches.
    :type yshft: scalar

    :param typ: graphic panel attribute type. If this value is
        1, the graphic panels will be transparent.
        If 0, the graphic panels will be nontransparent.
    :type typ: scalar



Remarks
-------

Note that if this procedure is used when rotating the page, the passed
parameters are scaled appropriately to the newly oriented page. The size
and shift values will not be true inches when printed, but the graphic
panel size to page size ratio will remain the same. The result of this
implementation automates the rotation and eliminates the required
graphic panel recalculations by the user.

See the window command for creating tiled graphic panels. For more
information on using graphic panels, see **Tiled Graphic Panels**,
Section 1.0.1.



Source
------

pwindow.src

.. seealso:: Functions :func:`window`, :func:`endwind`, :func:`setwind`, :func:`getwind`, :func:`begwind`, :func:`nextwind`
