
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
.. function:: savewind(filename)

    :param filename: name of file.
    :type filename: string

    :returns: err (*scalar*), 0 if successful, 1 if graphic panel matrix is invalid. Note that the file is written in either case.

Remarks
-------

See the discussion on using graphics panels in **Tiled Graphic Panels**, Section 1.0.1.

Source
------

pwindow.src

.. seealso:: Functions :func:`loadwind`

