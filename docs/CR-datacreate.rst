
datacreate
==============================================

Purpose
----------------

Creates a real data set.

Format
----------------
.. function:: datacreate(filename, vnames, col, dtyp, vtyp)

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

Remarks
-------

The file handle returned by datacreate is a scalar containing a positive
integer value that uniquely identifies each file. This value is assigned
by GAUSS when the create, datacreate, datacreatecomplex, open or
dataopen commands are executed. The file handle is used to reference the
file in the commands readr and writer. If datacreate fails, it returns a
-1.
If filename does not include a path, then the file is placed on the
current directory. The file is given a .dat extension if no extension is
specified.

If col is set to 0, then the number of columns in the data set is
controlled by the contents of vnames. If col is positive, then the file
will contain col columns.

If vnames contains col elements, then each column is given the name
contained in the corresponding row of vnames. If col is positive and
vnames is a string, then the columns are given the names vnames1,
vnames2, ..., vnamesN (or vnames01, vnames02, ..., vnamesN), where N =
col. The numbers appended to vnames are padded on the left with zeros to
the same length as N.

The dtyp argument allows you to specify the precision to use when
storing your data. Keep in mind the following range restrictions when
selecting a value for dtyp:

.. raw:: html

   <div align="center">

+-----------+--------+---------------------------------------------------------+
| Data Type | Digits | Range                                                   |
+-----------+--------+---------------------------------------------------------+
| integer   | 4      | -32768 < X < 32767                                      |
+-----------+--------+---------------------------------------------------------+
| single    | 6-7    | 8.43 x 10\ :sup:`-37` < \|X\| ≤ 3.37 x 10\ :sup:`+38`   |
+-----------+--------+---------------------------------------------------------+
| double    | 15-16  | 4.19 x 10\ :sup:`-307` < \|X\| < 1.67 x 10\ :sup:`+308` |
+-----------+--------+---------------------------------------------------------+


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
