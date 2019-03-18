
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

Examples
----------------
Automatic print using a single graphics call:

::

    library pgraph;
    graphset;
    
    load x,y;
    
    graphprt("-p"); /* tell "xy" to print */
    xy(x,y);         /* create graph and print */

Automatic print using multiple graphic panels. Note graphprt is called
once just before the endwind call:

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

The next example shows how to build a string to be used with graphprt:

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

The above string cmdstr will read as follows:

::

    "-c=1 -cf=mycvt.eps -q"

Source
++++++

pgraph.src

.. raw:: html

   </div>
