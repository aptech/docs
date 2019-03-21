
datacreatecomplex
==============================================

Purpose
----------------

Creates a complex data set.

Format
----------------
.. function:: datacreatecomplex(filename, vnames, col, dtyp, vtyp)

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

    string vnames = { "random1", "random2" };
    fh = datacreatecomplex("myfilecplx.dat",vnames,2,8,1);
    x = complex(rndn(1000,2),rndn(1000,2));
    r = writer(fh,x);
    ret = close(fh);

This example creates a complex double precision data file called myfilecplx.dat,
which is placed in the current directory. The file contains 2 columns
with 1000 observations (rows), and the columns are given the names 'random1'
and 'random2'.

Source
++++++

datafile.src

.. seealso:: Functions :func:`datacreate`, :func:`create`, :func:`dataopen`, :func:`writer`
