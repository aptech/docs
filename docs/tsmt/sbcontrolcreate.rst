===============
sbControlCreate
===============

10.0.48sbControlCreate
======================

Purpose
-------
Sets the members of a declared sbControl structure to default values.

Library
-------
tsmt

Format
------
sbc0 = sbControlCreate( );

Input
-----
None

Output
------
+------+--------------------------------------------------------------+
   | sbc0 | An instance of a sbControl structure with all members set to |
   |      | default values.                                              |
   +------+--------------------------------------------------------------+

Example
-------
::

new;
cls;
library tsmt;

// Declare sbControl structure
struct sbControl sbc0;

// Initialize instance of structure
sbc0 = sbControlCreate( );

Source
------
sbcontrolcreate.src
