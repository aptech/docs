
close
==============================================

Purpose
----------------
Closes a **GAUSS** file.

Format
----------------
.. function:: close(handle)

    :param handle: the file handle given to the file when it was opened with the `open`,
        `create`, or :func:`fopen` command.
    :type handle: scalar

    :returns: y (*scalar*), 0 if successful, -1 if unsuccessful.

Remarks
-------

*handle* is the scalar file handle created when the file was opened. It
will contain an integer which can be used to refer to the file.

`close` will close the file specified by *handle*, and will return a 0 if
successful and a -1 if not successful. The handle itself is not affected
by `close` unless the return value of `close` is assigned to it.

If *f1* is a file handle and it contains the value 7, then after:

::

   call close(f1);

the file will be closed but *f1* will still have the value 7. The best
procedure is to do the following:

::

   f1 = close(f1);

This will set *f1* to 0 upon a successful close.

It is important to set unused file handles to zero because both `open` and
`create` check the value that is in a file handle before they proceed with
the process of opening a file. During `open` or `create`, if the value that
is in the file handle matches that of an already open file, the process
will be aborted and a File already open error message will be given.
This gives you some protection against opening a second file with the
same handle as a currently open file. If this happened, you would no
longer be able to access the first file.

An advantage of the `close` function is that it returns a result which can
be tested to see if there were problems in closing a file. The most
common reason for having a problem in closing a file is that the disk on
which the file is located is no longer in the disk drive--or the handle
was invalid. In both of these cases, `close` will return a -1.

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

    // Create 'mydata' matrix
    mydata = seqa(1, 1, 3);

    // Using saved function to save mydata matrix into 'mydata.dat' file
    saved(mydata, "mydata.dat", "x");

    // Set a random seed
    rndseed 855;

    // Open 'mydata.dat' file
    open f1 = mydata for append;

    // Create an appended data set 'x'
    x = rndu(3, 1);

    y = writer(f1, x);
    f1 = close(f1);

    data_new = loadd("mydata.dat");

    print "mydata = " mydata;
    print "x = " x;
    print "data_new = " data_new;

After running above code,

::

    1.0000000 
    mydata =
    	1.0000000
    	2.0000000
    	3.0000000
    x =
    	0.33589398
    	0.62804541
    	0.017829664
    data_new =
    	1.0000000
    	2.0000000
    	3.0000000
    	0.33589398
    	0.62804541
    	0.017829664

The first 1 means the "mydata.dat" file is closed.

.. seealso:: Functions :func:`closeall`
