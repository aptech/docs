Multi-threaded Applications
===========================

The **GAUSS Engine** can be used in multi-threaded applications. To achieve the maximum amount of concurrency, you need to structure your application correctly.

The setup and initialization functions should be called from the main thread once at the beginning of the application. The functions that create the matrix, string and string array structures have no associated threading issues. The functions that compile, execute and move data between the application and the **GAUSS Engine** are discussed below.

If each thread is using a different workspace, there are no associated concurrency issues. The **GAUSS Engine** API is thread-safe across different workspaces for all functions as long as each workspace has only one associated thread. **GAUSS_CopyGlobal**

will read lock the source workspace and write lock the target workspace as it copies.

There are rules that you can follow to achieve nearly 100% concurrency for multiple threads in a single workspace. Those rules are also discussed below.

Locks 
----------

A workspace can have multiple read locks or one write lock. If a thread has a write lock on a workspace, all other threads are blocked until the thread releases the write lock. If a workspace is read locked by one or more threads, any threads requesting write locks are blocked until all the read locks are released.

Two flags are used with the compile functions to guarantee that the program compiled is thread-safe. These are **readonlyC** and **readonlyE** for “\ *read only* compile” and *“read only execute,”* respectively. They control workspace locking for compiling and execution of **GAUSS** code and are used during compiles to trap for code that is not thread-safe. The value of **readonlyE** is passed to the execute functions, via the program handle.

Be aware that this information is not kept across multiple compiles in the same workspace. Only the values from the compile that created the program handle are passed to the executer. It is therefore possible to make multiple compiles in a workspace and do a *read only* compile that succeeds erroneously. The reason for this is that procedures that assign to globals may be resident in the workspace from a previous compile and will not get recompiled each time. If an already resident procedure that assigns to globals is called in a subsequent compile, the global assignment will not be detected.

In practice, this does not usually matter. These arguments are to be used as an aid during development to verify that your code is or is not assigning to globals. They will not prevent you from creating code that is not thread-safe. When your compile fails it shows you the line of code that violated the rules you specified with the arguments.

Compiling and Executing GAUSS Programs 
-------------------------------------------

**GAUSS_CompileFile, GAUSS_CompileString** **and GAUSS_CompileExpression** read lock the workspace when the **readonlyC** argument is true (non-zero) and write lock the workspace when it is false. When **readonlyC** is true, the compile will fail if it tries to create or redefine any globals, including procedure definitions. When the **readonlyE** argument is true, the compile will fail if the program assigns to any globals. The value of **readonlyE** is passed to the executer, via the program handle.

**GAUSS_Execute** and **GAUSS_ExecuteExpression** read lock the workspace if the program was compiled with the **readonlyE** argument set to true and write lock the workspace otherwise.

Assuring Concurrency 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To assure concurrent compilation and execution of multiple threads in a single workspace, design your code so it can be compiled with **readonlyC** and **readonlyE** both true for any compiles and executes that you intend to run concurrently in the same workspace.

In practice this usually means you have an initialization cycle (compile and execute) with both flags false to compile and execute the code necessary to define and initialize any global data for a workspace. You then have a second initialization cycle (compile only) with **readonlyE** true to compile the procedures you need. This data and these procedures can then be used in a thread-safe

fashion (both flags true) in subsequent compiles and executes in the same workspace.

Calling GAUSS Procedures 
-----------------------------

The functions **GAUSS_CallProc** and **GAUSS_CallProcFreeArgs** provide a way to call **GAUSS** procedures with no globals used for either the arguments or the returns of the procedure. Arguments are passed directly from the application to the procedure via a C structure array and the returns are handled the same way. No globals are necessary in the workspace.

The program handle used with these functions can be created with **GAUSS_CompileFile**, **GAUSS_CompileString** or **GAUSS_CreateProgram**. If the program handle is created with **readonlyE** true, then **GAUSS_CallProc** and **GAUSS_CallProcFreeArgs** *read lock* the workspace, otherwise they use a *write lock*.


Assuring Concurrency 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To assure concurrent execution of multiple threads in a single workspace, design your procedures so they can be compiled with **readonlyE** true. Assuming a procedure that is listed in a library, the following code illustrates this:

ProgramHandle_t *ph;

char cmd[100];

int readonlyC, readonlyE;

strcpy( cmd, "library mylib; external proc proc1, proc2;" );

readonlyC = 0;

readonlyE = 1;

ph = GAUSS_CompileString( wh, cmd, readonlyC, readonlyE );

If this compile succeeds, you can call the procedures multiple times simultaneously in separate threads and they will execute concurrently. The compile will fail if the procedures contain code that assigns to global variables.
