
output
==============================================

Purpose
----------------

This command makes it possible to direct the output of print statements to two different places simultaneously. One output device is always the window or standard output. The other can
be selected by the user to be any disk file or other suitable output device such as a printer.

Format
----------------
.. function:: filename 
			  filename [on|off|reset]

    :param filename: 
        
        The file=filename subcommand selects the file or device to which
        output is to be sent.If the name of the file is to be taken from a string variable, the
        name of the string must be preceded by the ^ (caret) operator.The default file name is output.out.
    :type filename: literal or ^string

    :param on, off, reset: mode flag:
    :type on, off, reset: literal

    .. csv-table::
        :widths: auto

        "on", "opens the auxiliary output file ordevice and causes the results of all print statements to be sent tothat file or device. If the file already exists, it will be openedfor appending. If the file does not already exist, it will becreated."
        "off", "closes the auxiliary output file and turns off theauxiliary output."
        "reset", "similar to the on subcommand, except that it alwayscreates a new file. If the file already exists, it will be destroyedand a new file by that name will be created. If it does not exist, itwill be created."

Examples
----------------

::

    output file = out1.out on;

This statement will open the file out1.out and will cause the
results of all subsequent print statements to be sent to that
file. If out1.out already exists, the new output will be appended.

::

    output file = out2.out;
    output on;

This is equivalent to the previous example.

::

    output reset;

This statement will create a new output file using
 the current filename. If the file already exists,
 any data in it will be lost.

::

    output file = mydata.asc reset;
    screen off;
    format /m1/rz 1,8;
    open fp = mydata;
    
    do until eof(fp);
       print readr(fp,200);;
    endo;
    
    fp = close(fp);
    end;

The program above will write the contents of the
GAUSS file mydata.dat into an ASCII file called
mydata.asc. If there had been an existing file by
the name of mydata.asc, it would have been
overwritten.
The /m1 parameter in the format statement in
combination with the ;; at the end of the print
statement will cause one carriage return/line feed
pair to be written at the beginning of each row of
the output file. There will not be an extra line
feed added at the end of each 200 row block.
The end statement above will automatically perform
output off and screen on.

.. seealso:: Functions :func:`outwidth`, :func:`screen`, :func:`end`, :func:`new`
