dynFacBAM
=========

Purpose
-------
Provide Bayesian estimates of the posterior distributions of a dynamic, two-factor model.

Format
------
.. function:: dynOut = dynFacBAM(data, dctl)

    :param data: Matrix (NumSubGroups*NumObs x (3+k)), a stacked matrix of observable data. It must include a data/observation indicator in the first column, a group indicator in the second column, and a sub-group indicator in the third column. Unstacked panel series data can be converted to an acceptable format using the createDynFacData procedure.
    :type data: Matrix

    :param dctl: An instance of a :class:`dynControl` structure. For an instance of the :class:`dynControl` structure named *dctl* the members are:
       
        .. include:: include/dyncontrol.rst
    
    :type dctl: struct

    :return dOut: An instance of the :class:`dynOut` structure. For an instance of the :class:`dynOut` structure named *dOut* the members are:
    
        .. include:: include/dynout.rst
    
    :rtype: struct


