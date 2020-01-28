
box
==============================================

Purpose
----------------
Graphs data using the box graph percentile method.

.. NOTE:: This function uses the deprecated PQG graphics. Use :func:`plotBox` instead.

Library
-------
pgraph

Format
----------------
.. function:: box(grp, y)

    :param grp: This contains the group numbers corresponding to each column of *y* data.
        If scalar 0, a sequence from 1 to ``cols(y)`` will be generated automatically for the x-axis.
    :type grp: 1xM vector

    :param y: Each column represents the set of *y* values for an individual percentiles box symbol.
    :type y: NxM matrix

Global Input
------------

.. data:: \_pboxctl

    5x1 vector, controls box style, width, and color.

    .. list-table::
        :widths: auto

        * - [1]
          - box width between 0 and 1. If zero, the box plot is drawn as two vertical lines representing the quartile ranges with a filled circle representing the 50th percentile.
        * - [2]
          - box color. If this is set to 0, the colors may be individually controlled using the global variable `\_pcolor`.
        * - [3]
          - Min/max style for the box symbol. One of the following

              :1: Minimum and maximum taken from the actual limits of the data. Elements 4 and 5 are ignored.
              :2: Statistical standard with the minimum and maximum calculated according to interquartile range as follows:

                  - intqrange = 75th - 25th
                  - min = 25th - 1.5 intqrange
                  - max = 75th + 1.5 intqrange
                  - Elements 4 and 5 are ignored.
              :3: Minimum and maximum percentiles taken from elements 4 and 5.
        * - [4]
          -  Minimum percentile value (0-100) if \_pboxctl[3] = 3.
        * - [5]
          - Maximum percentile value (0-100) if \_pboxctl[3] = 3.

.. data:: \_plctrl

    1xM vector or scalar as follows:

    .. csv-table::
        :widths: auto

        0, "Plot boxes only, no symbols."
        1, "Plot boxes and plot symbols which lie outside the min and max box values."
        2, "Plot boxes and all symbols."
        -1, "Plot symbols only, no boxes."

    These capabilities are in addition to the usual line control capabilities of \_plctrl.

.. data:: \_pcolor

    1xM vector or scalar for symbol colors. If scalar, all symbols will be one color.

Remarks
-------
If missing values are encountered in the *y* data, they will be ignored

Source
------
pbox.src
