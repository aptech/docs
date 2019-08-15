
tkf2eps
==============================================

Purpose
----------------

Converts a :file:`.tkf` file to an Encapsulated PostScript file.

.. NOTE:: This function is deprecated and does not work for the new :file:`.plot` graphics files. Use :func:`plotSave` to convert :file:`.plot` files to EPS format.

Library
-------

pgraph

Format
----------------
.. function:: ret = tkf2eps(tekfile, epsfile)

    :param tekfile: name of :file:`.tkf` file.
    :type tekfile: string

    :param epsfile: name of Encapsulated PostScript file.
    :type epsfile: string

    :return ret: 0 if successful

    :rtype ret: scalar

Remarks
-------

The conversion is done using the global parameters in :file:`peps.dec`. You can
modify these globally by editing the :file:`.dec` file, or locally by setting
them in your program before calling :func:`tkf2eps`.

See the header of the output Encapsulated PostScript file and a
PostScript manual if you want to modify these parameters.

