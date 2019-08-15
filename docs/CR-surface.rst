
surface
==============================================

Purpose
----------------

Graphs a 3-D surface. 

.. NOTE:: This function is for use with the deprecated PQG graphics. Use :func:`plotSurface` instead.

Library
-------

pgraph

Format
----------------
.. function:: surface(x, y, z)

    :param x: the X axis data.
    :type x: 1xK vector

    :param y: the Y axis data.
    :type y: Nx1 vector

    :param z: the matrix of height data to be plotted.
    :type z: NxK matrix

Global Input
------------

.. data:: \_psurf

    2x1 vector, controls 3-D surface characteristics.

    :[1]: if 1, show hidden lines. Default 0.
    :[2]: color for base (default 7). The base is an outline of the X-Y plane with
        a line connecting each corner to the surface. If 0, no base is drawn.

.. data:: \_pticout

    scalar, if 0 (default), tick marks point inward, if 1, tick marks point outward.

.. data:: \_pzclr

    Z level color control.

    There are 3 ways to set colors for the Z levels of a surface graph.

    #. To specify a single color for the entire surface plot, set the color 
           control variable to a scalar value 1-15. For example:

        ::

            _pzclr = 15;

    #. To specify multiple colors distributed evenly over the entire Z range, 
           set the color control variable to a vector containing the desired colors 
           only. GAUSS will automatically calculate the required corresponding Z 
           values for you. The following example will produce a three color surface 
           plot, the Z ranges being lowest=blue, middle=light blue, highest=white:

        ::

            _pzclr = { 1, 10, 15 };

    #. To specify multiple colors distributed over selected ranges, the Z 
           ranges as well as the colors must be manually input by the user. The 
           following example assumes -0.2 to be the minimum value in the z matrix:

           ::
           
               _pzclr = { -0.2 1, 
               /* z >= -0.2 blue */
                0.0 10, 
               /* z >= 0.0 light blue */
                0.2 15 }; 
               /* z >= 0.2 white */

            Since a Z level is required for each selected color, the user must be
            responsible to compute the minimum value of the *z* matrix as the first Z
            range element. This may be most easily accomplished by setting the
            *\_pzclr* matrix as shown above (the first element being an arbitrary
            value), then resetting the first element to the minimum *z* value as
            follows:
            
            ::
            
                _pzclr = { 0.0 1,
                           0.0 10,
                           0.2 15 };
                _pzclr[1,1] = minc(minc(z));

See **PQG Graphics Colors**, for the list of available colors.

Remarks
-------

:func:`surface` uses only the minimum and maximum of the X axis data in
generating the graph and tick marks.

Source
------

psurface.src

.. seealso:: Functions :func:`volume`, :func:`view`

