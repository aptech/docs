pdfmvlogit
==============================================

Purpose
----------------

Computes the gradient of the standard multivariate logistic probability density function (PDF). 

Format
----------------
.. function:: w = pdfmvlogit(a)

    :param a: Abscissae.
    :type a: KxQ matrix

    :return w: Evaluated probability density at each observation.
    :rtype w: Qx1 vector


Source
------------

gradients-mvn.src
