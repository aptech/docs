arimamt
=======

Purpose
-------
Sets the members of an instance of an arimamtControl structure to
default values.

Format
------
amc = arimamtControlCreate();

Input
-----
None

Output
------
+-----+---------------------------------------------------------------+
| amc | An instance of an arimamtControl structure with its members   |
|     | set to default values.                                        |
+-----+---------------------------------------------------------------+

Example
-------
::

   new;
   cls;
   library tsmt;

   //Declare control structures
   struct arimamtControl amc;

   //Create default settings for arima model              
   amc = arimamtControlCreate();

Library
-------
tsmt

Source
------
arimamt.src
