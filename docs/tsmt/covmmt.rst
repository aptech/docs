covmmtmt
========

Purpose
-------
Prints covariance matrix of parameters with labels.

Format
------
.. function::  a = covmmt(vout);

  :param vout: a post-estimation instance of the :class:`varmamtOut`.
  :type vout: structure

  :return cov:
  :rtype cov: scalar

Example
-------

::

  new;
  cls;
  library tsmt;

  // Create file name with full path
  fname = getGAUSSHome $+ "pkgs/tsmt/examples/mink.csv";

  // Load two variables from the dataset into matrix 'y'
  y = loadd(fname, "LogMink + LogMusk");

  // Difference the data
  y = vmdiffmt(y, 1);

  // Declare 'vout' to be a varmamtOut structure
  struct varmamtOut vout;

  // Estimate the parameters of the VAR(1) model
  vout = varmaFit(y, 1);

  // Print covariance matrix
  print covmmt(vout);

The printed covariance matrix is:

::

  Covariance Matrix:

              phi[1,1,1]  phi[1,1,2]  phi[1,2,1]  phi[1,2,2]     vc[1,1]     vc[2,1]     vc[2,2]

  phi[1,1,1]     0.01557    -0.00504     0.00530    -0.00155     0.00001     0.00000    -0.00001
  phi[1,1,2]    -0.00504     0.01124    -0.00193     0.00384     0.00000     0.00001     0.00000
  phi[1,2,1]     0.00530    -0.00193     0.01571    -0.00511     0.00001     0.00000    -0.00001
  phi[1,2,2]    -0.00155     0.00384    -0.00511     0.01129     0.00000     0.00001     0.00001
     vc[1,1]     0.00001     0.00000     0.00001     0.00000     0.00016     0.00005     0.00002
     vc[2,1]     0.00000     0.00001     0.00000     0.00001     0.00005     0.00009     0.00006
     vc[2,2]    -0.00001     0.00000    -0.00001     0.00001     0.00002     0.00006     0.00016


Library
-------
tsmt

Source
------
autoregmt.src

.. seealso:: Functions :func:`varmaFit`
