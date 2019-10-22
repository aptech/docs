
save
==============================================

Purpose
----------------

Saves matrices, strings, or procedures to a disk file.

.. _save:
.. index:: save

Format
----------------

::

    save vflag path=path x, lpath=y;
    save path=path x;
    save x;

**Parameters**

:vflag: (*literal*) version flag

    ========= =========================================
    ``-v89``  not supported
    ``-v92``  supported on UNIX, Windows
    ``-v96``  supported on all platforms. See also `Foreign Language Interface`, 
              Chapter 1, for details on the various versions. The default format 
              can be specified in :file:`gauss.cfg` by setting the *dat_fmt_version* configuration 
              variable. If *dat_fmt_version* is not set, the default is *v96*.
    ========= =========================================

:path: (*literal or ^string*) a default path to use for this and subsequent `save`'s.

:x: (*literal*) a symbol name, the name of the file the symbol will be saved in is the same as this with the proper extension added for the type of the symbol.

:lpath: (*literal or ^string*) a local path and filename to be used for a particular symbol. This path will override 
    the path previously set and the filename will override the name of the symbol 
    being saved. The extension cannot be overridden.

:y: (*literal*) the symbol to be saved to *lpath*

Examples
----------------

::

    spath = "/gauss";
    save path = ^spath x,y,z;

Save *x*, *y*, and *z* using :file:`/gauss` as the path. This path will be used for the next `save` if none is specified.

::

    svp = "/gauss/data";
    save path = ^svp n, k, /gauss/quad1=quad;

*n* and *k* will be saved using :file:`/gauss/data` as the save path, quad will be saved in :file:`/gauss` 
with the name :file:`quad1.fmt`. On platforms that use the backslash as the path separator, the
double backslash is required inside double quotes to produce a backslash because it
is the escape character in quoted strings. It is not required when specifying
literals.

::

    save path=/procs;

Change save path to :file:`/procs`.

::

    save path = /miscdata;
    save /data/mydata1 = x, y, hisdata = z;

In the above program:

*x* would be saved in :file:`/data/mydata1.fmt`

*y* would be saved in :file:`/miscdata/y.fmt`

*z* would be saved in :file:`/miscdata/hisdata.fmt`

Remarks
-------

`save` can be used to save matrices, strings, procedures, and functions.

Procedures and functions must be compiled and resident in memory before
they can be `save`'d.

The following extensions will be given to files that are save'd:

+--------------+------+
|    matrix    | .fmt |
+--------------+------+
|    string    | .fst |
+--------------+------+
|    procedure | .fcg |
+--------------+------+
|    function  | .fcg |
+--------------+------+
|    keyword   | .fcg |
+--------------+------+

If the ``path=`` subcommand is used with `save`, the path string will be
remembered until changed in a subsequent command. This path will be used
whenever none is specified. The `save` path can be overridden in any
particular `save` by specifying an explicit path and filename.


.. seealso:: Functions :func:`datasave`, `load`, `saveall`, :func:`saved`

