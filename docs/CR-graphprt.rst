
graphprt
==============================================

Purpose
----------------

Controls automatic printer hardcopy and conversion file output. Note: This function is for use with the deprecated PQG graphics. Use the
func:`plotSave` function instead.

Format
----------------
.. function:: graphprt(str)

    :param str: control string.
    :type str: string

Examples
----------------
Automatic print using a single graphics call:

::

    library pgraph;
    graphset;

    load x,y;

    // Tell xy to print
    graphprt("-p");

    // Create graph and print
    xy(x, y);

Automatic print using multiple graphic panels. Note :func:`graphprt` is called
once just before the :func:`endwind` call:

::

    library pgraph;
    graphset;

    load x,y;

    // Create two windows
    begwind;
    window(1, 2, 0);

    // First graphics call
    setwind(1);
    xy(x, y);

    // Second graphics call
    nextwind;
    xy(x, y);


    // Print page containing all graphs
    graphprt("-p");
    endwind;

The next example shows how to build a string to be used with :func:`graphprt`:

::

    library pgraph;
    graphset;
    load x,y;

    // Name of output file
    cvtnam = "mycvt.eps";

    // Concatenate options into one string
    cmdstr = "-c=1" $+ " -cf=" $+ cvtnam;
    cmdstr = cmdstr $+ " -q";

    /*
    ** Tell `xy` to convert and
    ** close
    */
    graphprt(cmdstr);

    // Create graph and convert
    xy(x, y);

The above string ``cmdstr`` will read as follows:

::

    "-c=1 -cf=mycvt.eps -q"

Remarks
-------

:func:`graphprt` is used to create hardcopy output automatically without user
intervention. The input string *str* can have any of the following items,
separated by spaces. If *str* is a null string, the interactive mode is
entered. This is the default.

.. list-table::
    :widths: auto

    * - \-p
      - print graph
    * - \-po=c
      - set print orientation:

        :l: landscape
        :p: portrait
    * - \-c=n
      - convert to another file format:

        :1: Encapsulated PostScript file.
        :3: HPGL Plotter file.
        :5: BMP (Windows Bitmap).
        :8: WMF (Windows Enhanced Metafile).

    * - \-cf=name
      - set converted output file name.
    * - \-i
      - minimize (iconize) the graphics window.
    * - \-q
      - close window after processing.
    * - \-w=n
      - display graph, wait n seconds, then continue.


Source
------

pgraph.src
