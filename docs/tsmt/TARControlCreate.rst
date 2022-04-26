================
TARControlCreate
================

10.0.55TARControlCreate
=======================

Purpose
-------

.. container::
   :name: Purpose

   Sets the members of a declared structural break control structure to
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

   tar0 = TARControlCreate( );

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
   | tar0 | An instance of a TARControlCreate structure with all members |
   |      | set to default values.                                       |
   +------+--------------------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Declare the structure 
      struct TARControl TAR0;

      //Initialize the structure 
      TAR0 = TARControlCreate( );

Source
------

.. container:: gfunc
   :name: Source

   tarcontrolcreate.src
