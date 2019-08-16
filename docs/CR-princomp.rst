
princomp
==============================================

Purpose
----------------

Computes principal components of a data matrix.

Format
----------------
.. function:: { p, v, a } = princomp(x, j)

    :param x: :math:`N > K`, full rank.
    :type x: NxK data matrix

    :param j: number of principal components to be computed (:math:`j <= K`).
    :type j: scalar

    :return p: of the first *j* principal components of *x* in descending order of amount of variance explained.

    :rtype p: NxJ matrix

    :return v: of fractions of variance explained.

    :rtype v: Jx1 vector

    :return a: factor loadings such that:
        
        .. math:: x = p*a + error.

    :rtype a: JxK matrix

.. DANGER:: fix equations

Remarks
-------

Adapted from a program written by Mico Loretan.

The algorithm is based on Theil, Henri "Principles of Econometrics." Wiley, NY, 1971, 46-56.

Example
-------

::

   // Create matrix with percent return
   // of 4 stocks over 11 time periods
   pcnt_return = {  0.0646   1.2326   0.0508  -0.0346,
                   -0.1632   0.1806   0.1104   0.1276, 
                    1.3477   1.3347   0.1424   0.0159, 
                   -0.4465  -0.5691  -0.1524  -0.1719, 
                    1.6232   1.4690  -0.0192   0.0979, 
                    0.3381   0.5307   0.0610   0.0374, 
                   -0.0383   0.2556   0.0370   0.0518, 
                    0.4493   0.3140   0.0177   0.1001, 
                    0.5896   0.0542   0.1991   0.2669, 
                   -0.2218   0.3772   0.1189   0.1234, 
                    1.1778  -0.0464  -0.1282   0.2171 };

   // Compute: all 4 principal component vectors,
   //         percent variance explained
   //         matrix of factor loadings
   { p, v, a } = princomp(pcnt_return, 4);

After the code above:

::

    p =   0.2662  -0.6077   0.0965  -0.2951     v = 0.8394     a = 2.4244   2.3264   0.1321   0.2227 
          0.0059  -0.1702  -0.3938  -0.1569         0.1436         0.9506  -0.9977  -0.1402   0.1566
          0.5631  -0.0350   0.0953   0.6146         0.0144         0.0317   0.0153  -0.2757  -0.3420
         -0.2170   0.0709   0.4012  -0.0219         0.0026         0.0208  -0.0188   0.1455  -0.1162
          0.6491   0.0491   0.2359  -0.2269 
          0.1823  -0.1085  -0.0554   0.0444 
          0.0456  -0.1485  -0.1299  -0.1762 
          0.1624   0.0654  -0.1032  -0.1584 
          0.1445   0.2677  -0.6520   0.2598 
          0.0337  -0.3008  -0.3926  -0.2472 
          0.2447   0.6267  -0.0115  -0.5214

From the results above, we can see that approximately 83.9% of the
variance in the *pcnt_return* is included in the first principal component
vector and another 14.36% is included in the second principal component.

