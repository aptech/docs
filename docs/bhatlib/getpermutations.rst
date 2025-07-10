getpermutations
==============================================

Purpose
----------------

Generates all permutations of a given vector.

Format
----------------
.. function:: perm = getPermutations(s)

    :param s: Vector of elements to be permuted.
    :type s: 1xK matrix

    :return perm: Matrix where each row represents a unique permutation of `s`.
    :rtype perm: NxK matrix, where N = K! (factorial of the number of elements in `s`)

Notes
----------------

- If `s` contains only one element, the function returns `s` itself.
- The function recursively generates all permutations by selecting each element as the first element and computing permutations of the remaining elements.

Source
----------------

getpermutations.src
