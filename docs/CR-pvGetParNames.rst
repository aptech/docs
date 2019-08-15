
pvGetParNames
==============================================

Purpose
----------------

Generates names for parameter vector stored in structure of type :class:`PV`.

Format
----------------
.. function:: s = pvGetParNames(p1)

    :param p1: an instance of structure of type *PV*
    :type p1: struct

    :return s: names of parameters.

    :rtype s: Kx1 string array

Remarks
-------

If the vector in the structure of type :class:`PV` was generated with matrix
names, the parameter names will be concatenations of the matrix name
with row and column numbers of the parameters in the matrix. Otherwise
the names will have a generic prefix with concatenated row and column
numbers.


Examples
----------------

::

    // Define PV structure
    #include pv.sdf
    // Declare 'p1' as an instance of a 'PV' structure
    struct PV p1;
    
    // Initialize 'p1' with default values
    p1 = pvCreate;
    
    // Data to pack into the 'PV' struct
    x = { 1 2,
          3 4 };
    
    // 1's indicate an element to pack into the structure
    // 0's indicate elements to NOT pack into the structure
    mask = { 1 0,
             0 1 };
    
    // Pack values of 'x' selected by 'mask' into 'pi' and name 
    // this resulting vector, 'P'
    p1 = pvPackm(p1,x,"P",mask);
     
    print pvGetParNames(p1);

Since mask has ones in the :math:`[1,1]` and :math:`[2,2]` locations, the code above, produces:

::

     P[1,1]
     P[2,2]

Source
------

pv.src

