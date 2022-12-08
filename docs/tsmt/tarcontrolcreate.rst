================
TARControlCreate
================

10.0.55TARControlCreate
=======================

Purpose
-------
Sets the members of a declared structural break control structure to
   default values.

Library
-------
tsmt

Format
------
tar0 = TARControlCreate( );

Input
-----
None

Output
------
+------+--------------------------------------------------------------+
| tar0 | An instance of a TARControlCreate structure with all members |
|      | set to default values.                                       |
+------+--------------------------------------------------------------+

Example
-------
::

new;
cls;
library tsmt;

// Declare the structure
struct TARControl TAR0;

// Initialize the structure 
TAR0 = TARControlCreate( );

Source
------
tarcontrolcreate.src
