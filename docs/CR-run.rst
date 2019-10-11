
run
==============================================

Purpose
----------------

Runs a source code or compiled code program.

.. _run:
.. index:: run

Format
----------------

::

    run filename;
    run -r filename;

**Parameters**

:filename: (*literal or ^string*) name of file to run.

    ========= ==================================
    ``-r``    flag, returns control to the calling program.
    ========= ==================================

Examples
----------------

Example 1
+++++++++

::

    run myprog.prg;

Example 2
+++++++++

::

    name = "myprog.prg";
    run ^name;

Example 3
+++++++++

::

    x = rndn(3,3);
    run -r myprog.prg;
    y = inv(x);
    e = x*y;

In this case, GAUSS will execute the lines after the run command. If the 
the ``-r`` is omitted, the lines following the run command will not be executed within a program.

Remarks
-------

The *filename* can be any legal file name. Filename extensions can be
whatever you want, except for the compiled file extension, :file:`.gcg`.
Pathnames are okay. If the name is to be taken from a string variable,
then the name of the string variable must be preceded by the ``^`` (caret)
operator.

The `run` statement can be used both from the command line and within a
program. If used in a program, once control is given to another program
through the `run` statement, there is no return to the original program
unless the flag ``-r`` is used.

If you specify a filename without an extension, GAUSS will first look
for a compiled code program (i.e., a :file:`.gcg` file) by that name, then a
source code program by that name. For example, if you enter

::

   run dog;

GAUSS will first look for the compiled code file :file:`dog.gcg`, and run that
if it finds it. If GAUSS cannot find :file:`dog.gcg`, it will then look for the
source code file *dog* with no extension.

If a path is specified for the file, then no additional searching will
be attempted if the file is not found.

If a path is not specified, the current directory will be searched
first, then each directory listed in *src_path*. The first instance found
is run. *src_path* is defined in gauss.cfg.

::

    // No additional search will be made if the file is not found.
    run /gauss/myprog.prg; 

::

    // The directories listed in src_path will be searched for myprog.prg if the file is not found in the current directory.
    run myprog.prg; 

Programs can also be run by typing the filename on the OS command line
when starting GAUSS.


.. seealso:: `#include`
