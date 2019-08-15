
load, loadf, loadk, loadm, loadp, loads
==============================================

Purpose
----------------

Loads from a disk file.

.. _load:
.. _loadf:
.. _loadk:
.. _loadm:
.. _loadp:
.. _loads:
.. index:: load, loadf, loadk, loadm, loadp, loads

Format
----------------

::

    load [[path=path]]x, y[ ]=filename, z = filename;

Remarks
-------

All the ``loadxx`` commands use the same syntax-they only differ in the
types of symbols you use them for:

.. list-table::
    :widths: auto

    * - `load`, `loadm`
      - matrix
    * - `loads`
      - string
    * - `loadf`
      - function (`fn`)
    * - `loadk`
      - keyword (`keyword`)
    * - `loadp`
      - procedure (`proc`)

If no filename is given, as with *x* above, then the symbol name the file
is to be loaded into is used as the filename, and the proper extension
is added.

If more than one item is to be loaded in a single statement, the names
should be separated by commas.

The filename can be either a literal or a string. If the filename is in
a string variable, then the ``^`` (caret) operator must precede the name of
the string, as in:

::

   filestr = "mydata/char";
   loadm x = ^filestr;

If no extension is supplied, the proper extension for each type of file
will be used automatically as follows:

.. csv-table::
    :widths: auto

    "`load`", ":file:`.fmt` - matrix file or delimited ASCII file"
    "`loadm`", ":file:`.fmt` - matrix file or delimited ASCII file"
    "`loads`", ":file:`.fst` - string file"
    "`loadf`", ":file:`.fcg` - user-defined function (`fn`) file"
    "`loadk`", ":file:`.fcg` - user-defined keyword (`keyword`) file"
    "`loadp`", ":file:`.fcg` - user-defined procedure (`proc`) file"

These commands also signal to the compiler what type of object the
symbol is so that later references to it will be compiled correctly.

A dummy definition must exist in the program for each symbol that is
loaded in using `loadf`, `loadk`, or `loadp`. This resolves the need to have
the symbol initialized at compile time. When the load executes, the
dummy definition will be replaced with the saved definition:

::

   proc corrmat;
   endp;

   loadp corrmat;
   y = corrmat;
    
   keyword regress(x); endp;
   loadk regress;
   regress x on y z t from data01;
    
   fn sqrd=;
   loadf sqrd;
   y = sqrd(4.5);

To load GAUSS files created with the `save` command, no brackets are used
with the symbol name.

If you use `save` to save a scalar error code 65535 (i.e., ``error(65535)``),
it will be interpreted as an empty matrix when you load it again.

ASCII data files
++++++++++++++++

To load ASCII data files, square brackets follow the name of the symbol.

Numbers in ASCII files must be delimited with spaces, commas, tabs, or
newlines. If the size of the matrix to be loaded is not explicitly
given, as in:

::

   load x[] = data.asc;

GAUSS will load as many elements as possible from the file and create an
Nx1 matrix. This is the preferred method of loading ASCII data from a
file, especially when you want to verify if the load was successful.
Your program can then see how many elements were actually loaded by
testing the matrix with the rows command, and if that is correct, the
Nx1 matrix can be `reshape`'d to the desired form. You could, for
instance, put the number of rows and columns of the matrix right in the
file as the first and second elements and reshape the remainder of the
vector to the desired form using those values.

If the size of the matrix is explicitly given in the `load` command, then
no checking will be done. If you use:

::

   load x[500,6] = data.asc;

GAUSS will still load as many elements as possible from the file into an
Nx1 matrix and then automatically reshape it using the dimensions given.

If you `load` data from a file, :file:`data.asc`, which contains nine numbers (1 2
3 4 5 6 7 8 9), then the resulting matrix will be as follows:

::

   load x[1,9] = data.asc;

::

   x = 1 2 3 4 5 6 7 8 9

::

   load x[3,3] = data.asc;

::

       1 2 3 
   x = 4 5 6 
       7 8 9

::

   load x[2,2] = data.asc;

::

   x = 1 2
       3 4

::

   load x[2,9] = data.asc;

::

   x = 1 2 3 4 5 6 7 8 9
       1 2 3 4 5 6 7 8 9

::

   load x[3,5] = data.asc;

::

       1 2 3 4 5
   x = 6 7 8 9 1
       2 3 4 5 6

`load` accepts pathnames. The following is legal:

::

   loadm k = /gauss/x;

This will load :file:`/gauss/x.fmt` into *k*.

If the ``path=`` subcommand is used with `load` and `save`, the *path* string will
be remembered until changed in a subsequent command. This path will be
used whenever none is specified. There are four separate paths for:

#. `load`, `loadm`
#. `loadf`, `loadp`
#. `loads`
#. `save`

Setting any of the four paths will not affect the others. The current
path settings can be obtained (and changed) with the :func:`sysstate` function,
cases 4-7.

::

     loadm path = /data;

This will change the `loadm` path without loading anything.

::

     load path = /gauss x,y,z;

This will load :file:`x.fmt`, :file:`y.fmt`, and :file:`z.fmt` using :file:`/gauss` as a path. This path
will be used for the next `load` if none is specified.

The `load` path or `save` path can be overridden in any particular `load` or
`save` by putting an explicit path on the filename given to `load` from or
`save` to as follows:

::

   loadm path = /miscdata;
   loadm x = /data/mydata1, y, z = hisdata;

In the above program:

:file:`/data/mydata1.fmt` would be loaded into a matrix called *x*.

:file:`/miscdata/y.fmt` would be loaded into a matrix called *y*.

:file:`/miscdata/hisdata.fmt` would be loaded into a matrix called *z*.


::

   oldmpath = sysstate(5,"/data");
   load x, y;
   call sysstate(5,oldmpath);

This will get the old `loadm` path, set it to :file:`/data`, load :file:`x.fmt` and :file:`y.fmt`,
and reset the `loadm` path to its original setting.

.. seealso:: Functions :func:`loadd`, :func:`dataload`, `save`, `let`, :func:`con`, :func:`cons`, :func:`sysstate`

