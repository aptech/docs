
h5open
==============================================

Purpose
----------------
Open an HDF5 dataset and returns a file handle.

Format
----------------
.. function:: h5open(fname, dname, mode)

    :param fname: a name of HDF5 file to open.
    :type fname: string

    :param dname: a name of a dataset (or group) in HDF5 file. e.g. :code:`"/mydata"`.
    :type dname: string

    :param mode: the mode with which to open the file. Valid options include:

        - :code:`"open"`: open file for read, positioned at the first row.
        - :code:`"update"`: open file for write, positioned at the first row.
        - :code:`"append"`: open file for write, positioned at the end of the file.a

    :type mode: string

    :returns: **fh** (*scalar*) - file handle for use with :func:`readr`, or :func:`writer`.

Remarks
-------

-  The file handle must be closed with either the :func:`close` function or
   :func:`closeall` when you are finished using it.
-  To read or write data to a file opened with :func:`h5open`, use :func:`readr`, and
   :func:`writer`.
-  To read and write data to an HDF5 dataset without opening a file
   handle, use :func:`h5read` and :func:`h5write`.
-  The function :func:`dataopen` can open file handles for reading and writing
   to HDF5 datasets and other file types.


Examples
----------------

Create and write to an HDF5 dataset
+++++++++++++++++++++++++++++++++++

::

    rndseed 2344;

    // Create a 4 row by 3 column  HDF5 dataset
    call h5create("testdata.h5", "/mydata", 4 | 3);

    // Create a 2x3 matrix
    x = { 1.1 2.2 3.3,
          4.4 5.5 6.6 };

    // Open a file handle
    fh = h5open("testdata.h5", "/mydata", "update");

    // Write the data in 'x' to the the first two rows
    call writer(fh, x);

    // Create a 2x3 matrix
    y = { 10 20 30,
          40 50 60 };

    // Write the data in 'y' to the final two rows
    call writer(fh, y);

    // Close the file handle
    close(fh);

Read data written in Example 1
++++++++++++++++++++++++++++++

::

    // Open a file handle
    fh = h5open("testdata.h5", "/mydata", "read");

    // Read the first row
    a  = readr(fh, 1);

    // Read the second, third, and fourth rows
    b  = readr(fh, 3);

    // Close the file
    call close(fh);

After the code above

::

    a =  1.10  2.20  3.30

    b =   4.4   5.5   6.6
         10.0  20.0  30.0
         40.0  50.0  60.0

.. seealso:: Functions :func:`h5create`, :func:`h5read`, :func:`h5write`, `open`, :func:`dataopen`, :func:`readr`, :func:`seekr`
