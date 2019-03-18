
axmargin
==============================================

Purpose
----------------
Sets absolute margins for the plot axes which control placement and size of plot. NOTE: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: axmargin(l, r,  t,  b)

    :param l: the left margin in inches.
    :type l: scalar

    :param r: the right margin in inches.
    :type r: scalar

    :param t: the top margin in inches.
    :type t: scalar

    :param b: the bottom margin in inches.
    :type b: scalar

Examples
----------------
The statement:

::

    library pgraph;
    axmargin(1,1,.5,.855);

will create a plot area of 7 inches horizontally by 5.5 inches
vertically, and positioned 1 inch right and .855 up from the lower
left corner of the graphic panel/page.

Source
++++++

pgraph.src

.. raw:: html

   </div>
