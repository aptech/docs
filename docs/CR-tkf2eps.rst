
tkf2eps
==============================================

Purpose
----------------

Converts a *.tkf* file to an Encapsulated PostScript file.

.. NOTE:: This function is deprecated and does not work for the new *.plot* graphics files. Use :func:`plotSave` to convert *.plot* files to EPS format.

Library
-------

pgraph

Format
----------------
.. function:: ret = tkf2eps(tekfile, epsfile)

    :param tekfile: name of *.tkf* file.
    :type tekfile: string

    :param epsfile: name of Encapsulated PostScript file.
    :type epsfile: string

    :return ret: 0 if successful

    :rtype ret: scalar

Remarks
-------

The conversion is done using the global parameters in *peps.dec*. You can
modify these globally by editing the *.dec* file, or locally by setting
them in your program before calling :func:`tkf2eps`.

See the header of the output Encapsulated PostScript file and a
PostScript manual if you want to modify these parameters.

