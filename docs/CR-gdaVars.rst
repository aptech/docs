
gdaVars
==============================================

Purpose
----------------

Gets the number of variables in a GAUSS Data Archive.

Format
----------------
.. function:: gdaVars(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: nvars (*scalar*), the number of variables in  filename.

Examples
----------------

::

    nvars = gdaVars("myfile.gda");

Source
++++++

gdafns.src

.. seealso:: Functions :func:`gdaReportVarInfo`, :func:`gdaGetNames`
