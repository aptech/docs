
save
==============================================

Purpose
----------------

Saves matrices, strings, or procedures to a disk file.

Format
----------------
.. function:: path xsave x

    :param vflag: version flag.
    :type vflag: TODO

    .. csv-table::
        :widths: auto

        "-v89", "not supported"
        "-v92", "supported on UNIX, Windows"
        "-v96", "supported on all platformsSee also  Foreign Language Interface, Chapter  1, for details on the various versions. The default format can be specified in gauss.cfg by setting the dat_fmt_version configuration variable. If dat_fmt_version is not set, the default is v96."

    :param path: literal or ^string, a default path to
        use for this and subsequent save's.
    :type path: TODO

    :param x: the name of the file the symbol will be saved
        in is the same as this with the proper extension added for the type
        of the symbol.
    :type x: a symbol name

    :param lpath: literal or ^string, a local path and filename to be
        used for a particular symbol. This path will override the path
        previously set and the filename will override the name of the symbol
        being saved. The extension cannot be overridden.
    :type lpath: TODO

    :param y: the symbol to be saved to  lpath.
    :type y: TODO

Examples
----------------

::

    spath = "/gauss";
    save path = ^spath x,y,z;

Save x, y, and z using 
/gauss as the path. This path will be
used for the next save if none is specified.

::

    svp = "/gauss/data";
    save path = ^svp n, k, /gauss/quad1=quad;

n and k will be saved using /gauss/data as
the save path, quad will be saved in /gauss 
with the name quad1.fmt.
On platforms that use the backslash as the path separator, the
double backslash is required inside double quotes to produce a backslash because it
is the escape character in quoted strings. It is not required when specifying
literals.

::

    save path=/procs;

Change save path to /procs.

::

    save path = /miscdata;
    save /data/mydata1 = x, y, hisdata = z;

In the above program:
x would be saved in /data/mydata1.fmt

y would be saved in /miscdata/y.fmt

z would be saved in /miscdata/hisdata.fmt

.. seealso:: Functions :func:`datasave`, :func:`load`, :func:`saveall`, :func:`saved`
