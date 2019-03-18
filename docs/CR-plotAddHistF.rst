
plotAddHistF
==============================================

Purpose
----------------
Adds a frequency histogram to an existing graph.

Format
----------------
.. function:: plotAddHistF(myPlot, f, c)plotAddHistF(f, c)

    :param myPlot: A plotControl structure.
    :type myPlot: TODO

    :param f: frequencies to be graphed.
    :type f: Nx1 vector

    :param c: numeric labels for categories.
        If this is a scalar 0, a sequence from 1 to rows(f) will be created.
    :type c: Nx1 vector

