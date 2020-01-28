
title
==============================================

Purpose
----------------

Sets the title for the graph.

.. NOTE:: This function is for the deprecated PQG graphics. Use :func:`plotSetTitle` instead.

Library
-------

pgraph

Format
----------------
.. function:: title(str)

    :param str: the title to display above the graph.
    :type str: string

Examples
----------------

::

    title("First title line\LSecond title line\L"\
    "Third title line");

Fonts may be specified in the title string. For instructions on 
using fonts, see Selecting Fonts, Section 1.0.1.

Remarks
-------

Up to three lines of title may be produced by embedding a line feed
character (``"\L"``) in the title string.


Source
------

pgraph.src

.. seealso:: Functions :func:`xlabel`, :func:`ylabel`, :func:`fonts`

