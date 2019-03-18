
system
==============================================

Purpose
----------------
Quits GAUSS and returns to the operating system.

Format
----------------
.. function:: system 
			  system c

    :param c: an optional exit code that can be
        recovered by the program that invoked GAUSS.
        The default is 0. Valid arguments are 0-255.
    :type c: scalar

