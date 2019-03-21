
gdaGetVarInfo
==============================================

Purpose
----------------

Gets information about all of the variables in a GAUSS Data 
Archive and returns it in an array of gdavartable 
structures.

Format
----------------
.. function:: gdaGetVarInfo(filename)

    :param filename: name of data file.
    :type filename: string

    :returns: vtab (*TODO*), Nx1 array of gdavartable
        structures, where N is the number of variables in
        filename, containing the following members:

    .. csv-table::
        :widths: auto

        "vtab[i].name", "string, name of variable."
        "vtab[i].type", "scalar, type of variable."
        "vtab[i].orders", "Mx1 vector or scalar, orders of the variable."

Remarks
-------

The size of vtab.orders is dependent on the type of the variable as
follows:

+---------------------------+---+
| Variable Type             | v |
|                           | t |
|                           | a |
|                           | b |
|                           | . |
|                           | o |
|                           | r |
|                           | d |
|                           | e |
|                           | r |
|                           | s |
+---------------------------+---+
| array                     | M |
|                           | x |
|                           | 1 |
|                           | v |
|                           | e |
|                           | c |
|                           | t |
|                           | o |
|                           | r |
|                           | , |
|                           | w |
|                           | h |
|                           | e |
|                           | r |
|                           | e |
|                           | M |
|                           | i |
|                           | s |
|                           | t |
|                           | h |
|                           | e |
|                           | n |
|                           | u |
|                           | m |
|                           | b |
|                           | e |
|                           | r |
|                           | o |
|                           | f |
|                           | d |
|                           | i |
|                           | m |
|                           | e |
|                           | n |
|                           | s |
|                           | i |
|                           | o |
|                           | n |
|                           | s |
|                           | i |
|                           | n |
|                           | t |
|                           | h |
|                           | e |
|                           | a |
|                           | r |
|                           | r |
|                           | a |
|                           | y |
|                           | , |
|                           | c |
|                           | o |
|                           | n |
|                           | t |
|                           | a |
|                           | i |
|                           | n |
|                           | i |
|                           | n |
|                           | g |
|                           | t |
|                           | h |
|                           | e |
|                           | s |
|                           | i |
|                           | z |
|                           | e |
|                           | s |
|                           | o |
|                           | f |
|                           | e |
|                           | a |
|                           | c |
|                           | h |
|                           | d |
|                           | i |
|                           | m |
|                           | e |
|                           | n |
|                           | s |
|                           | i |
|                           | o |
|                           | n |
|                           | , |
|                           | f |
|                           | r |
|                           | o |
|                           | m |
|                           | t |
|                           | h |
|                           | e |
|                           | s |
|                           | l |
|                           | o |
|                           | w |
|                           | e |
|                           | s |
|                           | t |
|                           | - |
|                           | m |
|                           | o |
|                           | v |
|                           | i |
|                           | n |
|                           | g |
|                           | d |
|                           | i |
|                           | m |
|                           | e |
|                           | n |
|                           | s |
|                           | i |
|                           | o |
|                           | n |
|                           | t |
|                           | o |
|                           | t |
|                           | h |
|                           | e |
|                           | f |
|                           | a |
|                           | s |
|                           | t |
|                           | e |
|                           | s |
|                           | t |
|                           | - |
|                           | m |
|                           | o |
|                           | v |
|                           | i |
|                           | n |
|                           | g |
|                           | d |
|                           | i |
|                           | m |
|                           | e |
|                           | n |
|                           | s |
|                           | i |
|                           | o |
|                           | n |
|                           | . |
+---------------------------+---+
| matrix                    | 2 |
|                           | x |
|                           | 1 |
|                           | v |
|                           | e |
|                           | c |
|                           | t |
|                           | o |
|                           | r |
|                           | c |
|                           | o |
|                           | n |
|                           | t |
|                           | a |
|                           | i |
|                           | n |
|                           | i |
|                           | n |
|                           | g |
|                           | t |
|                           | h |
|                           | e |
|                           | r |
|                           | o |
|                           | w |
|                           | s |
|                           | a |
|                           | n |
|                           | d |
|                           | c |
|                           | o |
|                           | l |
|                           | u |
|                           | m |
|                           | n |
|                           | s |
|                           | o |
|                           | f |
|                           | t |
|                           | h |
|                           | e |
|                           | m |
|                           | a |
|                           | t |
|                           | r |
|                           | i |
|                           | x |
|                           | , |
|                           | r |
|                           | e |
|                           | s |
|                           | p |
|                           | e |
|                           | c |
|                           | t |
|                           | i |
|                           | v |
|                           | e |
|                           | l |
|                           | y |
|                           | . |
+---------------------------+---+
| string                    | s |
|                           | c |
|                           | a |
|                           | l |
|                           | a |
|                           | r |
|                           | c |
|                           | o |
|                           | n |
|                           | t |
|                           | a |
|                           | i |
|                           | n |
|                           | i |
|                           | n |
|                           | g |
|                           | t |
|                           | h |
|                           | e |
|                           | l |
|                           | e |
|                           | n |
|                           | g |
|                           | t |
|                           | h |
|                           | o |
|                           | f |
|                           | s |
|                           | t |
|                           | r |
|                           | i |
|                           | n |
|                           | g |
|                           | , |
|                           | e |
|                           | x |
|                           | c |
|                           | l |
|                           | u |
|                           | d |
|                           | i |
|                           | n |
|                           | g |
|                           | t |
|                           | h |
|                           | e |
|                           | n |
|                           | u |
|                           | l |
|                           | l |
|                           | t |
|                           | e |
|                           | r |
|                           | m |
|                           | i |
|                           | n |
|                           | a |
|                           | t |
|                           | i |
|                           | n |
|                           | g |
|                           | b |
|                           | y |
|                           | t |
|                           | e |
|                           | . |
+---------------------------+---+
| string array              | 2 |
|                           | x |
|                           | 1 |
|                           | v |
|                           | e |
|                           | c |
|                           | t |
|                           | o |
|                           | r |
|                           | c |
|                           | o |
|                           | n |
|                           | t |
|                           | a |
|                           | i |
|                           | n |
|                           | i |
|                           | n |
|                           | g |
|                           | t |
|                           | h |
|                           | e |
|                           | r |
|                           | o |
|                           | w |
|                           | s |
|                           | a |
|                           | n |
|                           | d |
|                           | c |
|                           | o |
|                           | l |
|                           | u |
|                           | m |
|                           | n |
|                           | s |
|                           | o |
|                           | f |
|                           | t |
|                           | h |
|                           | e |
|                           | s |
|                           | t |
|                           | r |
|                           | i |
|                           | n |
|                           | g |
|                           | a |
|                           | r |
|                           | r |
|                           | a |
|                           | y |
|                           | , |
|                           | r |
|                           | e |
|                           | s |
|                           | p |
|                           | e |
|                           | c |
|                           | t |
|                           | i |
|                           | v |
|                           | e |
|                           | l |
|                           | y |
|                           | . |
+---------------------------+---+

vtab.type may contain any of the following:

+----+--------------+
| 6  | matrix       |
+----+--------------+
| 13 | string       |
+----+--------------+
| 15 | string array |
+----+--------------+
| 21 | array        |
+----+--------------+


Examples
----------------

::

    //Execute structure definition
    #include gdafns.sdf
    struct gdavartable vtab;
    
    vtab = gdaGetVarInfo("myfile.gda");

Source
++++++

gdafns.src

.. seealso:: Functions :func:`gdaReportVarInfo`, :func:`gdaGetNames`, :func:`gdaGetTypes`, :func:`gdaGetOrders`
