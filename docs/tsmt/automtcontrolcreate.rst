automtControlCreate
=========================

Purpose
-------
Sets the members of an instance of an :class:`automtControl` structure to default values.

Format
------
.. function:: arc = automtControlCreate();

  :return arc: instance of :class:`automtControlCreate` struct with members set to default values.
  :rtype arc: struct

Example
-------

::

 new;
 cls;
 library tsmt;

 // Declare control structures
 struct automtControl arc;

 // Create default settings for arima model
 arc = automtControlCreate();

Library
-------
tsmt

Source
------
autoregmt.src

.. seealso:: Functions  :func:`autoregFit`
