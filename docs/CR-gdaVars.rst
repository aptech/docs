
gdaVars
==============================================

Purpose
----------------

Gets the number of variables in a GAUSS Data Archive.

Format
----------------
.. function:: nvars = gdaVars(filename)

    :param filename: name of data file.
    :type filename: string

    :return nvars: the number of variables in  filename.

    :type nvars: scalar

Examples
----------------

::

    nvars = gdaVars("myfile.gda");

Source
------

gdafns.src

.. seealso:: Functions :func:`gdaReportVarInfo`, :func:`gdaGetNames`
