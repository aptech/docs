
draw
==============================================

Purpose
----------------

Graphs lines, symbols, and text using the PQG global
variables. This procedure does not require actual X,
Y, or Z data since its main purpose is to manually
build graphs using  _pline,_pmsgctl, _psym,
_paxes, _parrow and other globals.
NOTE: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: draw

Examples
----------------

::

    library pgraph;
    graphset;
     
    begwind;
    makewind(9,6.855,0,0,0); /* make full size window for 
                              plot */
    makewind(3,1,3,3,0);     /* make small overlapping window 
                              for text */
    setwind(1);
       x = seqa(.1,.1,100);
       y = sin(x); 
       xy(x,y);              /* plot data in first window */
    nextwind;
       _pbox = 15;
       _paxes = 0;
       _pnum = 0;
       _ptitlht = 1;
       margin(0,0,2,0);
       title("This is a text window.");
       draw;                  /* add a smaller text window */
    endwind;                  /* create graph */

Source
++++++

pdraw.src

.. seealso:: Functions :func:`window`, :func:`makewind`
