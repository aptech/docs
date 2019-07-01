
closeall
==============================================

Purpose
----------------

Closes all currently open GAUSS files.

Format
----------------
.. function:: closeall
              closeall list_of_handles

Remarks
-------

*list_of_handles* is a comma-delimited list of file handles.

:func:`closeall` with no specified list of handles will close all files. The
file handles will not be affected. The main advantage of using :func:`closeall`
is ease of use; the file handles do not have to be specified, and one
statement will close all files.

When a list of handles follows :func:`closeall`, all files are closed and the
file handles listed are set to scalar 0. This is safer than :func:`closeall`
without a list of handles because the handles are cleared.

It is important to set unused file handles to zero because both `open` and
`create` check the value that is in a file handle before they proceed with
the process of opening a file. During `open` or `create`, if the value that
is in the file handle matches that of an already open file, the process
will be aborted and a File already open error message will be given.
This gives you some protection against opening a second file with the
same handle as a currently open file. If this happened, you would no
longer be able to access the first file.

Files are not automatically closed when a program terminates. This
allows users to run a program that opens files, and then access the
files from interactive mode after the program has been run. Files are
automatically closed when GAUSS exits to the operating system or when a
program is terminated with the `end` statement. `stop` will terminate a
program but not close files.

As a rule it is good practice to make `end` the last statement in a
program, unless further access to the open files is desired from
interactive mode. You should close files as soon as you are done writing
to them to protect against data loss in the case of abnormal termination
of the program due to a power or equipment failure.

The danger in not closing files is that anything written to the files
may be lost. The disk directory will not reflect changes in the size of
a file until the file is closed and system buffers may not be flushed.

Examples
----------------

::

    new;
    cls;

    // Create 'mydata' vector
    mydata = seqa(1, 1, 3);

    // Save 'mydata' vector into 'mydata.dat' file
    call saved(mydata, "mydata.dat", "x");

    /*
    ** Open two file handles to 'mydata.dat'
    **     f1 can only be used to read data.
    **     f2 can be used to read or write data.
    */
    f1 = dataOpen("mydata.dat", "read");
    f2 = dataOpen("mydata.dat", "update");


    // Read all rows from 'mydata.dat'
    x = readr(f1, rowsf(f1));

    // Modify the data and write it back
    // to 'mydata.dat'
    x = sqrt(x);
    call writer(f2, x);

    // Close both file handles and set them equal to zero
    closeall f1,f2;

    // Check the new data file
    mydata_new = loadd("mydata.dat");

    print "mydata = " mydata;
    print "x = " x;
    print "mydata_new = " mydata_new;
    print "f1 = " f1;
    print "f2 = " f2;

After running the above code,

::

    mydata =
    	1.0000000
    	2.0000000
    	3.0000000

    x =
    	1.0000000
    	1.4142136
    	1.7320508

    mydata_new =
    	1.0000000
    	1.4142136
    	1.7320508

    f1 = 0.000000
    f2 = 0.000000

.. seealso:: Functions `close`, `open`
