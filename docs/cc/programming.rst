
Programming
==================

Program control
------------------


=====================    ======================================================
:doc:`../changedir`      Changes the working directory within a program.
:doc:`../end`            Terminates a program and closes all files.
:doc:`../pause`          Pauses for the specified time.
:doc:`../sleep`          Sleeps for the specified time.
:doc:`../stop`           Stops a program and leaves files open.
:doc:`../system`         Quits and returns to the OS.
=====================    ======================================================


Flow control
------------------


=============================    ======================================================
:doc:`../break`                   Jumps out the bottom of a do or for loop.
:doc:`../continue`                Jumps to the top of a do or for loop.
:doc:`../dowhiledountil`          Executes a series of statements in a loop based on a conditional statement.
:doc:`../for`                     Loops with integer counter.
:doc:`../if`                      Conditional branching.
:doc:`../waitwaitc`               Waits until any key is pressed.
=============================    ======================================================


Error handling and debugging
-----------------------------------


=============================    ======================================================
:doc:`../debug`                   Executes a program under the source level debugger.
:doc:`../error`                   Creates user-defined error code.
:doc:`../errorlog`                Sends an error message to screen and log file.
:doc:`../errorlogat`              Sends an error message with the line number of the error report to the screen and log file.
:doc:`../linesonlinesoff`         Includes or omits line number and file name records from program.
:doc:`../scalerr`                 Tests for a scalar error code.
:doc:`../trace`                   Traces program execution for debugging.
:doc:`../trap`                    Controls trapping of program errors.
:doc:`../trapchk`                 Examines the trap flag.
:doc:`../warninglog`              Prints a warning message to the error window and error log file. The only difference between this and errorlog() is that it will display a warning icon in the error output window.
:doc:`../warninglogat`            Prints a warning message to the window and warning log file, along with the file name and line number at which the warning occurred. The only difference between this and errorlogat() is that it will display a warning icon in the error output window
=============================    ======================================================


Procedures, keywords and functions
-------------------------------------

=============================    ======================================================
:doc:`../call`                     Calls function and discards return values.
:doc:`../dynargscount`             Returns the number of dynamic arguments passed into the current procedure.
:doc:`../dynargsget`               Returns specified dynamic arguments with the option to set default values.
:doc:`../dynargstypes`             Returns a vector containing the types of the dynamic arguments passed into the current procedure.
:doc:`../endp`                     Terminates a procedure definition.
:doc:`../fn`                       Allows user to create one-line functions.
:doc:`../keyword`                  Begins the definition of a keyword procedure. Keywords are user-defined functions with local or global variables.
:doc:`../local`                    Declares variables local to a procedure.
:doc:`../proc`                     Begins definition of multi-line procedure.
:doc:`../retp`                     Returns from a procedure.
=============================    ======================================================

User input
------------

=============================    ======================================================
:doc:`../con_`                    Requests console input, creates matrix.
:doc:`../cons`                    Requests console input, creates string.
:doc:`../key`                     Gets the next key from the keyboard buffer. If buffer is empty, returns a 0.
:doc:`../keyav`                   Checks if keystroke is available.
:doc:`../keyw`                    Gets the next key from the keyboard buffer. If buffer is empty, waits for a key.
=============================    ======================================================

Output
-----------

=============================    ======================================================
:doc:`../head`                   Returns the first ``n`` rows of a matrix, dataframe or string array.
:doc:`../output`                 Directs printed output to a file.
:doc:`../print`                  Prints matrices, arrays, strings and string arrays to the screen and/or auxiliary output.
:doc:`../sprintf`                Converts numeric vectors, string vectors and their combinations into formatted strings.
:doc:`../tail`                   Returns the last ``n`` rows of a matrix, dataframe or string array.
=============================    ======================================================




General
----------

=============================    ======================================================
:doc:`../compile`                 Compiles a source file to a compiled code file.
:doc:`../run`                     Runs a program in a text file.
=============================    ======================================================
