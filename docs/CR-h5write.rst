
h5write
==============================================

Purpose
----------------
Write a GAUSS matrix or N-dimensional array to an HDF5 dataset.

Format
----------------
.. function:: h5write(fname, dname, x)

    :param fname: name of the HDF5 file.
    :type fname: String

    :param dname: name of the dataset in the HDF5 file.
    :type dname: String

    :param x: Matrix or N-dimensional array, the data to write to the file.
    :type x: TODO

Examples
----------------

Basic HDF5 file/dataset creation and write
++++++++++++++++++++++++++++++++++++++++++

::

    //Create a 3x2 dataset
    call h5create("testdata.h5", "/writetest", 3|2);
    				
    //Create a data matrix
    x = { 1.1 2.2,
          3.3 4.4,
          5.5 6.6 };
    
    //Write x to HDF5 dataset
    call h5write("testdata.h5", "/writetest", x);
    
    //Read data from a data set of a HDF5 file				
    y = h5read("testdata.h5", "/writetest");

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
    
    //Write x_new over first 2 rows of  HDF5 dataset
    call h5write("testdata.h5", "/writetest", x_new);
    
    //Read data again
    y_new = h5read("testdata.h5", "/writetest");

After the above code:

::

    y_new =  1000    2000 
             3000    4000
              5.5     6.6

Remarks
+++++++

To write rows of data to an HDF5 dataset in a iterative manner, see
writer.

.. seealso:: Functions :func:`h5create`, :func:`h5read`, :func:`h5writeAttribute`, :func:`dataopen`, :func:`writer`, :func:`seekr`

HDF5 h5 write
