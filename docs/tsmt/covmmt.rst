========
covmmtmt
========

10.0.16covmmt
=============

Purpose
-------

.. container::
   :name: Purpose

   Prints covariance matrix of parameters with labels.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   a = covmmt(vout);

Input
-----

.. container::
   :name: Input

   ==== =============================================
   vout A post-estimation instance of the varmamtOut.
   ==== =============================================

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;
      //Create file name with full path
      fname = getGAUSSHome $+ "pkgs/tsmt/examples/mink.csv";

      //Load two variables from the dataset into matrix 'y'
      y = loadd(fname, "LogMink + LogMusk");

      //Difference the data
      y = vmdiffmt(y, 1);

      //Declare 'vout' to be a varmamtOut structure
      struct varmamtOut vout;

      //Estimate the parameters of the VAR(3) model
      vout = varmaFit(y, 3); 

      //Print covariance matrix
      print "";
      print "";

      print covmmt(vout);

Source
------

.. container::
   :name: Source

   autoregmt.src
