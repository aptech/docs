
h5writeAttribute
==============================================

Purpose
----------------
Writes a GAUSS matrix, N-dimensional array or string array as an attribute of an HDF5 dataset.

Format
----------------
.. function:: h5writeAttribute(fname, dname, attr_name, attr)

    :param fname: a name of the HDF5 file.
    :type fname: string

    :param dname: a name of the dataset in the HDF5 file.
    :type dname: string

    :param attr_name: the name of attribute to write.
    :type attr_name: string

    :param attr: N-dimensional array or string array, the contents of the attribute.
    :type attr: matrix

    :returns: **retcode** (*scalar*) - 0 if successful, non-zero otherwise.

-------

-  Attributes in an HDF5 file cannot be read or written partially. The
   entire contents of the attribute must be read or written in one call.
-  GAUSS functions that take in an HDF5 dataset as a data source (see
   :func:`dstatmt`, :func:`glm`), expect the dataset to have an attribute called
   :code:`"headers"`, containing the variable names of the dataset.


Examples
----------------

Create an HDF5 dataset and add headers
++++++++++++++++++++++++++++++++++++++

::

    // Define file name
    fname = "commodities.h5";

    // Name of dataset in HDf5 file
    dname = "/energy"
    // Create an HDF5 dataset with room for 100 observations of 4 variables
    call h5create(fname, dname, 100 | 4);

    // Variable names for the dataset
    attr = "Crude Oil"$|"Gasoline"$|"Heating Oil"$|"Diesel";

    // Define a name of the attributes
    attr_name = "headers";

    // Write attributes to a HDF5 file
    call h5writeAttribute(fname, dname, attr_name, attr);

    // Read attributes from a HDF5 file
    attr_read = h5readAttribute(fname, dname, attr_name);

Add data and calculate descriptive statistics
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Set seed for repeatable random data
    rndseed 54235;

    // Create 100x4 random normal data
    x = rndn(100, 4);

    // Write data to dataset created in the example above
    call h5write(fname, dname, x);

    /*
    ** Calculate descriptive statistics on some of the variables
    ** using an hdf5 file schema (h5://filename/dataset)
    */
    call dstatmt("h5://commodities.h5/energy", "Gasoline + Heating Oil");

::

    ----------------------------------------------------------------------------------
    Variable          Mean   Std Dev    Variance   Minimum   Maximum   Valid   Missing
    ----------------------------------------------------------------------------------

    Gasoline        0.0212    1.0130      1.0261   -2.9943    2.3527     100      0
    Heating Oil    -0.1120    0.9263      0.8580   -2.7726    3.0910     100      0

.. seealso:: Functions :func:`h5readAttribute`, :func:`h5read`, :func:`h5write`, :func:`h5create`, :func:`h5write`
