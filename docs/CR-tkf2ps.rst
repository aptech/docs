
tkf2ps
==============================================

Purpose
----------------

Converts a *.tkf* file to a PostScript file.

.. NOTE:: This function is deprecated and does not work for the new *.plot* graphics files. Use :func:`plotSave` to convert *.plot* files to PS format.

Library
-------

pgraph

Format
----------------
.. function:: ret = tkf2ps(tekfile, psfile)

    :param tekfile: name of *.tkf* file.
    :type tekfile: string

    :param psfile: name of PostScript file.
    :type psfile: string

    :return ret: 0 if successful.

    :rtype ret: scalar

Remarks
-------

The conversion is done using the global parameters in :file:`peps.dec`. You can
modify these globally by editing the *.dec* file, or locally by setting
them in your program before calling :func:`tkf2ps`.

See the header of the output PostScript file and a PostScript manual if
you want to modify these parameters.

