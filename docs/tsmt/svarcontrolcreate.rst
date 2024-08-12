svarControlCreate
=====================

Purpose
-------
Sets the members of an instance of an :class:`svarControl` structure to
default values.

Format
------
.. function:: sctl = svarControlCreate();

  :return amc: instance of :class:`svarControl` struct with members set to default values.
  :rtype amc: struct

Example
-------

::

   new;
   cls;
   library tsmt;

   // Declare control structures
   struct svarControl sCtl;

   // Create default settings for SVAR model
   sCtl = svarControlCreate();

.. seealso:: Functions :func:`svarFit`
