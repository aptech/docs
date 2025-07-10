randcorr
==============================================
Purpose
----------------
Generates a random correlation matrix.

Format
----------------
.. function:: rcorr = randcorr(d, delta)

    :param d: Dimension of the correlation matrix.
    :type d: scalar

    :param delta: Small positive scalar for stability.
    :type delta: scalar

    :return rcorr: Random correlation matrix of size d x d.
    :rtype rcorr: matrix

Library
-------
bhatlib

Source
------
vecup.src