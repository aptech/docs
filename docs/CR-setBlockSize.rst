
setBlockSize
==============================================

Purpose
----------------

Set maximum size of memory block to load.

Format
----------------
.. function:: setBlockSize(block_size)

    :param block_size: 
    :type block_size: scalar or string

    .. csv-table::
        :widths: auto

        "scalar, fixed number of rows to use"
        "string, string specifier for chunk size. options can be:					"10%" [10% of total system RAM] "500K" [500 Kilobytes] "10M" [10 Megabytes]"100M" [100 Megabytes]"1G"  [1 Gigabyte]"

Examples
----------------

::

    //Set maximum ammount of data to load at a time to be 10 Kilobytes
    setBlockSize("10K");
    
    //Estimate model parameters, never loading more
    //than 10 KB of 'mydata.dat' at a time
    call olsmt("mydata.dat", "Y ~ X1 + X2");

Remarks
-------

setBlockSize controls the maximum number of rows to read at a time for
functions which can process datasets in chunks, such as olsmt and
dstatmt.

setBlockSize is not threadsafe. To control the size of data blocks
loaded in code which is threaded with threadBegin/threadStat or
threadFor, you must call setBlockSize before the threads are created.

