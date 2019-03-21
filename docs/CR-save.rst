
save
==============================================

Purpose
----------------

Saves matrices, strings, or procedures to a disk file.

Format
----------------
.. function:: path xsave x

    :param vflag: 
    :type vflag: version flag

    .. csv-table::
        :widths: auto

        "-v89", "not supported"
        "-v92", "supported on UNIX, Windows"
        "-v96", "supported on all platformsSee also  Foreign Language Interface, Chapter  1, for details on the various versions. The default format can be specified in gauss.cfg by setting the dat_fmt_version configuration variable. If dat_fmt_version is not set, the default is v96."

    :param path: , a default path to
        use for this and subsequent save's.
    :type path: literal or ^string

    :param x: the name of the file the symbol will be saved
        in is the same as this with the proper extension added for the type
        of the symbol.
    :type x: a symbol name

    :param lpath: , a local path and filename to be
        used for a particular symbol. This path will override the path
        previously set and the filename will override the name of the symbol
        being saved. The extension cannot be overridden.
    :type lpath: literal or ^string

    :param y: 
    :type y: the symbol to be saved to  lpath

Remarks
-------

save can be used to save matrices, strings, procedures, and functions.
Procedures and functions must be compiled and resident in memory before
they can be save'd.

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

If the path= subcommand is used with save, the path string will be
remembered until changed in a subsequent command. This path will be used
whenever none is specified. The save path can be overridden in any
particular save by specifying an explicit path and filename.


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
