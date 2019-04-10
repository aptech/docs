
getwind
==============================================

Purpose
----------------

Retrieve the current graphic panel number. 

.. NOTE:: This function is for use with the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------

.. function:: getwind()

    :returns: n (*scalar*), graphic panel number of current graphic panel.

Remarks
-------

The current graphic panel is the graphic panel in which the next graph
will be drawn.

Source
------

pwindow.src

.. seealso:: Functions :func:`endwind`, :func:`begwind`, :func:`window`, :func:`setwind`, :func:`nextwind`

