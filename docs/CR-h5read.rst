
h5read
==============================================

Purpose
----------------
Reads data from an HDF5 dataset into a GAUSS matrix.

Format
----------------
.. function:: h5read(fname, dname[, dims[, offset]])

    :param fname: a name of the HDF5 file.
    :type fname: string

    :param dname: a name of the dataset in HDF5 file. e.g. :code:`"/mydata"`.
    :type dname: string

    :param dims: where *N* is the number of dimensions in the dataset, the dimensions of data to read.
    :type dims: Nx1 vector

    :param offset: where *N* is the number of dimensions in the dataset, the data to skip.
    :type offset: Nx1 vector

    :returns: **y** (*Matrix or array*) - the data requested from the file.

Examples
----------------

Basic write then read entire contents of an HDF5 file
+++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define a name of a HDF5 file
    fname = "testdata.h5";

    // Define a name of a dataset
    dname = "/mydata";

    // Define a size of 4 rows and 3 columns
    r = 3;
    c = 2;
    dims  = r|c;

    // Create a 3x2 fixed dimension dataset in a HDF5 file
    call h5create(fname, dname, dims);

    // Create a 3x2 matrix
    x = { 9 4,
          2 1,
          0 7 };

    // Write x to dataset
    call h5write(fname, dname, x);

    // Read all contents from dataset
    y = h5read(fname, dname);

After the code above:

::

    x = 9  4    y = 9  4
        2  1        2  1
        0  7        0  7

Read HDF5 first two rows and first two columns
++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define a name of a HDF5 file
    fname = "testdata.h5";

    // Define a name of a dataset
    dname = "/mydata";

    // Size of data to read
    dims = 2|2;

    // Read data from file created in Example 1, above
    y2 = h5read(fname, dname, dims);

After the code above:

::

    y2 =    9 4
    	      2 1

Read HDF5 first two rows and first two columns
++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define a name of a HDF5 file
    fname = "testdata.h5";

    // Define a name of a dataset
    dname = "/mydata";

    // Size of data to read
    dims = 2|2;

    // Dimensions to skip: 1 row and 0 columns
    offset = 1|0;

    // Read data from file created in Example 1, above
    y3 = h5read(fname, dname, dims, offset);

After the code above:

::

    y3 =    2 1
            0 7

Read HDF5 file with offset at more than one dimension
+++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Define a name of a HDF5 file
    fname = "testdata.h5";

    // Define a new dataset name
    dname = "/highdimension";

    // Create 3 dimensions, with __INFP indicating expandable rows
    dims = 3 | __INFP  | 4;

    // Define data type
    datatype = "double";

    // Define chunk size since the second dimension is infinite
    chunk_size = 1|128|4;

    // Create "highdimension" dataset, inside file created in Example 1 (above)
    call h5create(fname, dname, dims, datatype, chunk_size);

    // Set seed for repeatable random numbers
    rndseed 7672342;

    // Create random normal data array, with dimensions 3x10x4
    x = areshape(rndn(3 * 10 * 4, 1), 3 | 10 | 4);

    // Write it into dataset
    call h5write(fname, dname, x);

    // Skip first two rows and first column of each
    // of the 3 matrices in the 3x10x4 array
    offset = 0|2|1;

    // Define the read size after removing offset
    dims_read = 2|2|2;

    // Run h5read function
    y4 = h5read(fname, dname, dims_read, offset);

After the code above, we see that *y4* is a 2x2x2 (number of dimensions to read *dims_read*) array, containing the contents of the *x*, after skipping the dimensions :math:`{ 0, 2, 1 }` specified in *offset*:

::

    y4  = Plane [1,.,.]

         -0.61557786      -0.76592868
         -0.30976522       0.11296623

          Plane [2,.,.]

         -0.23144975       -1.1369840
         -0.89682110        1.6684102


    x =   Plane [1,.,.]

          -1.2045242       -1.0675179      -0.74403139      -0.72860218
          0.20337032      -0.48451306    -0.0039387096       0.46361645
         -0.57448560      -0.61557786      -0.76592868     -0.032267807
         -0.88033211      -0.30976522       0.11296623        1.2724183
          -1.4409872      -0.90939666       0.22487451      -0.37188053
          -1.5478724      -0.43944280      0.010049938        1.0196427
           1.3352024        1.0734150      -0.98373668      -0.57590137
         -0.32428680       0.53099143      -0.71162764       -2.1188409
         -0.22060808     -0.024172215       0.64942867      -0.51276843
          0.12600180      -0.65155519       -2.2815720        1.4961735

         Plane [2,.,.]

         -0.78337697      -0.52759501       -1.2322159      -0.31936828
         -0.47552440       -1.0708763       0.43111378        1.5146598
          0.54119533      -0.23144975       -1.1369840      -0.11052318
          0.47963176      -0.89682110        1.6684102      -0.43704128
         -0.27511827      -0.65207535      -0.17394561      -0.84737201
         -0.14595989     -0.028056845       0.50018732      -0.76191566
         -0.98846912        1.4389099        1.3716329       -1.3419693
         -0.29630831       -1.2029618       -1.4958204       -2.0829113
         -0.56764971      -0.53397186      -0.95002213      -0.10182348
          -1.6156998       -1.5120152      0.013456774     -0.037790884

         Plane [3,.,.]

          0.42346079      -0.61879151      0.062894922       0.43245351
         0.092322769       0.68876937      -0.61677358        2.8805431
          0.33204968        2.1878476       -1.1113500      -0.38579652
          0.35943828       0.32172778      -0.25074937      -0.34662609
         -0.95053031     0.0010335034      -0.12838005       -1.2333248
          0.59991891       0.73834232      -0.23521782      -0.63566653
          -1.5290045      -0.36202638       0.69077565        1.0898312
          0.71036599      0.086441099      -0.40250335       0.58997554
         -0.55612014      0.084524826       0.60194547       0.26031576
          0.49760949      0.070206385       0.65894867       0.73385573

.. seealso:: Functions :func:`h5create`, :func:`h5write`, `open`, `create`, :func:`writer`, :func:`seekr`, :func:`eof`
