
saveall
==============================================

Purpose
----------------
Saves the current state of the machine to a compiled file. All procedures, global matrices and strings will be saved.

Format
----------------
.. function:: saveall fname

    :param fname: , the path and
        filename of the compiled file to be created.
    :type fname: literal or ^string



Remarks
-------

The file extension will be .gcg.

A file will be created containing all your matrices, strings, and
procedures. No main code segment will be saved. This just means it will
be a .gcg file with no main program code (see compile). The rest of the
contents of memory will be saved, including all global matrices,
strings, functions and procedures. Local variables are not saved. This
can be used inside a program to take a snapshot of the state of your
global variables and procedures. To reload the compiled image, use run
or use.

::

   library pgraph;
   external proc xy,logx,logy,loglog,hist;
   saveall pgraph;

This would create a file called pgraph.gcg, containing all the
procedures, strings and matrices needed to run **Publication Quality
Graphics** programs. Other programs could be compiled very quickly with
the following statement at the top of each:

::

   use pgraph;

.. seealso:: Functions `compile`, `run`, `use`

