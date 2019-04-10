
h5readAttribute
==============================================

Purpose
----------------
Read attributes from an HDF5 file into GAUSS. 

Format
----------------
.. function:: h5readAttribute(fname, dname, attr_name)

    :param fname: a name of HDF5 file.
    :type fname: string

    :param dname: a name of the HDF5 data set.
    :type dname: string

    :param attr_name: the name of attribute.
    :type attr_name: string

Remarks
-------

-  HDF5 does not support partial read or write of dataset attributes.
   The entire contents of the attribute will be read.
-  GAUSS functions that accept HDF5 datasets as a datasource, expect the
   dataset to have an attribute named :code:`"headers"`, containing the variable
   names of the dataset.


Examples
----------------

Create an HDF5 dataset and add headers
++++++++++++++++++++++++++++++++++++++

::

    //Create an HDF5 dataset with room for 100 observations of 4 variables
    call h5create("commodities.h5", "/energy", 100 | 4);
    
    //Variable names for the dataset			
    attr = "Crude Oil"$|"Gasoline"$|"Heating Oil"$|"Diesel";
    
    //Define a name of the attributes				
    attr_name = "headers";
    
    //Write attributes to a HDF5 file
    call h5writeAttribute("commodities.h5", "/energy", attr_name, attr);							
    
    //Read attributes from a HDF5 file
    attr_read = h5readAttribute("commodities.h5", "/energy", attr_name);

a: Add data and calculate descriptive statistics
++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Set seed for repeatable random data
    rndseed 54235;
    
    //Create 100x4 random normal data
    x = rndn(100, 4);
    
    //Write data to dataset created in the example above
    call h5write("commodities.h5", "/energy", x);
    
    //Calculate descriptive statistics on some of the variables
    //using an hdf5 file schema (h5://filename/dataset)
    call dstatmt("h5://commodities.h5/energy", "Gasoline + Heating Oil");

::

    ----------------------------------------------------------------------------------
    Variable          Mean   Std Dev    Variance   Minimum   Maximum   Valid   Missing
    ----------------------------------------------------------------------------------
    
    Gasoline        0.0212    1.0130      1.0261   -2.9943    2.3527     100      0 
    Heating Oil    -0.1120    0.9263      0.8580   -2.7726    3.0910     100      0

.. seealso:: Functions :func:`h5create`, :func:`h5writeAttribute`, :func:`h5read`, :func:`h5write`

