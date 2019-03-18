
setvwrmode
==============================================

Purpose
----------------

Sets the graphics viewer mode. NOTE: This function is for use with the deprecated PQG graphics.

Format
----------------
.. function:: setvwrmode(mode)

    :param mode: new mode or null string.
    :type mode: string

    .. csv-table::
        :widths: auto

        ""one"", "Use only one viewer."
        ""many"", "Use a new viewer for each graph."

    :returns: oldmode (*string*), previous  mode.

Examples
----------------

::

    oldmode = setvwrmode("one");
    call setvwrmode(oldmode);

Source
++++++

pgraph.src

.. seealso:: Functions :func:`pqgwin`
