=======
arimamt
=======

10.0.9automtControlCreate
=========================

Purpose
-------

.. container::
   :name: Purpose

   Sets the members of an instance of an automtControl structure to
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

   arc = automtControlCreate();

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
   | arc | An instance of an automtControlstructure with its members set |
   |     | to default values.                                            |
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
      struct automtControl arc;

      //Create default settings for arima model  
      arc = arimamtControlCreate();

Source
------

.. container:: gfunc
   :name: Source

   autoregmt.src
