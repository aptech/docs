.. list-table::
   :widths: auto

   * - svarCtl0.numVar
     - Scalar, number of independent variables in the system.
   * - svarCtl0.T0
     - Scalar, observations number of initial time.
   * - svarCtl0.numIRF
     - Scalar, number of impulse responses.
   * - svarCtl0.numirfSR
     - Scalar, number of sign restrictions on impulse response functions.
   * - svarCtl0.signRestrictions
     - Matrix, vector indicating sign restrictions on structural parameter coefficients. [0 = no restriction, 1 = response >= 0, -1 = response <= 0]. Violation of sign restriction: irf*restriction < bound.
   * - svarCtl0.printOut
     - Scalar, indicator variable to print results to screen. [0 = no print out or 1 = print out].
   * - svarCtl0.numObsScale
     - Scalar, creates a multiple of the sample size; nobsscale _> 100 indicates fixed OLS values.
   * - svarCtl0.numBlocks
     - Scalar, number of simulation blocks.
   * - svarCtl0.numSimulations
     - Scalar, number of iterations in each simulation.
   * - svarCtl0.numSimulationTot
     - Scalar, total number of simulation iterations.

