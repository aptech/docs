
h5write
==============================================

Purpose
----------------
Write a GAUSS matrix or N-dimensional array to an HDF5 dataset.

Format
----------------
.. function:: h5write(fname, dname, x)

    :param fname: name of the HDF5 file.
    :type fname: string

    :param dname: name of the dataset in the HDF5 file.
    :type dname: string

    :param x: the data to write to the file.
    :type x: Matrix or N-dimensional array

    :returns: **retcode** (*scalar*) - 0 if successful, non-zero otherwise.

Examples
----------------

Basic HDF5 file/dataset creation and write
++++++++++++++++++++++++++++++++++++++++++

::

    // Define file name
    fname =  "testdata.h5";

    // Define dataset in HDF5 file
    dname = "/writetest";

    // Define the size of the dataset, 3 rows and 2 columns
    r = 3;
    c = 2;
    dims = r|c;

    // Create a 3x2 dataset
    call h5create(fname, dname, dims);

    // Create a data matrix
    x = { 1.1 2.2,
          3.3 4.4,
          5.5 6.6 };

    // Write x to HDF5 dataset
    call h5write(fname, dname, x);

    // Read data from a dataset of a HDF5 file
    y = h5read(fname, dname);

After the code above:

::

    y =  1.1  2.2
         3.3  4.4
         5.5  6.6

Write over first two rows of dataset
++++++++++++++++++++++++++++++++++++

::

    x_new = { 1000 2000,
              3000 4000 };

    // Write x_new over first 2 rows of  HDF5 dataset
    call h5write(fname, dname, x_new);

    // Read data again
    y_new = h5read(fname, dname);

After the above code:

::

    y_new =  1000    2000
             3000    4000
              5.5     6.6

Remarks
-------

To write rows of data to an HDF5 dataset in an iterative manner, see :func:`writer`.

.. seealso:: Functions :func:`h5create`, :func:`h5read`, :func:`h5writeAttribute`, :func:`dataopen`, :func:`writer`, :func:`seekr`
