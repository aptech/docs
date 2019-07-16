
graphprt
==============================================

Purpose
----------------

Controls automatic printer hardcopy and conversion file output. Note: This function is for use with the deprecated PQG graphics. Use the
plotSave function instead.

Format
----------------
.. function:: graphprt(str)

    :param str: control string.
    :type str: string

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


Examples
----------------
Automatic print using a single graphics call:

::

    library pgraph;
    graphset;

    load x,y;

    graphprt("-p"); /* tell "xy" to print */
    xy(x,y);         /* create graph and print */

Automatic print using multiple graphic panels. Note :func:`graphprt` is called
once just before the :func:`endwind` call:

::

    library pgraph;
    graphset;

    load x,y;

    begwind;
    window(1,2,0);   /* create two windows */
    setwind(1);
    xy(x,y);         /* first graphics call */
    nextwind;
    xy(x,y);         /* second graphics call */
    graphprt("-p");
    endwind;        /* print page containing all graphs */

The next example shows how to build a string to be used with :func:`graphprt`:

::

    library pgraph;
    graphset;
    load x,y;

    cvtnam = "mycvt.eps"; /* name of output file */
    /* concatenate options into one string */
    cmdstr = "-c=1" $+ " -cf=" $+ cvtnam;
    cmdstr = cmdstr $+ " -q";

    graphprt(cmdstr); /* tell "xy" to convert and */
    /* close */
    xy(x,y); /* create graph and convert */

The above string ``cmdstr`` will read as follows:

::

    "-c=1 -cf=mycvt.eps -q"

Source
------

pgraph.src
