Interrupts
==========

To interrupt **GAUSS** programs, there are the following functions:

+-------------------------------+------------------------------------------------------------+
| GAUSS_SetGlobalInterrupt      | Interrupt all programs.                                    |
+===============================+============================================================+
| GAUSS_SetProgramInterrupt     | Interrupt all programs using a specified program handle.   |
+-------------------------------+------------------------------------------------------------+
| GAUSS_SetWorkspaceInterrupt   | Interrupt all programs using a specified workspace handle. |
+-------------------------------+------------------------------------------------------------+

To clear the interrupts use:

+--------------------------------+--------------------------------+
| GAUSS_ClearGlobalInterrupt     |                                |
+================================+================================+
| GAUSS_ClearProgramInterrupt    |                                |
+--------------------------------+--------------------------------+
| GAUSS_ClearWorkspaceInterrupt  |                                |
+--------------------------------+--------------------------------+

A global interrupt must be explicitly cleared or no subsequent programs will run. If the program and workspace interrupts are not cleared, the associated handles will be disabled for subsequent programs. Also, all programs in all threads will run slightly slower when interrupts are pending. Clearing the interrupt requests will allow any simultaneously running threads to run at full speed,

so it is good practice even if the associated handles will not be reused.
