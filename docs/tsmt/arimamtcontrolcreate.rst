arimamtControlCreate
=====================

Purpose
-------
Sets the members of an instance of an arimamtControl structure to
default values.

Format
------
.. function:: amc = arimamtControlCreate();

  :return amc: instance of :class:`arimatmtControl` struct with members set to default values.
  :rtype amc: struct

Example
-------
::

   new;
   cls;
   library tsmt;

   // Declare control structures
   struct arimamtControl amc;

   // Create default settings for arima model
   amc = arimamtControlCreate();

Library
-------
tsmt

Source
------
arimamt.src

.. seealso:: Functions :func:`arimaFit`
