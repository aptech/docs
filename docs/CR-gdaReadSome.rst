
gdaReadSome
==============================================

Purpose
----------------

Reads part of a variable from a GAUSS Data Archive.

Format
----------------
.. function:: gdaReadSome(filename,  varname,  index,  orders)

    :param filename: name of data file.
    :type filename: string

    :param varname: name of variable in the GDA.
    :type varname: string

    :param index: index into variable where read is to begin.
    :type index: scalar or Nx1 vector

    :param orders: orders of object to output.
    :type orders: scalar or Kx1 vector

    :returns: y (*matrix*), array, string or string array, variable data.

Examples
----------------

::

    x = rndn(100,50);
    ret = gdaCreate("myfile.gda",1);
    ret = gdaWrite("myfile.gda",x,"x1");
     
    index = { 35,20 };
    orders = { 25,5 };
    y = gdaReadSome("myfile.gda","x1",index,orders);

This example reads 25*5=125 elements from x1, beginning
with the [35,20] element. The 125 elements are returned as
a 25x5 matrix, y.

.. seealso:: Functions :func:`gdaWriteSome`, :func:`gdaRead`
