
graphset
==============================================

Purpose
----------------

Reset graphics global variables to default values. Note: This function is for use with the deprecated PQG graphics.

Format
----------------
.. function:: graphset



Remarks
-------

This procedure is used to reset the defaults between graphs.

:func:`graphset` may be called between each graphic panel to be displayed.

To change the default values of the global control variables, make the
appropriate changes in the file :file:`pgraph.dec` and to the procedure
:func:`graphset`.



Source
------

pgraph.src
