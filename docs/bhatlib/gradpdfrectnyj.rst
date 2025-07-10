gradpdfrectnyj
==============================================
Purpose
----------------
Computes the gradient of the PDF for a rectangular distribution with user-specified truncation.

Format
----------------
.. function:: grad = gradpdfrectnyj(x, a, b)

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