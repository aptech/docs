
loadwind
==============================================

Purpose
----------------

Load a previously saved graphic panel configuration. 

.. NOTE:: This function is for use with the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: err = loadwind(namestr)

    :param namestr: name of file to be loaded.
    :type namestr: string

    :return err: 0 if successful, 1 if graphic panel matrix
        is invalid. Note that the current graphic panel configuration will
        be overwritten in either case.

    :type err: scalar

Globals
-------

\_pwindmx

Source
------

pwindow.src

.. seealso:: Functions :func:`savewind`

