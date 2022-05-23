===================
tscsmtControlCreate
===================

10.0.59tscsmtControlCreate
==========================

Purpose
-------
Sets the members of an instance of a tscsmtControl structure to
   default values.

Library
-------
tsmt

Format
------
tsc = tscsmtControlCreate( );

Input
-----
None

Output
------
+-----------------+-----------------------------------------------------+
   | tsc             | An instance of a tscsmtControl structure with its   |
   |                 | members set to default values.                      |
   +-----------------+-----------------------------------------------------+

Example
-------
::

new;
cls;
library tsmt;

//Declare control structure
struct tscsmtControl tsc;
tsc = tscsmtControlCreate();

Source
------
tscsmt.src
