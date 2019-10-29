
setwind
==============================================

Purpose
----------------

Sets the current graphic panel to a previously created graphic
panel number.

.. NOTE:: This function is for use with the deprecated PQG graphics. Use :func:`plotLayout` instead.

Library
-------

pgraph

Format
----------------
.. function:: setwind(n)

    :param n: graphic panel number.
    :type n: scalar

Remarks
-------

This function selects the specified graphic panel to be the current
graphic panel. This is the graphic panel in which the next graph will be
drawn.

See the discussion on using graphic panels in **Graphic Panels**,
Section 1.1.

Source
------

pwindow.src

.. seealso:: Functions :func:`begwind`, :func:`endwind`, :func:`getwind`, :func:`nextwind`, :func:`makewind`, :func:`window`
