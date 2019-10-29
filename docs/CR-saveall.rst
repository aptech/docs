
saveall
==============================================

Purpose
----------------
Saves the current state of the machine to a compiled file. All procedures, global matrices and strings will be saved.

.. _saveall:
.. index:: saveall

Format
----------------

::

    saveall fname;

**Parameters**

:fname: (*literal or ^string*) the path and filename of the compiled file to be created.

Remarks
-------

The file extension will be :file:`.gcg`.

A file will be created containing all your matrices, strings, and
procedures. No main code segment will be saved. This just means it will
be a :file:`.gcg` file with no main program code (see `compile`). The rest of the
contents of memory will be saved, including all global matrices,
strings, functions and procedures. Local variables are not saved. This
can be used inside a program to take a snapshot of the state of your
global variables and procedures. To reload the compiled image, use `run`
or `use`.

::

   library pgraph;
   external proc xy,logx,logy,loglog,hist;
   saveall pgraph;

This would create a file called :file:`pgraph.gcg`, containing all the
procedures, strings and matrices needed to run **Publication Quality
Graphics** programs. Other programs could be compiled very quickly with
the following statement at the top of each:

::

   use pgraph;

.. seealso:: Functions `compile`, `run`, `use`
