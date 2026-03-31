Using the Command Line Interface
================================

**ENGAUSS** is the command line version of **GAUSS**, which comes with the **GAUSS Engine**. The executable file, **engauss**, is located in the **GAUSS Engine** installation directory.

The format for using **ENGAUSS** is:

**engauss** *flag(s) program program...*

+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| -b              | Execute file in batch mode and then exit. You can execute multiple files by separating file names with spaces.                     |
+=================+====================================================================================================================================+
| -l *logfile*    | Set the name of batch mode log file when using the *-b* argument. The default is **wksp/gauss.log.###,** where **###** is the pid. |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| -e *expression* | Executes a **GAUSS** expression. This command is not logged when **GAUSS** is in batch mode.                                       |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| -o              | Suppresses the sign-on banner (output only).                                                                                       |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| -T              | Turns the dataloop translator on.                                                                                                  |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+
| -t              | Turns the dataloop translator off.                                                                                                 |
+-----------------+------------------------------------------------------------------------------------------------------------------------------------+

Viewing Graphics 
---------------------

**GAUSS** generates **.tkf** files for graphical output. The default output for graphics is **graphic.tkf**. Two functions are available to convert **.tkf** files to PostScript for printing and viewing with external viewers: the **tkf2ps** function will convert .\ **tkf** files to PostScript\ **(.ps)** files, and the **tkf2eps** function will convert .\ **tkf** files to encapsulated PostScript(**.eps**) files. For example, to convert the file **graphic.tkf** to a postscript file named **graphic.ps** use:

ret = tkf2ps *(“filename.*\ **tkf**\ *”, “filename.*\ **ps**\ *”)*

If the function is successful it returns **0**.

Interactive Commands 
-------------------------

quit 
~~~~~~~~~~~

The **quit** command will exit **ENGAUSS**.

The format for **quit** is:

quit

You can also use the **system** command to exit **ENGAUSS** from either the command line or a program (see **system** in the **GAUSS** Language Reference). The format for **system** is:

system

ed 
~~~~~~~~~

The **ed** command will open an input file in an external text editor, see **ed** in the **GAUSS** Language Reference.

The format for **ed** is:

ed *filename*

compile 
~~~~~~~~~~~~~~

The **compile** command will compile a **GAUSS** program file to a compiled code file.

The format for **compile** is:

**compile** *source_file*

**compile** *source_file output_file*

If you do not specify an *output_file*, **GAUSS** will append a .\ **gcg** extension to your *source_file* to create an *output_file*. Unlike the **gc** compiler, the **compile** command will not automatically replace a **.gau** extension with a **.gcg** extension. It will append a **.gcg** extension to .\ **gau** files.

run 
~~~~~~~~~~

The **run** command will run a **GAUSS** program file or compiled code file.

The format for **run**:

**run** *filename*

browse 
~~~~~~~~~~~~~

The **browse** command allows you to search for specific symbols in a file and open the file in the default editor. You can use wildcards to extend search capabilities of the **browse** command.

The format for **browse** is:

browse *symbol*

config 
~~~~~~~~~~~~~

The **config** command gives you access to the configuration menu allowing you to change the way **GAUSS** runs and compiles files.

The format for **config** is:

config

Run Menu 
^^^^^^^^^

+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Translator                      | Toggles on/off the translation of a file using **dataloop**. The translator is not necessary for **GAUSS** program files not using **dataloop**. |
+=================================+==================================================================================================================================================+
| Line number tracking            | Toggles on/off execution time line number tracking of the original file before translation.                                                      |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Translator line number tracking | Toggles on/off the execution time line number tracking. If the translator is on, the line numbers refer to the translated file.                  |
+---------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Compile Menu 
^^^^^^^^^^^^^

+---------------------+------------------------------------------------------------------------------------------+
| Autoload            | Toggles on/off the autoloader.                                                           |
+=====================+==========================================================================================+
| GAUSS_Library       | Toggles on/off the **GAUSS** library functions.                                          |
+---------------------+------------------------------------------------------------------------------------------+
| Autodelete          | Toggles on/off autodelete.                                                               |
+---------------------+------------------------------------------------------------------------------------------+
| User Library        | Toggles on/off the user library functions.                                               |
+---------------------+------------------------------------------------------------------------------------------+
| Declare Warnings    | Toggles on/off the **declare** warning messages during compiling.                        |
+---------------------+------------------------------------------------------------------------------------------+
| Compiler Trace      |                                                                                          |
+---------------------+------------------------------------------------------------------------------------------+
|                     | **Off** Turns off the compiler trace function.                                           |
+---------------------+------------------------------------------------------------------------------------------+
|                     | **On** Turns on the compiler trace function.                                             |
+---------------------+------------------------------------------------------------------------------------------+
|                     | **Line** Traces compilation by line.                                                     |
+---------------------+------------------------------------------------------------------------------------------+
|                     | **File** Creates a report of procedures and the local and global symbols they reference. |
+---------------------+------------------------------------------------------------------------------------------+

Debugging 
--------------

The **debug** command runs a program under the source level debugger.

The format for **debug** is:

debug *filename*

General Functions 
^^^^^^^^^^^^^^^^^^

+-------------------+---------------------------------------------------------------+
| ?                 | Displays a list of available commands.                        |
+===================+===============================================================+
| q/Esc             | Exits the debugger and returns to the **GAUSS** command line. |
+-------------------+---------------------------------------------------------------+
| +/-               | Enables/disables the last command repeat function.            |
+-------------------+---------------------------------------------------------------+

Listing Functions 
^^^^^^^^^^^^^^^^^^

+--------------------+------------------------------------------------------------------------------+
| **l** *number*     | Displays a specified number of lines of source code in the current file.     |
+====================+==============================================================================+
| lc                 | Displays source code in the current file starting with the current line.     |
+--------------------+------------------------------------------------------------------------------+
| **ll** *file line* | Displays source code in the named file starting with the specified line.     |
+--------------------+------------------------------------------------------------------------------+
| **ll** *file*      | Displays source code in the named file starting with the first line.         |
+--------------------+------------------------------------------------------------------------------+
| **ll** *line*      | Displays source code starting with the specified line. File does not change. |
+--------------------+------------------------------------------------------------------------------+
| ll                 | Displays the next page of source code.                                       |
+--------------------+------------------------------------------------------------------------------+

Execution Functions 
^^^^^^^^^^^^^^^^^^^^

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| s *number*      | Executes the specified number of lines, stepping over procedures.                                                                                                                |
+=================+==================================================================================+===============================================================================================+
| i *number*      | Executes the specified number of lines, stepping into procedures.                                                                                                                |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| X *number*      | Executes code from the beginning of the program to the specified line count, or until a breakpoint is hit.                                                                       |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| G [[*args*]]    | Executes from the current line to the end of the program, stopping at breakpoints. The optional arguments specify other stopping points.                                         |
|                 |                                                                                                                                                                                  |
|                 | The syntax for each optional argument is:                                                                                                                                        |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *filename line cycle*                                                            | The debugger will stop every *cycle* times it reaches the specified *line* in the named file. |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *filename line*                                                                  | The debugger will stop when it reaches the specified *line* in the named file.                |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *filename , cycle*                                                               | The debugger will stop every *cycle* times it reaches any *line* in the current file.         |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *line cycle*                                                                     | The debugger will stop every *cycle* times it reaches the specified line in the current file. |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *filename*                                                                       | The debugger will stop at every *line* in the named file.                                     |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *line*                                                                           | The debugger will stop when it reaches the specified *line* in the current file.              |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *procedure cycle*                                                                | The debugger will stop every *cycle* times it reaches the first *line* in a called procedure. |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
|                 | *procedure*                                                                      | The debugger will stop every time it reaches the first *line* in a called procedure.          |
+-----------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| j [[*args*]]    | Executes code to a specified line, procedure, or cycle in the file without stopping at breakpoints. The optional arguments are the same as **g,** listed above.                  |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| jx *number*     | Executes code to the execution count specified (*number*) without stopping at breakpoints.                                                                                       |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| o               | Executes the remainder of the current procedure (or to a breakpoint) and stops at the next line in the calling procedure.                                                        |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 View Commands 
^^^^^^^^^^^^^^^

+---------------------------+---------------------------------------------------------------------------------------------------------+
| **v [[**\ *vars*\ **]]**  | Searches for (a local variable, then a global variable) and displays the value of a specified variable. |
+===========================+=========================================================================================================+
| **v$ [[**\ *vars*\ **]]** | Searches for (a local variable, then a global variable) and displays the specified character matrix.    |
+---------------------------+---------------------------------------------------------------------------------------------------------+

The display properties of matrices can be set using the following commands:

+------------------+-----------------------------------------------------------------------------+
| r                | Specifies the number of rows to be shown.                                   |
+==================+=============================================================================+
| c                | Specifies the number of columns to be shown.                                |
+------------------+-----------------------------------------------------------------------------+
| *number, number* | Specifies the indices of the upper left corner of the block to be shown.    |
+------------------+-----------------------------------------------------------------------------+
| w                | Specifies the width of the columns to be shown.                             |
+------------------+-----------------------------------------------------------------------------+
| p                | Specifies the precision shown.                                              |
+------------------+-----------------------------------------------------------------------------+
| f                | Specifies the format of the numbers as decimal, scientific, or auto format. |
+------------------+-----------------------------------------------------------------------------+
| q                | Quits the matrix viewer.                                                    |
+------------------+-----------------------------------------------------------------------------+

Breakpoint Commands 
^^^^^^^^^^^^^^^^^^^^

+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lb           | Shows all the breakpoints currently defined.                                                                                                               |
+==============+==========================================================+=================================================================================================+
| b [[*args*]] | Sets a breakpoint in the code. The syntax for each optional argument is:                                                                                   |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *filename line cycle*                                    | The debugger will stop every *cycle* times it reaches the specified *line* in the named file.   |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *filename line*                                          | The debugger will stop when it reaches the specified *line* in the named file.                  |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *filename , cycle*                                       | The debugger will stop every *cycle* times it reaches any *line* in the current file.           |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *line cycle*                                             | The debugger will stop every *cycle* times it reaches the specified *line* in the current file. |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *filename*                                               | The debugger will stop at every *line* in the named file.                                       |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *line*                                                   | The debugger will stop when it reaches the specified *line* in the current file.                |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *procedure cycle*                                        | The debugger will stop every *cycle* times it reaches the first *line* in a called procedure.   |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
|              | *procedure*                                              | The debugger will stop every time it reaches the first *line* in a called procedure.            |
+--------------+----------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| d [[*args*]] | Removes a previously specified breakpoint. The optional arguments are the same arguments as **b**, listed above.                                           |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
