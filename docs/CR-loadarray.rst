
loadarray
==============================================

Purpose
----------------

Loads an N-dimensional array from a disk file.

Format
----------------
.. function:: filename



Remarks
-------

If no filename is given, as with x above, then the symbol name the file
is to be loaded into is used as the filename, and the proper extension
is added.

If more than one item is to be loaded in a single statement, the names
should be separated by commas.

The filename can be either a literal or a string. If the filename is in
a string variable, then the ^ (caret) operator must precede the name of
the string, as in:

::

   filestr = "mydata/adat";
   loadarray x = ^filestr;

If no extension is supplied, then an .fmt extension will be assumed.

loadarray accepts pathnames. The following is legal:

::

   loadarray k = /gauss/a;

This will load /gauss/a.fmt into k.

If the path= subcommand is used, the path string will be remembered
until changed in a subsequent command. This path will be used for all
loadarray, loadm, and load calls whenever none is specified.

The current path setting can be obtained (and changed) with the sysstate
function, case 5.

::

   loadarray path = /data;

This will change the loadarray path without loading anything.

::

   loadarray path = /gauss a,b,c;

This will load a.fmt, b.fmt, and c.fmt using /gauss as a path. This path
will be used for the next loadarray, loadm, or load call if none is
specified.

The load path or save path can be overridden in any particular load or
save by putting an explicit path on the filename given to load from or
save to as follows:

::

   loadarray path = /miscdata;
   loadarray a = /data/mydata1, b, c = hisdata;

In the above program:

/data/mydata1.fmt would be loaded into an array called a.

/miscdata/b.fmt would be loaded into an array called b.

/miscdata/hisdata.fmt would be loaded into an array called c.

::

   oldarraypath = sysstate(5,"/data");
   loadarray a, b;
   call  sysstate(5,oldarraypath);

This will get the old loadarray path, set it to /data, load a.fmt and
b.fmt, and reset the loadarray path to its original setting.

.. seealso:: Functions :func:`load`, :func:`save`, :func:`let`, :func:`sysstate`
