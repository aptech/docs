
pvPack
==============================================

Purpose
----------------

Packs general matrix into a structure of type PV with matrix name.

Format
----------------
.. function:: pvPack(p1, x, nm)

    :param p1: 
    :type p1: an instance of structure of type PV

    :param x: 
    :type x: MxN matrix or N-dimensional array

    :param nm: name of matrix/array.
    :type nm: string

    :returns: p1 (*TODO*), an instance of structure of type PV.

Examples
----------------

Basic usage
+++++++++++

::

    //Create starting parameter vector
    start_vals = { 0,
                   1,
                   1 };
    
    //Declare 'p1' as an instance of a 'PV' structure
    struct PV p1;
    
    //Initialize 'p1' with default settings
    p1 = pvCreate();
    
    //Add a variable named 'b' in 'p1' containing the data from 'start_vals'
    p1 = pvPack(p1, start_vals, "b");

The data can be extracted using the pvUnpack
command:

::

    b_out = pvUnpack(p1,"b");
    print b_out;

The code above, should return the following output:

::

    0
    1
    1

Source
++++++

pv.src

.. seealso:: Functions :func:`pvPackm`, :func:`pvPacks`, :func:`pvUnpack`
