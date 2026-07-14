# Write GAUSS command-reference documentation

Use this workflow only for a user-requested GAUSS RST command-reference update
for a named function.

## Scope and verification

1. Identify the requested function and documentation target. Read the complete
   applicable `AGENTS.md` and `CLAUDE.md` instruction chain for gxmldoc and for
   every source repository consulted or changed.
2. Verify behavior from the implementation, declarations, tests, examples, and
   nearby command-reference pages. Do not infer unsupported formats or
   semantics.
3. Confirm every supported signature and overload; parameter types, shapes,
   optional values, and defaults; return values and structure members; errors,
   missing-value behavior, boundaries, and material side effects; and related
   functions or control constructors.

## Draft and integrate

1. Follow current gxmldoc RST structure and cross-reference conventions.
2. Include only verified formats, parameter and return details, working
   examples, relevant remarks, and `seealso` links.
3. Update an index, category page, or changelog only when the current
   documentation organization requires it. Preserve ordering and formatting.

## Validate and report

Run the narrowest available documentation build, link check, or targeted
validation. Report changed files, verified sources, commands, results, and any
unverified behavior.

Do not stage, commit, or publish unless the user separately asks.
