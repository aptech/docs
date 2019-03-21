
gdaIsCplx
==============================================

Purpose
----------------

Checks to see if a variable in a GAUSS Data Archive is complex.

Format
----------------
.. function:: gdaIsCplx(filename, varname)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :returns: y (*scalar*), 1 if variable is complex; 0 if real.

Examples
----------------

::

    cplx = gdaIsCplx("myfile.gda","x1");

