
setvwrmode
==============================================

Purpose
----------------

Sets the graphics viewer mode.

.. NOTE:: This function is for use with the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: oldmode = setvwrmode(mode)

    :param mode: new mode or null string.

        ====== ===============================
        "one"  Use only one viewer.
        "many" Use a new viewer for each graph.
        ====== ===============================

    :type mode: string

    :return oldmode: previous *mode*.

    :rtype oldmode: string

Remarks
-------

If *mode* is a null string, the current mode will be returned with no changes made.

If "one" is set, the viewer executable will be :func:`vwr.exe`.


Examples
----------------

::

    oldmode = setvwrmode("one");
    call setvwrmode(oldmode);

Source
------

pgraph.src

.. seealso:: Functions :func:`pqgwin`

