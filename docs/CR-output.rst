
output
==============================================

Purpose
----------------

This command makes it possible to direct the output of print statements to two different places simultaneously. 
One output device is always the window or standard output. The other can be selected by the user to be any disk 
file or other suitable output device such as a printer.

.. _output:
.. index:: output

Format
----------------

::

    output file=filename;
    output file=filename [on|off|reset];

**Parameters:**

:filename: (*literal or ^string*) 
           
    The ``file=filename`` subcommand selects the file or device to which output is to be sent.
    
    If the name of the file is to be taken from a string variable, the name of the string must 
    be preceded by the ``^`` (caret) operator..
    
    The default file name is *output.out*.

:on, off, reset: (*literal*) mode flag:

    .. csv-table::
        :widths: auto

        "on", "opens the auxiliary output file or device and causes the results of all print statements to be sent to that file or device. If the file already exists, it will be opened for appending. If the file does not already exist, it will be created."
        "off", "closes the auxiliary output file and turns off the auxiliary output."
        "reset", "similar to the *on* subcommand, except that it always creates a new file. If the file already exists, it will be destroyed and a new file by that name will be created. If it does not exist, it will be created."

Remarks
-------

After you have written to an output file you have to close the file
before you can print it or edit it with the GAUSS editor. Use

::

   output off;

The selection of the auxiliary output file or device remains in effect
until a new selection is made, or until you get out of GAUSS. Thus, if a
file is named as the output device in one program, it will remain the
output device in subsequent programs until a new ``file=filename``
subcommand is encountered.

The command

::

   output file=filename;

will select the file or device but will not open it. A subsequent ``output on`` 
or ``output reset`` will open it and turn on the auxiliary output.

The command ``output off`` will close the file and turn off the auxiliary
output. The filename will remain the same. A subsequent ``output on`` will
cause the file to be opened again for appending. A subsequent ``output reset`` 
will cause the existing file to be destroyed and then recreated
and will turn on the auxiliary output.

The command ``output`` by itself will cause the name and status (i.e., open
or closed) of the current auxiliary output file to be printed to the
window.

The output to the console can be turned off and on using the ``screen off``
and ``screen on`` commands. Output to the auxiliary file or device can be
turned off or on using the ``output off`` or ``output on`` command. The defaults
are ``screen on`` and ``output off``.

The auxiliary file or device can be closed by an explicit ``output off``
statement, by an `end` statement, or by an interactive `new` statement.
However, a `new` statement at the beginning of a program will not close
the file. This allows programs with `new` statements in them to be run
without reopening the auxiliary output file.

If a program sends data to a disk file, it will execute much faster if
the window is off.

The :func:`outwidth` command will set the line width of the output file. The
default is 80.


Examples
----------------

::

    output file = out1.out on;

This statement will open the file *out1.out* and will cause the
results of all subsequent `print` statements to be sent to that
file. If *out1.out* already exists, the new output will be appended.

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
GAUSS file *mydata.dat* into an ASCII file called
*mydata.asc*. If there had been an existing file by
the name of *mydata.asc*, it would have been overwritten.

The ``/m1`` parameter in the `format` statement in
combination with the ``;;`` at the end of the `print`
statement will cause one carriage return/line feed
pair to be written at the beginning of each row of
the output file. There will not be an extra line
feed added at the end of each 200 row block.

The `end` statement above will automatically perform
``output off`` and ``screen on``.

.. seealso:: Functions :func:`outwidth`, `screen`, `end`, `new`

