====================
varmamtControlCreate
====================

10.0.63varmamtControlCreate
===========================

Purpose
-------

.. container::
   :name: Purpose

   Sets the members of an instance of a varmamtControl structure to
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

   vmc = varmamtControlCreate( );

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
   | amc | An instance of a varmamtControl structure with its members    |
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

      //Declare control structure
      struct varmamtControl vsc;
      vsc = varmamtControlCreate( );

Source
------

.. container:: gfunc
   :name: Source

   varmamt.src
