
pvPacki
==============================================

Purpose
----------------

Packs general matrix or array into a PV instance with
name and index.

Format
----------------
.. function:: pvPacki(p1, x, nm, i)

    :param p1: 
    :type p1: an instance of structure of type PV

    :param x: 
    :type x: MxN matrix or N-dimensional array

    :param nm: name of matrix or array, or null string.
    :type nm: string

    :param i: index of matrix or array in lookup table.
    :type i: scalar

    :returns: p1 (*struct*) instance of :class:`PV` struct.

Examples
----------------

::

    //Define the 'PV' structure
    #include pv.sdf
     
    y = rndn(100,1);
    x = rndn(100,5);
    
    //Declare 'p1' as an instance of a 'PV' structure
    struct PV p1;
    
    //Initialize 'p1' with default values
    p1 = pvCreate;
    
    //Pack the variables in with a variable name and an index
    p1 = pvPacki(p1,y,"Y",1);
    p1 = pvPacki(p1,x,"X",2);

pvUnpack

::

    //Unpack variables by index
    y = pvUnpack(p1,1);
    x = pvUnpack(p1,2);
    
    //Unpack variables by variable name
    y = pvUnpack(p1,"Y");
    x = pvUnpack(p1,"X");

.. seealso:: Functions :func:`pvPack`, :func:`pvUnpack`
