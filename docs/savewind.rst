
savewind
==============================================

Purpose
----------------

Save the current graphic panel configuration to a file.

.. NOTE:: This function is for use with the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: err = savewind(filename)

    :param filename: name of file.
    :type filename: string

    :return err: 0 if successful, 1 if graphic panel matrix is invalid. Note that the file is written in either case.

    :rtype err: scalar

Remarks
-------

See the discussion on using graphics panels in `Tiled Graphic Panels <PQG.3.1-TiledGraphicPanels.html>`_.

Source
------

pwindow.src

.. seealso:: Functions :func:`loadwind`

