=======
arimamt
=======

10.0.9automtControlCreate
=========================

Purpose
-------
Sets the members of an instance of an automtControl structure to
   default values.

Library
-------
tsmt

Format
------
arc = automtControlCreate();

Input
-----
None

Output
------
+-----+---------------------------------------------------------------+
   | arc | An instance of an automtControlstructure with its members set |
   |     | to default values.                                            |
   +-----+---------------------------------------------------------------+

Example
-------
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
autoregmt.src
