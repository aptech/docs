
use
==============================================

Purpose
----------------

Loads a compiled file at the beginning of the compilation of a source program.

Format
----------------
.. function:: use fname

    :param fname: , the name of a compiled file
        created using the compile or the saveall command.
    :type fname: literal or ^string



Remarks
-------

The use command can be used ONCE at the TOP of a program to load in a
compiled file which the rest of the program will be added to. In other
words, if xy.e had the following lines:

::

   library pgraph;
   external proc xy;
   x = seqa(0.1,0.1,100);

it could be compiled to xy.gcg. Then the following program could be run:

::

   use xy;
   xy(x, sin(x));

which would be equivalent to:

::

   new;
   library pgraph;
   x = seqa(0.1,0.1,100);
   xy(x, sin(x));

The use command can be used at the top of files that are to be compiled
with the compile command. This can greatly shorten compile time for a
set of closely related programs. For example:

::

   library pgraph;
   external proc xy,logx,logy,loglog,hist;
   saveall pgraph;

This would create a file called pgraph.gcg containing all the
procedures, strings and matrices needed to run PQG programs. Other
programs could be compiled very quickly with the following statement at
the top of each:

::

   use pgraph;

or the same statement could be executed once, for instance from the
command prompt, to instantly load all the procedures for PQG.

When the compiled file is loaded with use, all previous symbols and
procedures are deleted before the program is loaded. It is therefore
unnecessary to execute a new before use'ing a compiled file.

use can appear only ONCE at the TOP of a program.

.. seealso:: Functions `compile`, `run`, `saveall`
