.. list-table::
   :widths: auto

   * - dOut.facsave1
     - Matrix, Nobs x numIterations, stores draws of factor one, one column for each iteration.
   * - dOut.facsavea
     - Array, NumFac2 x Nobs x numIterations, stores draws of second factors, stored on separate planes for each sub-group, with each iteration stored on separate columns.
   * - dOut.facsaveb
     - Matrix, NumFac2 x Nobs, stores means of the draws of second factors with each factor stored on a separate column.
   * - dOut.parms
     - Matrix, NumFac2 x Nobs, stores draws of the parameter vector, one column for each iteration.
   * - dOut.vdecom2
     - Array, 3 x numObs x numVars, stores variance decomposition from group factor, sub-group factors, and idiosyncratic error terms, in separate planes respectively.
   * - dOut.errTerms
     - Array, numVars x numInd x numObs x numIters, stores draws of error terms, stored on separate planes for each variable per each sub-group, with each iteration stored on separate columns.