
box
==============================================

Purpose
----------------
Graphs data using the box graph percentile method. NOTE: This function uses the deprecated PQG graphics. Use
plotBox instead. 

Format
----------------
.. function:: box(grp, y)

    :param grp: 1xM vector. This contains the group numbers corresponding to each column of y data.
        If scalar 0, a sequence from 1 to cols(y) will be generated automatically for the X axis.
    :type grp: TODO

    :param y: NxM matrix. Each column represents the set of y values for an individual percentiles box symbol.
    :type y: TODO

