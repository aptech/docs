
run
==============================================

Purpose
----------------

Runs a source code or compiled code program.

Format
----------------
.. function:: run filename run -r filename

    :param filename: literal or ^string,
        name of file to run.
    :type filename: TODO

    .. csv-table::
        :widths: auto

        "-r", "flag, returns control to the calling program."

Examples
----------------

run myprog.prg;
+++++++++++++++

name = "myprog.prg";
run ^name;
+++++++++++++++++++++++++++++++

x = rndn(3,3);
run -r myprog.prg;
y = inv(x);
e = x*y;
++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this case, GAUSS will execute the lines after the run command. If the 
the -r is omitted, the lines following the run command will not be executed within a program.

.. seealso:: Functions 
