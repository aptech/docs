====================
varmamtControlCreate
====================

10.0.63varmamtControlCreate
===========================

Purpose
-------
Sets the members of an instance of a varmamtControl structure to
   default values.

Library
-------
tsmt

Format
------
vmc = varmamtControlCreate( );

Input
-----
None

Output
------
+-----+---------------------------------------------------------------+
   | amc | An instance of a varmamtControl structure with its members    |
   |     | set to default values.                                        |
   +-----+---------------------------------------------------------------+

Example
-------
::

new;
cls;
library tsmt;

// Declare control structure
struct varmamtControl vsc;
vsc = varmamtControlCreate( );

Source
------
varmamt.src
