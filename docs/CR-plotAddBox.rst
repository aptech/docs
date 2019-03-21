
plotAddBox
==============================================

Purpose
----------------
Adds a box graph to an existing graph.

Format
----------------
.. function:: plotAddBox(myPlot, grp, y) 
			              plotAddBox(grp, y)

    :param myPlot: 
    :type myPlot: A plotControl structure

    :param grp:  This contains the group numbers corresponding to each column of y data. If scalar 0, a sequence from 1 to cols(y) will be generated automatically for the X axis.
    :type grp: 1xM vector

    :param y:  Each column represents the set of y values for an individual percentiles box symbol.
    :type y: NxM matrix

