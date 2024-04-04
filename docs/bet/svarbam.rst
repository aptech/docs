svarBAM
=======

Purpose
-------
Estimates parameters of a reduced form VAR model. Returns both the parameter estimates and boot-strapped standard error terms.

Format
------
.. function:: svarOut = svarBAM(svard0, svarCtl0)

   :param svard0: An instance of the :class:`svarDataControl` structure. For an instance of the :class:`svarDataControl` structure named *svard0* the members are:
        .. include:: include/svardatacontrol.rst
   :type svard0: struct

   :param svarCtl0: An instance of the :class:`svarControl` structure. For an instance of the :class:`svarControl` structure named *svarCtl0* the members are:
       .. include:: include/svarcontrol.rst
   :type svarCtl0: struct

   :return svarOut: An instance of the :class:`svarOutput` structure. For an instance of the :class:`svarOut` structure named *sOut* the members are:
      .. include:: include/svarout.rst
   :rtype: struct

Remarks
--------