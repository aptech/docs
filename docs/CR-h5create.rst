
h5create
==============================================

Purpose
----------------
Creates an HDF5 data file, or adds a new dataset to an existing HDF5 file.

Format
----------------
.. function:: ret = h5create(fname, dname, dims[, datatype[, chunk_size]])

    :param fname: name of the HDF5 file. The file extension, ``.h5``, is recommended, but not required.
    :type fname: string

    :param dname: a name of the dataset in HDF5 file. e.g. :code:`"/mydata"`.
    :type dname: string

    :param dims: where :math:`N` is the number of dimensions of the dataset, the size of each of the dimensions of the dataset.
    :type dims: Nx1 matrix

    :param datatype: data type. Valid options include:

        - :code:`"double"`
        - :code:`"float"`
        - :code:`"int64"`
        - :code:`"int32"`
        - :code:`"uint64"`
        - :code:`"uint32"`

        Default is :code:`"double"`.

    :type datatype: string

    :param chunk_size: with the same dimensions as the dataset, specifying the size of the chunks of data that will be created in the file.
    :type chunk_size: matrix or array

    :returns: **retcode** (*scalar*) - 0 if successful, non-zero otherwise.

Remarks
-------

-  HDF5 files can hold more than one dataset. They are referenced in the
   same manner as a Linux or macOS file system. The base or root node is
   ``/``. All datasets are relative to this root node.
-  If a dataset name contains multiple intermediate groups, for example:

   ::

      "/surveys/household/Washington"

   and the intermediate groups, ``surveys`` and ``household`` in the
   above string, do not yet exist, :func:`h5create` will create them.

-  By default, HDF5 datasets may not change size. To make one of the
   dimensions expandable, set it to `__INFP`.
-  All columns of an HDF5 dataset must be of the same data type.
   However, multiple datasets with different data types may be created
   in a single HDF5 file.
-  Information about a dataset, called an attribute, may be attached to
   a dataset in an HDF5 file with the function :func:`h5writeAttribute`.
-  Chunk size must be specified when users create a dataset with more
   than 2 dimensions and one of those dimensions is unlimited (`__INFP`).


Examples
----------------

Create a fixed size 2-dimensional dataset
+++++++++++++++++++++++++++++++++++++++++

::

    // Define a name of a  HDF5 file
    fname = "testdata.h5";

    // Define a dataset name under the HDF5 file
    dname = "/mydata";

    // Define the size of the dataset, 100 rows and 5 columns
    r = 100;
    c = 5;
    dims = r|c;

    // Create a dataset under the HDF5 file
    call h5create(fname, dname, dims);

    // Fill dataset with random normal data
    x = rndn(100, 5);
    h5write(fname, dname, x);

Create a 2-dimensional dataset with 5 columns and a flexible number of rows
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define filename
    fname = "expandable_data.h5";

    // Define dataset in HDF5 file
    dname = "/data";

    // Define a size of flexible rows and 5 columns
    r = __INFP;
    c = 5;
    dims  = r|c;

    // Create a dataset
    call h5create(fname, dname, dims);

Create a 3-Dimensional dataset and one intermediate group
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define file name
    fname = "surveys.h5";

    // Define a new dataset name, including one intermediate group
    dname = "/household/Washington";

    /*
    ** Define a 3-dimensional dataset, containing 3 matrices with
    ** 8 columns and an expandable number of rows
    */
    num_matrices = 3;
    r = __INFP;
    c = 8;
    dims = num_matrices|r|c;

    // Store the data in chunks of 1000x8 elements
    chunk_size = { 1, 1000, 8 };

    // Store data as 4 byte floating point (about 8 digits of precision)
    dtype = "float";

    // Create the dataset
    call h5create(fname, dname, dims, dtype, chunk_size);

    /*
    ** Define another dataset of same type
    ** inside the same file
    */
    dname_new =  "/household/Oregon";

    // Create new dataset
    call h5create(fname, dname_new, dims, dtype, chunk_size);

.. seealso:: Functions :func:`h5read`, :func:`h5write`, `open`, `create`, :func:`writer`, :func:`seekr`, :func:`eof`
