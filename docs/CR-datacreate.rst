
datacreate
==============================================

Purpose
----------------

Creates a real data set.

Format
----------------
.. function:: datacreate(filename,  vnames,  col,  dtyp,  vtyp)

    :param filename: name of data file.
    :type filename: string

    :param vnames: names of variables.
    :type vnames: string or Nx1 string array

    :param col: number of variables.
    :type col: scalar

    :param dtyp: data precision, one of the following:
    :type dtyp: scalar

    .. csv-table::
        :widths: auto

        "2", "2-byte, signed integer."
        "4", "4-byte, single precision."
        "8", "8-byte, double precision."

    :param vtyp: types of variables, may contain
        one or both of the following:
    :type vtyp: scalar or Nx1 vector

    .. csv-table::
        :widths: auto

        "0", "character variable."
        "1", "numeric variable."

    :returns: fh (*scalar*), file handle.

Examples
----------------

::

    fh = datacreate("myfile.dat", "V",100,8,1);
    x = rndn(500,100);
    r = writer(fh,x);
    ret = close(fh);

This example creates a double precision data file called  myfile.dat,
which is placed in the current directory. The file contains 100 columns
with 500 observations (rows), and the columns are given the names 'V001',
'V002', ..., 'V100'.

Source
++++++

datafile.src

.. seealso:: Functions :func:`datacreatecomplex`, :func:`create`, :func:`dataopen`, :func:`writer`
