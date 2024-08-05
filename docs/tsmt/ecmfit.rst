ecmFit
======

Purpose
-------
Calculate and return parameter estimates for an error correction model.

Format
------
.. function:: vmo = ecmFit(y, p[, vmc])
              vmo = ecmFit(dataset, formula, p[, vmc])

   :param y: data.
   :type y: Nx1 vector

   :param dataset: name of data set or null string.
   :type dataset: string

   :param formula: formula string of the model. E.g. "y ~ X1 + X2" 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables; E.g. "y ~ ." , '.' means including all variables except dependent variable 'y';
   :type formula: string

   :param p: order of AR process.
   :type p: scalar

   :param vmc: Optional input, an instance of a :class:`varmamtControl` structure. The following members of *vmc* are referenced within this routine:

      .. include:: include/varmamtcontrol.rst

   :type vmc: struct

   :return vmo: An instance of a :class:`varmamtOut` structure containing the following members:

      .. include:: include/varmamtout.rst

   :rtype vmo: struct

Example
-------

::

   new;
   cls,;
   library tsmt;

   // Load data
   fname = getGAUSSHome() $+ "pkgs/tsmt/examples/ecmmt.csv";
   y = csvReadM(fname, 1, 2);

   y = vmdiffmt(y, 1);

   // Declare varmamt control structure
   struct varmamtControl vmc;

   // Initialize control structure with default values
   vmc = varmamtControlCreate;

   // No contraints
   vmc.setConstraints = 0;

   // Set up start values
   phi = { 0.05 -0.05, 0 0.01, 0.1 -0.07, 0.05 -0.04 };
   vmc.start = pvcreate();
   vmc.start = pvPacki(vmc.start,areshape(phi, 2|2|2), "phi", 1);
   vmc.start = pvPacksi(vmc.start, xpnd(15.9521|14.2525|15.9908), "vc", 3);

   // Call ecmFit
   struct varmamtOut vout;
   vout = ecmFit(y , 1, vmc);


Remarks
-------
Errors are assumed to be distributed :math:`N(0, Q)`.

Library
-------
tsmt

Source
------
varmamt.src

.. seealso:: Functions :func:`varmaFit`
