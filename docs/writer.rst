
writer
==============================================

Purpose
----------------
Writes a matrix to a GAUSS dataset.

Format
----------------
.. function:: ret = writer(fh, x)

    :param fh: handle of the file that data is to be written to
    :type fh: scalar

    :param x: data
    :type x: NxK matrix

    :return ret: specifying the number of rows of data actually written to the dataset.

    :rtype ret: scalar

Examples
----------------

Create and write to dataset
+++++++++++++++++++++++++++++++++

::

    x = { 1 2 3,
          4 5 6 };

    var_names = "alpha" $| "beta" $| "gamma";
    nvars = rows(var_names);

    // Create dataset and get file handle
    fh = dataCreate("test.dat", var_names, nvars, 8, 1);

    // Write data in 'x' to test.dat
    ret = writer(fh, x);

    close(fh);


Create and iteratively write to dataset
++++++++++++++++++++++++++++++++++++++++++


::

    new;

    nvars = 10;

    // Create dataset and get file handle
    fp = dataCreate("data.dat", "X", nvars, 8, 1);
    
    // Check to confirm that data file was created
    if fp == -1;
       errorlog "Can't create output file";
       end;
    endif;
    
    for i(1, 10, 1);
       y = rndn(100,10);
       ret = writer(fp,y);
    
       // Check to see if all data was written
       if ret != rows(y);
         errorlog "Write failed";
         fp = close(fp);
         end;
       endif;
    
    endfor;
    
    fp = close(fp);

In this example, a 1000x10 dataset of Normal random numbers is written to a dataset called :file:`data.dat`. 
The variable names are ``X01 - X10``.

Remarks
-------
* :func:`saved` provides a more convenient method to create a dataset.

* The file must have been opened with :func:`dataCreate`, or :func:`dataOpen` for update or append. The keywords `create` and `open` are still supported as well.

* The data in *x* will be written to the dataset whose handle is *fh*
  starting at the current pointer position in the file. The pointer
  position in the file will be updated, so the next call to :func:`writer` will
  put the next block of data after the first block. (See `open` and `create`
  for the initial pointer positions in the file for reading and writing.)

* *x* must have the same number of columns as the dataset. :func:`colsf` returns
  the number of columns in a dataset.

* If the dataset is not double precision, the data will be rounded as it is written out.

* If the data contain character elements, the file must be double precision or the character information will be lost.

* If the file being written to is the 2-byte integer data type, then
  missing values will be written out as -32768. These will not
  automatically be converted to missings on input. They can be converted
  with the :func:`miss` function:
  ::

    x = miss(x,-32768);

* Trying to write complex data to a dataset that was originally created
  to store real data will cause a program to abort with an error message.
  (See `create` for details on creating a complex dataset.)


.. seealso:: Functions `open`, `close`, `create`, :func:`readr`, :func:`saved`, :func:`seekr`

