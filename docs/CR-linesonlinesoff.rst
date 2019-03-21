
#lineson, #linesoff
==============================================

Purpose
----------------

The  #lineson command causes GAUSS to embed line
number and file name records in a program for the
purpose of reporting the location where an error occurs. The 
#linesoff command causes GAUSS to stop embedding line and file
records in a program.

Format
----------------
.. function:: #lineson 
			  #linesoff



Remarks
-------

In the "lines on" mode, GAUSS keeps track of line numbers and file names
and reports the location of an error when an execution time error
occurs. In the "lines off" mode, GAUSS does not keep track of lines and
files at execution time. During the compile phase, line numbers and file
names will always be given when errors occur in a program stored in a
disk file.

It is easier to debug a program when the locations of errors are
reported, but this slows down execution. In programs with several scalar
operations, the time spent tracking line numbers and file names is most
significant.

These commands have no effect on interactive programs (that is, those
typed in the window and run from the command line), since there are no
line numbers in such programs.

Line number tracking can be turned on and off through the user
interface, but the #lineson and #linesoff commands will override that.

The line numbers and file names given at run-time will reflect the last
record encountered in the code. If you have a mixture of procedures that
were compiled without line and file records and procedures that were
compiled with line and file records, use the trace command to locate
exactly where the error occurs.

The Currently active call error message will always be correct. If it
states that it was executing procedure xyz at line number nnn in file
ABC and xyz has no line nnn or is not in file ABC, you know that it just
did not encounter any line or file records in xyz before it crashed.

When using #include'd files, the line number and file name will be
correct for the file the error was in within the limits stated above.

