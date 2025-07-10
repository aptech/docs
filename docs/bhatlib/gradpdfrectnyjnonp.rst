gradpdfrectnyjnonp
==============================================
Purpose
----------------
Computes the gradient of the PDF of a rectangular distribution without parameterization adjustments.

Format
----------------
.. function:: grad = gradpdfrectnyjnonp(x, a, b)

    :param x: Evaluation points.
    :type x: scalar or vector

    :param a: Lower truncation point.
    :type a: scalar

    :param b: Upper truncation point.
    :type b: scalar

    :return grad: Gradient values.
    :rtype grad: scalar or vector

Library
-------
bhatlib

Source
------
gradients-mvn.src