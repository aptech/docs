Using the GAUSS Engine
======================

This chapter covers the general guidelines for creating an application that uses the **GAUSS Engine**. Specific multi-threading issues are covered in Chapter 5.

The use of the **GAUSS Engine** can be broken up into the following steps:

- Setup and Initialization

  - Set up logging

  - Set home directory

  - Hook I/O callback functions

  - Initialize Engine

- Computation

  - Create workspaces

  - Copy or move data

  - Compile or load **GAUSS** code

  - Execute **GAUSS** code

  - Free workspaces

- Shutdown

Setup and Initialization
----------------------------

Logging
~~~~~~~~~~~~~

General **GAUSS Engine** system errors are sent to a file and/or a stream pointer. Default values are provided for each. You can change the default values or turnoff logging altogether with **GAUSS_SetLogFile** and **GAUSS_SetLogStream**. This should be done before calling any other **GAUSS Engine** functions.

Home Directory 
~~~~~~~~~~~~~~~~~~~~~

The **GAUSS Engine** home directory location is usually set to the same directory as the main executable of the calling application. It is used to locate the configuration file, Run-Time Library files, etc. used by the **GAUSS Engine**.

Use **GAUSS_SetHome** to set the home directory, prior to calling **GAUSS_Initialize**. An alternate method is to use **GAUSS_SetHomeVar** to set the name of an environment variable that contains the home directory location.

I/O CallbackFunctions 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **GAUSS Engine** calls user defined functions for program output from **print** statements and for error messages. Default functions are provided for the main thread in console applications.

+---------------------------------+------------------------------------+
| Normal program output           | **stdout**                         |
+---------------------------------+------------------------------------+
| Program error output            | **stderr**                         |
+---------------------------------+------------------------------------+
| Program input                   | **stdin**                          |
+---------------------------------+------------------------------------+

To change the default behavior, you can supply callback functions of your own and use the following functions to hook them:

+---------------------------------+------------------------------------+
| Normal program output           | **GAUSS_HookProgramOutput**        |
+---------------------------------+------------------------------------+
| Program error output            | **GAUSS_HookProgramErrorOutput**   |
+---------------------------------+------------------------------------+
| Program input                   | **GAUSS_HookProgramInputString**   |
+---------------------------------+------------------------------------+

The functions **GAUSS_HookProgramInputChar, GAUSS_HookProgramInputCharBlocking** and **GAUSS_HookProgramInputCheck** are also supported, but no default behavior is defined.

All I/O callback functions are thread specific and must be explicitly hooked in each thread that uses them, except for the three above that are hooked by default for the main thread.

Use the hook functions to specify the input functions that the GAUSS Engine calls as follows:

+------------------------------------+------------------------------------+
| **Functions Hooked By**            | **Are Called By**                  |
+------------------------------------+------------------------------------+
| GAUSS_HookProgramInputChar         | key                                |
+------------------------------------+------------------------------------+
| GAUSS_HookProgramInputCharBlocking | keyw, show                         |
+------------------------------------+------------------------------------+
| GAUSS_HookProgramInputCheck        | keyav                              |
+------------------------------------+------------------------------------+
| GAUSS_HookProgramInputString       | con, cons                          |
+------------------------------------+------------------------------------+

There are two hook functions that are used to control output from **GAUSS** programs. Use **GAUSS_HookProgramOutput**

to hook a function that **GAUSS** will call to display all normal program output. Use **GAUSS_HookProgramErrorOutput**

to hook a function that **GAUSS** will call to display all program error output.

Initialize Engine 
~~~~~~~~~~~~~~~~~~~~~~~~

Call **GAUSS_Initialize** after the previous steps are completed. The **GAUSS Engine** ready for use.

Computation 
----------------

Workspaces 
~~~~~~~~~~~~~~~~~

All computation in the **GAUSS Engine** is done in a *workspace*. Workspaces are independent from one another and each workspace contains its own global data and procedures. Workspaces are created with **GAUSS_CreateWorkspace**, which returns a *workspace handle*.

Workspaces are freed with **GAUSS_FreeWorkspace**. The contents of a workspace can be saved to disk with **GAUSS_SaveWorkspace**.

Programs 
~~~~~~~~~~~~~~~

Two functions are provided in order to execute **GAUSS** program code. Each requires *a program handle.*

+---------------------------------+---------------------------------------+
| **GAUSS_Execute**               | Executes a **GAUSS** program          |
+---------------------------------+---------------------------------------+
| **GAUSS_ExecuteExpression**     | Executes a right-hand side expression |
+---------------------------------+---------------------------------------+

Six functions are provided to create program handles. A program handle contains compiled **GAUSS** program code.

+---------------------------------+---------------------------------------------------+
| **GAUSS_CompileExpression**     | Compiles a right-hand side expression             |
+---------------------------------+---------------------------------------------------+
| **GAUSS_CompileFile**           | Compiles a **GAUSS** program file                 |
+---------------------------------+---------------------------------------------------+
| **GAUSS_CompileString**         | Compiles **GAUSS** commands in a character string |
+---------------------------------+---------------------------------------------------+
| **GAUSS_CompileStringAsFile**   | Compiles **GAUSS** commands in a character string |
+---------------------------------+---------------------------------------------------+
| **GAUSS_LoadCompiledFile**      | Loads a compiled program from disk                |
+---------------------------------+---------------------------------------------------+
| **GAUSS_LoadCompiledBuffer**    | Loads a compiled program from disk                |
+---------------------------------+---------------------------------------------------+

The following code illustrates a simple program that creates a random matrix and computes its inverse.

WorkspaceHandle_t *w1;

ProgramHandle_t *ph;

Int rv;

w1 = GAUSS_CreateWorkspace("Workspace 1");

ph = GAUSS_CompileString(w1,"x = rndu(10,10);xi = inv(x);",0,0);

rv = GAUSS_Execute(ph);

When this program is finished executing, the workspace will contain two global matrices. *x* is a 10×10 matrix of random numbers and *xi* is its inverse.

The following code retrieves *xi* from the workspace to the calling application.

Matrix_t *mat;

mat = GAUSS_GetMatrix(w1,"xi");

The following code copies the retrieved matrix to another workspace as *xinv*.

WorkspaceHandle_t *w2;

w2 = GAUSS_CreateWorkspace("Workspace 2");

rv = GAUSS_CopyMatrixToGlobal(w2, mat,"xinv");

The copy can also be done directly from one workspace to another.

WorkspaceHandle_t *w2;

w2 = GAUSS_CreateWorkspace("Workspace 2");

rv = GAUSS_CopyGlobal(w2,"xinv",w1,"xi");

GAUSS Engine Data Structures 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following data structures are used for moving data between the application and the **GAUSS Engine**. See **Chapter 12** for detailed information on the structures.

+--------------------------+-----------------------------------------+
| Array\ **\_**\ t         | N-dimensional array, real or complex    |
+==========================+=========================================+
| Matrix\ **\_**\ t        | 2-dimensional matrix, real or complex   |
+--------------------------+-----------------------------------------+
| String\ **\_**\ t        | character string                        |
+--------------------------+-----------------------------------------+
| StringArray\ **\_**\ t   | string array                            |
+--------------------------+-----------------------------------------+
| StringElement\ **\_**\ t | string array element                    |
+--------------------------+-----------------------------------------+

API calls to create and free this data. You can create copies of the data or aliases to the data.

If you have a lot of data, you will want to minimize the amount of memory used and the number of times a block of data is copied from one location in memory to another.

Use **GAUSS_Matrix** to create a **Matrix_t** structure. The following code creates a copy of the matrix *x*.

WorkspaceHandle_t *w1;

Matrix_t *mat;

double x[100][20];

w1 = GAUSS_CreateWorkspace("Workspace 1");

mat = GAUSS_Matrix(w1, 100, 20, x);

The call to **GAUSS_Matrix** calls **malloc** once for the **Matrix_t** structure and once for the matrix data. It then copies the matrix into the newly allocated block.

The following code creates an alias for the matrix *x*.

Matrix_t *matalias;

Matalias = GAUSS_MatrixAlias(w1, 100, 20, x );

The call to **GAUSS_MatrixAlias** calls **malloc** only once for the **Matrix_t** structure. It then sets the data pointer in the **Matrix_t** structure to the address of *x*. No copy is necessary.

The following code frees both *mat* and *matalias*.

GAUSS_FreeMatrix( mat );

GAUSS_FreeMatrix( matalias );

The first call above frees both the data block (which is a **malloc**\ ‘d copy of *x*) and the **Matrix_t** structure for *mat*. The second call frees only the **Matrix_t** structure for *matalias* because that **Matrix_t** structure contained only an alias to data that the user is left responsible for freeing if necessary.

Memory Ownership Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every **Matrix_t** structure contains a ``freeable`` flag that determines whether the data block is freed when **GAUSS_FreeMatrix** is called. The following table summarizes who owns the data after each API call:

+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| Pattern                                  | Data owned by      | Shell struct owned by | Caller action after                   |
+==========================================+====================+=======================+=======================================+
| ``GAUSS_Matrix`` + ``FreeMatrix``        | Engine (copy)      | Engine                | Call ``FreeMatrix`` when done         |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| ``GAUSS_MatrixAlias`` + ``FreeMatrix``   | **Caller** (alias) | Engine                | Call ``FreeMatrix`` (frees shell      |
|                                          |                    |                       | only). Keep your data pointer alive.  |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| ``GAUSS_Matrix`` +                       | Engine             | Freed inside Move     | **Do NOT call FreeMatrix** -- the     |
| ``MoveMatrixToGlobal``                   | (transferred)      |                       | shell is already freed by the move.   |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| ``GAUSS_Matrix`` +                       | Caller (original)  | Caller                | Call ``FreeMatrix`` to free your copy |
| ``CopyMatrixToGlobal``                   | + Engine (copy)    |                       |                                       |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| ``GAUSS_GetMatrix``                      | Caller (copy)      | Caller                | Call ``FreeMatrix`` when done         |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| ``GAUSS_GetMatrixAndClear``              | Caller (zero-copy) | Caller                | Call ``FreeMatrix`` when done.        |
|                                          |                    |                       | Engine variable is reset to 1x1.      |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+
| ``GAUSS_AssignFreeableMatrix``           | **Engine takes     | N/A (no shell)        | **Do NOT free the pointer** -- the    |
|                                          | ownership**        |                       | engine will free it.                  |
+------------------------------------------+--------------------+-----------------------+---------------------------------------+

.. warning::

   **Do not call GAUSS_FreeMatrix after GAUSS_MoveMatrixToGlobal.** The Move function frees the ``Matrix_t`` shell internally. Calling ``FreeMatrix`` afterward is a double-free that will crash your application.

   **Do not free memory passed to GAUSS_AssignFreeableMatrix.** After this call, the engine owns the data block and will free it when the variable is reassigned or the workspace is destroyed.

Copying and Moving Data to a Workspace 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the **GAUSS Engine** API calls to pass the data between a **GAUSS Engine** workspace and your application. There are two versions of many of these API calls. One makes a copy of the data (**malloc**\ ’s a new data block) and the other moves the data (gives the data pointer away without any calls to **malloc** and frees the original structure). The functions are named accordingly.

The following code uses **GAUSS_CopyMatrixToGlobal** to copy a matrix to the **GAUSS Engine**. The matrix will be called *xm* in the workspace.

WorkspaceHandle_t *w1;

Matrix_t *mat;

double x[100][20];

int rv;

w1 = GAUSS_CreateWorkspace( "Workspace 1" );

mat = GAUSS_Matrix( w1, 100, 20, x );

rv = GAUSS_CopyMatrixToGlobal( w1, mat, "xm" );

The following code uses **GAUSS_MoveMatrixToGlobal** to move a matrix to the **GAUSS Engine** and free the **Matrix_t**

structure. The matrix will be called *xm* in the workspace. The original **malloc**\ ’d block held by the double pointer *x* is left intact.

WorkspaceHandle_t *w1;

Matrix_t *mat;

double *x;

int r, c;

int rv;

r = 1000;

c = 10;

x = (double *) malloc( r*c*sizeof(double) );

memset( x, 0, r*c*sizeof(double) );

w1 = GAUSS_CreateWorkspace( "Workspace 1" );

mat = GAUSS_Matrix( w1, 100, 20, x );

rv = GAUSS_MoveMatrixToGlobal( w1, mat, "xm" );

This can also be accomplished with a nested call, eliminating the need for the intermediate structure. Again, the original **malloc**\ ’d block held by the double pointer *x* is left intact.

WorkspaceHandle_t *w1;

double *x;

int r, c;

int rv;

r = 1000;

c = 10;

x = (double *) malloc( r*c*sizeof(double) );

memset( x, 0, r*c*sizeof(double) );

w1 = GAUSS_CreateWorkspace("Workspace 1");

rv = GAUSS_MoveMatrixToGlobal( w1, GAUSS_Matrix( w1, r, c, x ), "xm" );

A very large **malloc**\ ’d matrix can be given to a workspace without any additional **malloc**\ ’s or copying with **GAUSS_AssignFreeableMatrix**. In the code below, a 1000000×100 real matrix is created and placed in a workspace.

WorkspaceHandle_t *w1;

double *x;

int r, c;

int rv;

r = 1000000;

c = 100;

x = (double *) malloc( r*c*sizeof(double) );

memset( x, 0, r*c*sizeof(double) );

w1 = GAUSS_CreateWorkspace( "Workspace 1" );

rv = GAUSS_AssignFreeableMatrix( w1, r, c, 0, x, "largex" );

After the call to **GAUSS_AssignFreeableMatrix**, the block of memory pointed to by the double pointer is owned by the **GAUSS Engine**. An attempt by the user to free it will cause a fatal error. The **GAUSS Engine** will free the block when necessary.

Getting Data From a Workspace 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code retrieves the matrix *xi* from the workspace to the calling application.

Matrix_t *mat;

mat = GAUSS_GetMatrix( w1, "xi" );

The following code checks the type of the symbol *xi* and retrieves it from the workspace to the calling application.

Array_t *arr;

Matrix_t *mat;

StringArray_t *sa;

String_t *st;

int type;

arr = NULL;

mat = NULL;

sa = NULL;

st = NULL;

type = GAUSS_GetSymbolType( w1, "xi" );

switch( type )

{

case GAUSS_ARRAY:

   arr = GAUSS_GetArray( w1, "xi" );

   break;

case GAUSS_MATRIX:

   mat = GAUSS_GetMatrix( w1, "xi" );

   break;

case GAUSS_STRING_ARRAY:

   sa = GAUSS_GetStringArray( w1, "xi" );

   break;

case GAUSS_STRING:

   st = GAUSS_GetString( w1, "xi" );

   break;

default:

   fprintf( stderr, "Invalid type (%d)\n", type);

   break;

}

Calling Procedures 
~~~~~~~~~~~~~~~~~~~~~~~~~

Two functions are provided to call **GAUSS** procedures, passing the arguments directly to the calling application and receiving the returns back directly, without the use of globals. Each requires an empty program handle. An empty program handle can be created with **GAUSS_CreateProgram**.

+---------------------------------+-----------------------------------------------------+
| GAUSS\ **\_**\ CallProc         | Calls a **GAUSS** procedure                         |
+=================================+=====================================================+
| GAUSS\ **\_**\ CallProcFreeArgs | Calls a **GAUSS** procedure and frees the arguments |
+---------------------------------+-----------------------------------------------------+

Shutdown
------------

When your application has completed using the **GAUSS Engine** you should call **GAUSS_Shutdown** before exiting the application.

It is possible to restart the **GAUSS Engine** by calling **GAUSS_Initialize** again after calling **GAUSS_Shutdown**.
