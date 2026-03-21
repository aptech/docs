Sample Programs
===============

At least five sample programs are provided in the **GAUSS Engine** installation directory: **eng2d.c, mtexpr.c, mtcall.c, grte01.c,** and **grte02.c.**

The examples that start with **grte** will run with the **GAUSS Engine**. The makefile is set to link these examples with the **GAUSS**

**Run-Time Engine (GRTE)**. You will need to modify the makefile to link them with the **GAUSS Engine**. See the source code for these examples for further instructions.

Linux/macOS 
----------------

The **GAUSS Engine** is shipped with several sample C programs that incorporate the **GAUSS Engine**, and a Makefile for building them.

For 32-bit compilation on a 64-bit machine, ensure the Makefile contains the **CCOPTIONS=-m32** line.

Go to the directory you installed the **GAUSS Engine** to such as mteng26.

cd /usr/local/mteng26

Sample Program **eng2d**: 
^^^^^^^^^^^^^^^^^^^^^^^^^^

Run make to build **eng2d**

make eng2d

**eng2d** sets some global variables, runs a program that uses them, then extracts the result from the workspace. Try running it.

./eng2d

You can see that the computation printed out by the **GAUSS** program and the data extracted by **GAUSS_GetMatrix**

are the same.


Windows 
------------

The **GAUSS Engine** is shipped with several sample C programs that incorporate the **GAUSS Engine**, and a Makefile

for building them. (Note: The Makefile is written for Microsoft Visual Studio 2019. If you are using a different compiler, you will have to manually compile the sample programs.)

For 32-bit compilation on a 64-bit machine, ensure the Makefile contains the **CCOPTIONS=-m32** line.

Open a Command window and go to the directory you installed the **GAUSS Engine** to. We’ll assume **c:\\mteng26**

cd c:\\mteng26


Sample Program **eng2d**: 
^^^^^^^^^^^^^^^^^^^^^^^^^^

Run **nmake** to build **eng2d**.

nmake eng2d

**eng2d** sets some global variables, runs a program that uses them, then extracts the result from the workspace. Try running it.

eng2d

You can see that the computation printed out by the **GAUSS** program and the data extracted by **GAUSS_GetMatrix** are the same.

Visual Studio Example **msvc_example**: 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Change your current working directory to c:\\mteng26\\msvc_example and either open gauss_eng2d.sln with Visual Studio 2019 or build it from the command line:

devenv.exe gauss_eng2d.sln /build “Release|x64”

Note that if you are compiling for the 32-bit version of the GAUSS Engine you must change the ‘x64’ reference to ‘Win32’ (eg “Release|Win32”). After successfully compiling and linking, the new binary gauss_eng2d.exe should be located in your c:\\mteng26 directory.

See the Makefile for other targets; there may have been additions after the manual was printed.

Building With CMake
-----------------------

A **CMakeLists.txt** file is also available in the **GAUSS Engine** installation directory. To build the examples, CMake must be installed and able to be found in the PATH environment variable.

1. Ensure the ‘rlm’ (rlm.exe on Windows) binary is running in the installation directory. This step is required for the grte01/grte02 programs to compile correctly. A temporary license is sufficient for the **mtcall**, **mtexpr** and **eng2d** examples but **grte01** and **grte02** require a full license with a **g.gkf** file present in the same directory to correctly run.

2. Create the build directory: **mkdir build**

3. Change to the build directory: **cd build**

4. Run cmake with the appropriate values (Release can be substituted with ‘Debug’). The –G flag for CMake will specify the generator for creating the project. Command-line building is easiest with “NMake Makefiles” on Windows and “Unix Makefiles” on Linux/macOS. Omitting the –G flag will use the system default generator (ie Visual Studio Solution on Windows and Xcode project on macOS).

   a. **cmake –G”NMake Makefiles” –DCMAKE_BUILD_TYPE=Release ..**

..

   OR

b. **cmake –G”Visual Studio 14 Win64”**

..

   Or for a 32-bit build, specify the –m32 flag

c. **cmake –G”NMake Makefiles” –DCMAKE_BUILD_TYPE=Release –DCMAKE_C_FLAGS=-m32 ..**

..

   OR

d. **cmake –G”Visual Studio 14”**

5. Build the examples

   a. **make install** (Linux/macOS)

..

   OR

b. **nmake install** (Windows)

..

   OR

c. **cmake --build . --config Release --target install** (Either)

Change back to the installation directory and execute the newly built binaries.
