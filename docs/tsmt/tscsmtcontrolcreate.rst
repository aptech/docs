===================
tscsmtControlCreate
===================

10.0.59tscsmtControlCreate
==========================

Purpose
-------

.. container::
   :name: Purpose

   Sets the members of an instance of a tscsmtControl structure to
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

   tsc = tscsmtControlCreate( );

Input
-----

.. container::
   :name: Input

   None

Output
------

.. container::
   :name: Output

   +-----------------+-----------------------------------------------------+
   | tsc             | An instance of a tscsmtControl structure with its   |
   |                 | members set to default values.                      |
   +-----------------+-----------------------------------------------------+

Example
-------

.. container::
   :name: Example

   ::

      new;
      cls;
      library tsmt;

      //Declare control structure
      struct tscsmtControl tsc;
      tsc = tscsmtControlCreate();

Source
------

.. container:: gfunc
   :name: Source

   tscsmt.src
