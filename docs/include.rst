
#include
==============================================

Purpose
----------------

Inserts code from another file into a GAUSS program.

Format
----------------
.. function:: #include filename
			  #include "filename"

Examples
----------------

::

    #include  "/gauss/inc/cond.inc"

The command will cause the code in the program :file:`cond.inc` to be merged into the current program at the point at which this statement appears.

Remarks
-------

filename can be any legitimate file name.

This command makes it possible to write a section of general-purpose
code, and insert it into other programs.

The code from the ``#include``'d file is inserted literally as if it were
merged into that place in the program with a text editor.

If a path is specified for the file, then no additional searching will
be attempted if the file is not found.

If a path is not specified, the current directory will be searched
first, then each directory listed in ``src_path``. ``src_path`` is defined in
:file:`gauss.cfg`.

+-----------------------------------+---------------------------------------+
| #include/gauss/myprog.prc         | No additional search will be made     |
|                                   | if the file is not found.             |
+-----------------------------------+---------------------------------------+
| #includemyprog.prc                | The directories listed in             |
|                                   | ``src_path`` will be searched for     |
|                                   | :file:`myprog.prc` if the file is not |
|                                   | found in the current directory.       |
+-----------------------------------+---------------------------------------+

Compile time errors will return the line number and the name of the file
in which they occur. For execution time errors, if a program is compiled
with #lineson, the line number and name of the file where the error
occurred will be printed. For files that have been ``#include``'d this
reflects the actual line number within the ``#include``'d file. See ``#lineson``
for a more complete discussion of the use of and the validity of line
numbers when debugging.


.. seealso:: Functions `run`, :func:`lineson`

