
nextwind
==============================================

Purpose
----------------

Set the current graphic panel to the next available graphic panel.

.. NOTE:: This function is for use with the deprecated PQG graphics. For similar functionality use :func:`plotLayout` instead.

Library
-------

pgraph

Format
----------------
.. function:: nextwind()

Remarks
-------

This function selects the next available graphic panel to be the current
graphic panel. This is the graphic panel in which the next graph will be
drawn.

See the discussion on using graphic panels in **Tiled Graphic Panels**, Section 1.0.1.

Source
------

pwindow.src

.. seealso:: Functions :func:`endwind`, :func:`begwind`, :func:`setwind`, :func:`getwind`, :func:`makewind`, :func:`window`

