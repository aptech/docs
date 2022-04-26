=======
arimamt
=======

10.0.4arimamtControlCreate
==========================

Purpose
-------

.. container::
   :name: Purpose

   Sets the members of an instance of an arimamtControl structure to
   default values.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   amc = arimamtControlCreate();

Input
-----

.. container::
   :name: Input

   None

Output
------

.. container::
   :name: Output

   +-----+---------------------------------------------------------------+
   | amc | An instance of an arimamtControl structure with its members   |
   |     | set to default values.                                        |
   +-----+---------------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Declare control structures
      struct arimamtControl amc;

      //Create default settings for arima model              
      amc = arimamtControlCreate();

Source
------

.. container::
   :name: Source

   arimamt.src
