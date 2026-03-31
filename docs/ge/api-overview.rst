C API: Overview
===============

Functions 
---------------

Pre-initialization setup 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the first functions called. Use these to setup logging, I/O, error handling and the home directory location.

+------------------------------------+---------------------------------------------------------------------+
| GAUSS_GetHome                      | Gets the **GAUSS Engine** home path.                                |
+====================================+=====================================================================+
| GAUSS_GetHomeVar                   | Gets the name of the environment variable containing the home path. |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_HookProgramErrorOutput       | Sets the callback function for program error output.                |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_HookProgramInputChar         | Sets callback function for **key** function.                        |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_HookProgramInputCharBlocking | Sets callback function for **keyw** and **show** functions.         |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_HookProgramInputCheck        | Sets callback function for **keyav** function.                      |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_HookProgramInputString       | Sets callback function for **con** and **cons** functions.          |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_HookProgramOutput            | Sets the callback function for normal program output.               |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_SetHome                      | Sets the **GAUSS Engine** home path directly.                       |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_SetHomeVar                   | Sets the name of an environment variable containing the home path.  |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_SetLogFile                   | Sets the file name and path for logging system errors.              |
+------------------------------------+---------------------------------------------------------------------+
| GAUSS_SetLogStream                 | Sets the file pointer for logging system errors.                    |
+------------------------------------+---------------------------------------------------------------------+

Initialization and Shutdown 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_Initialize            | Initializes the **GAUSS Engine**. Call at the beginning of your application, after setup functions. |
+=============================+=====================================================================================================+
| GAUSS_Shutdown              | Shuts the **GAUSS Engine** down. Call prior to ending your application.                             |
+-----------------------------+-----------------------------------------------------------------------------------------------------+


Compiling and Executing GAUSS programs 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+------------------------------------------------------------------+
| GAUSS_CompileExpression        | Compiles a right-hand side expression.                           |
+================================+==================================================================+
| GAUSS_CompileFile              | Compiles a file containing **GAUSS** code.                       |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_CompileString            | Compiles a character string containing **GAUSS** code.           |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_CompileStringAsFile      | Compiles a character string containing **GAUSS** code as a file. |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_CreateWorkspace          | Creates a workspace handle.                                      |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_Execute                  | Executes a program.                                              |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_ExecuteExpression        | Executes a right-hand side expression.                           |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_FreeProgram              | Frees a program handle created in a compile.                     |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_FreeWorkspace            | Frees a workspace handle.                                        |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_LoadCompiledBuffer       | Loads a compiled program from a buffer.                          |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_LoadCompiledFile         | Loads a compiled program from a file.                            |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_LoadWorkspace            | Loads workspace information saved in a file.                     |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_SaveProgram              | Saves a compiled program as a file.                              |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_SaveWorkspace            | Saves workspace information in a file                            |
+--------------------------------+------------------------------------------------------------------+
| GAUSS_TranslateDataloopFile    | Translates a dataloop file.                                      |
+--------------------------------+------------------------------------------------------------------+


Calling Procedures 
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CallProc                 | Calls a procedure                                                                    |
+================================+======================================================================================+
| GAUSS_CallProcFreeArgs         | Calls a procedure and frees its arguments.                                           |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyArgToArg             | Copies an argument from one argument list to another.                                |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyArgToArray           | Copies an array from an argument list descriptor to an array descriptor.             |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyArgToMatrix          | Copies a matrix from an argument list descriptor to a matrix descriptor.             |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyArgToString          | Copies a string from an argument list descriptor to a string descriptor.             |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyArgToStringArray     | Copies a string array from an argument list descriptor to a string array descriptor. |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyArrayToArg           | Copies an array to an argument list descriptor.                                      |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyMatrixToArg          | Copies a matrix to an argument list descriptor.                                      |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyStringArrayToArg     | Copies a string array to an argument list descriptor.                                |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CopyStringToArg          | Copies a string to an argument list descriptor.                                      |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CreateArgList            | Creates an empty argument list descriptor.                                           |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_CreateProgram            | Creates a program handle to use when calling a procedure.                            |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_DeleteArg                | Deletes an argument from an argument list descriptor.                                |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_FreeArgList              | Frees an argument list descriptor.                                                   |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_GetArgType               | Gets the type of an argument in an argument list descriptor.                         |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_InsertArg                | Inserts an argument in an argument list descriptor.                                  |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveArgToArg             | Moves an argument from one argument list to another.                                 |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveArgToArray           | Moves an array from an argument list descriptor to an array descriptor.              |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveArgToMatrix          | Moves a matrix from an argument list descriptor to a matrix descriptor.              |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveArgToString          | Moves a string from an argument list descriptor to a string descriptor.              |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveArgToStringArray     | Moves a string array from an argument list descriptor to a string array descriptor.  |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveArrayToArg           | Moves an array to an argument list descriptor.                                       |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveMatrixToArg          | Moves a matrix to an argument list descriptor.                                       |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveStringArrayToArg     | Moves a string array to an argument list descriptor.                                 |
+--------------------------------+--------------------------------------------------------------------------------------+
| GAUSS_MoveStringToArg          | Moves a string to an argument list descriptor.                                       |
+--------------------------------+--------------------------------------------------------------------------------------+

Creating and Freeing GAUSS Format Data 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_ComplexArray            | Creates an array descriptor for a complex array and copies the array.                               |
+===============================+=====================================================================================================+
| GAUSS_ComplexArrayAlias       | Creates an array descriptor for a complex array.                                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_ComplexMatrix           | Creates a matrix descriptor for a complex matrix and copies the matrix.                             |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_ComplexMatrixAlias      | Creates a matrix descriptor for a complex matrix.                                                   |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_FreeArray               | Frees an array descriptor.                                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_FreeMatrix              | Frees a matrix descriptor.                                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_FreeString              | Frees a string descriptor.                                                                          |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_FreeStringArray         | Frees a string array descriptor.                                                                    |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_Array                   | Creates an array descriptor and copies array.                                                       |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_ArrayAlias              | Creates an array descriptor.                                                                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_Matrix                  | Creates a matrix descriptor and copies matrix.                                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_MatrixAlias             | Creates a matrix descriptor.                                                                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_String                  | Creates a string descriptor and copies the string.                                                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_StringAlias             | Creates a string descriptor.                                                                        |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_StringAliasL            | Creates a string descriptor for a string of user-specified length.                                  |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_StringArray             | Creates a string array descriptor and copies the string array.                                      |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_StringArrayL            | Creates a string array descriptor for strings of user-specified length and copies the string array. |
+-------------------------------+-----------------------------------------------------------------------------------------------------+
| GAUSS_StringL                 | Creates a string descriptor for string of user-specified length and copies the string.              |
+-------------------------------+-----------------------------------------------------------------------------------------------------+

Moving Data Between GAUSS and Your Application 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+--------------------------------------------------------------+
| GAUSS_AssignFreeableArray       | Assigns **malloc**\ ’d data to a global array.               |
+=================================+==============================================================+
| GAUSS_AssignFreeableMatrix      | Assigns **malloc**\ ’d data to a global matrix.              |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_CopyGlobal                | Copies a symbol from one workspace to another.               |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_CopyArrayToGlobal         | Copies an array to **GAUSS**.                                |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_CopyMatrixToGlobal        | Copies a matrix to **GAUSS**.                                |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_CopyStringToGlobal        | Copies a string to **GAUSS**.                                |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_CopyStringArrayToGlobal   | Copies a string array to **GAUSS**.                          |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetDouble                 | Gets a double from a **GAUSS** global.                       |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetArray                  | Gets an array from a **GAUSS** global.                       |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetArrayAndClear          | Gets an array from a **GAUSS** global and clears the global. |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetMatrix                 | Gets a matrix from a **GAUSS** global.                       |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetMatrixAndClear         | Gets a matrix from a **GAUSS** global and clears the global. |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetMatrixInfo             | Gets information for a matrix in a **GAUSS** global.         |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetString                 | Gets a string from a **GAUSS** global.                       |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetStringArray            | Gets a string array from a **GAUSS** global.                 |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_GetSymbolType             | Gets the type of a symbol in a **GAUSS** global.             |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_MoveArrayToGlobal         | Moves an array to **GAUSS** and frees the descriptor.        |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_MoveMatrixToGlobal        | Moves a matrix to **GAUSS** and frees the descriptor.        |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_MoveStringToGlobal        | Moves a string to **GAUSS** and frees the descriptor.        |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_MoveStringArrayToGlobal   | Moves a string array to **GAUSS** and frees the descriptor.  |
+---------------------------------+--------------------------------------------------------------+
| GAUSS_PutDouble                 | Puts a double into **GAUSS**.                                |
+---------------------------------+--------------------------------------------------------------+

GAUSS Engine Error Handling 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+-------------------------------------------------+
| GAUSS_CheckInterrupt            | Checks for a thread-specific interrupt request. |
+=================================+=================================================+
| GAUSS_ClearGlobalInterrupt      | Clears a global interrupt request.              |
+---------------------------------+-------------------------------------------------+
| GAUSS_ClearInterrupt            | Clears a thread-specific interrupt request.     |
+---------------------------------+-------------------------------------------------+
| GAUSS_ClearProgramInterrupt     | Clears a program interrupt request.             |
+---------------------------------+-------------------------------------------------+
| GAUSS_ClearWorkspaceInterrupt   | Clears a workspace interrupt request.           |
+---------------------------------+-------------------------------------------------+
| GAUSS_ErrorText                 | Gets the text for an error number.              |
+---------------------------------+-------------------------------------------------+
| GAUSS_GetError                  | Gets the stored error number.                   |
+---------------------------------+-------------------------------------------------+
| GAUSS_GetLogFile                | Gets the current error log file.                |
+---------------------------------+-------------------------------------------------+
| GAUSS_GetLogStream              | Gets the current error log stream.              |
+---------------------------------+-------------------------------------------------+
| GAUSS_SetError                  | Sets the stored error number.                   |
+---------------------------------+-------------------------------------------------+
| GAUSS_SetGlobalInterrupt        | Sets a global interrupt request.                |
+---------------------------------+-------------------------------------------------+
| GAUSS_SetInterrupt              | Sets a thread specific interrupt request.       |
+---------------------------------+-------------------------------------------------+
| GAUSS_SetProgramInterrupt       | Sets a program interrupt request.               |
+---------------------------------+-------------------------------------------------+
| GAUSS_SetWorkspaceInterrupt     | Sets a workspace interrupt request.             |
+---------------------------------+-------------------------------------------------+

Include Files 
-------------------

**mteng.h** contains all the function declarations, structure definitions, etc. for the C API. Include it in any C file that references the **GAUSS Engine**.
