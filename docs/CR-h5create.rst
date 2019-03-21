
h5create
==============================================

Purpose
----------------
Creates an HDF5 data file, or adds a new dataset to an existing HDF5 file.

Format
----------------
.. function:: h5create(fname, dname, dims) 
			  h5create(fname, dname, dims, datatype) 
			  h5create(fname, dname, dims, datatype, chunk_size)

    :param fname: name of the HDF5 file. The file extension, .h5 recommended, but not required.
    :type fname: String

    :param dname: a name of the data set in HDF5 file. e.g. "/mydata".
    :type dname: String

    :param dims: where N is the number of dimensions of the dataset, the size of each of the dimensions of the dataset.
    :type dims: Nx1 matrix

    :param datatype: data type. Valid options include:
        "double" "float" "int64" "int32" "uint64" "uint32"Default is "double".
    :type datatype: String

    :param chunk_size: with the same dimensions as the data set, specifying the size of the chunks of data that will be created in the file.
    :type chunk_size: Matrix or array

Remarks
-------

-  HDF5 files can hold more than one dataset. They are referenced in the
   same manner as a Linux or Mac file system. The base or root node is
   '/'. All datasets are relative to this root node.
-  If a dataset name contains multiple intermediate groups, for example:

   ::

      "/surveys/household/Washington"

   and the intermediate groups, ``surveys`` and ``household`` in the
   above string, do not yet exist, h5create will create them.

-  By default, HDF5 datasets may not change size. To make one of the
   dimensions expandable, set it to \__INFP.
-  All columns of an HDF5 dataset must be of the same data type.
   However, multiple datasets with different data types may be created
   in a single HDF5 file.
-  Information about a dataset, called an attribute, may be attached to
   a dataset in an HDF5 file with the function h5writeAttribute.
-  Chunk size must be specified when users create a dataset with more
   than 2 dimensions and one of those dimensions is unlimited (\__INFP).


Examples
----------------

Create a fixed size 2-dimensional dataset
+++++++++++++++++++++++++++++++++++++++++

::

    // Define a name of a  HDF5 file				
    fname = "testdata.h5";
    
    // Define a data set name under the HDF5 file					
    dname = "/mydata";
    
    // Define the size of the data set, 100 rows and 5 columns 	
    r = 100;
    c = 5;	
    
    // Create a data set under the HDF5 file							
    call h5create(fname, dname, r|c);
    
    // Fill dataset with random normal data
    x = rndn(100, 5);
    h5write(fname, dname, x);

Create a 2-dimensional dataset with 5 columns and a flexible number of rows
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define a size of flexible rows and 5 columns 
    dims  = __INFP|5;	
    
    // Create a data set 							
    call h5create("expandable_data.h5", "/data", dims);

Create a 3-Dimensional dataset and one intermediate group
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define a new data set name, including one intermediate group
    dname = "/household/Washington";
    
    // Define a 3-dimensional dataset, containing 3 matrices with
    // 8 columns and an expandable number of rows				
    dims = 3|__INFP|8;	
    
    // Store the data in chunks of 1000x8 elements
    chunk_size = { 1, 1000, 8 };
    
    // Store data as 4 byte floating point (about 8 digits of precision)
    dtype = "float";
    
    // Create the data set 
    call h5create("surveys.h5", dname, dims, dtype, chunk_size);
    
    // Create another data set of the same type inside the same file
    call h5create("surveys.h5", "/household/Oregon", dims, dtype, chunk_size);

.. seealso:: Functions :func:`h5read`, :func:`h5write`, :func:`open`, :func:`create`, :func:`writer`, :func:`seekr`, :func:`eof`

HDF5 create new h5
