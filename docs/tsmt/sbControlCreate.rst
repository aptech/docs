===============
sbControlCreate
===============

10.0.48sbControlCreate
======================

Purpose
-------

.. container::
   :name: Purpose

   Sets the members of a declared sbControl structure to default values.

Library
-------

.. container:: gfunc
   :name: Library

   tsmt

Format
------

.. container::
   :name: Format

   sbc0 = sbControlCreate( );

Input
-----

.. container::
   :name: Input

   None

Output
------

.. container::
   :name: Output

   +------+--------------------------------------------------------------+
   | sbc0 | An instance of a sbControl structure with all members set to |
   |      | default values.                                              |
   +------+--------------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Declare sbControl structure
      struct sbControl sbc0;

      //Initialize instance of structure
      sbc0 = sbControlCreate( );

Source
------

.. container:: gfunc
   :name: Source

   sbcontrolcreate.src
