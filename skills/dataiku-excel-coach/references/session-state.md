# Resumable coaching state

Maintain `coaching_state.json` beside the existing migration and validation plans in the selected process's migration working directory. Before that directory exists, use `excel_coaching/<workbook-stem>/` in the current writable workspace and record its location. Move the record into the migration directory once established.

Store operational memory, not a full transcript or duplicate migration plan. Do not store credentials, tokens, secrets from external connections, or full customer rows.

## Fields

Use valid JSON; unknown fields can be null:

- `version`: 2 for new records. Read version 1 records compatibly; leave new confirmations unknown until explicitly established. Do not infer a conceptual confirmation or initial instance choice from a generic legacy scope flag.
- `workbook`: resolved path, size, modification time, optionally a digest.
- `phase`: discovery, process_confirmation, planning, construction, walkthrough, validation, or handover.
- `candidate_processes`: names, sheet/range references, confirmation status.
- `selected_process`: confirmed goal, input boundaries, output grain, expected outputs, and a separate `conceptual_confirmation` with the confirmed business description.
- `target`: instance identifier/name/URL, `instance_selection_confirmed`, project key, grounded project URL, and separate project/plan confirmation. An active/default instance alone does not establish selection.
- `plans`: paths to migration, validation, and documentation plans.
- `pacing`: `build_then_walkthrough`, `guided_construction`, or `batched_construction`; user confirmation, approved plan IDs/batch scope, next-start choice, and any observed comparable duration evidence. Map legacy guided/grouped/automatic to behavior on resume and ask only where intent is unclear.
- `learner`: stated experience, concepts introduced, observed questions/understanding. Avoid speculative skill ratings.
- `lessons`: stable plan IDs, exact Excel ranges/formulas, dataset/recipe names, UI inspection targets, check coverage/results, evidence paths, build status, and separate learning status. Distinguish planned/executing/verified construction from pending/current/reviewed walkthrough. A numeric acknowledgement is evidence of a comparison, not proof of recipe understanding.
- `created_assets`: migration-created identifiers, distinguished from pre-existing assets.
- `cobuild`: project key, conversation ID, pending turn ID/status if any.
- `open_questions`: source ambiguity, blockers, unanswered learning prompts.
- `next_action`: exact remaining step or response awaited.

Update at checkpoints. Keep detailed evidence in migration artifacts and reference it. If persistence is unavailable, provide a compact resume note and disclose it has not been saved.

## Resume

1. Locate the matching record; ask which process if several apply.
2. Check workbook changes; re-inspect affected dependencies and contracts if changed.
3. Confirm active instance/project against the recorded explicit selection. If selection was never confirmed, ask now; re-confirm if the destination changes. Do not silently substitute a destination.
4. Read the live Flow, relevant assets, and jobs. Reconcile user edits and missing objects.
5. Recover pending Cobuild operations through Headless's guide. Do not resend a lost response's mutation. If retained conversations disappeared, inspect actual assets before starting a replacement for remaining work.
6. Show the compact plan with separate build/learning progress and the next workbook/recipe operation. Return to an unanswered checkpoint unless the current message answers it or changes pacing. Continue only within approved construction scope; a completed build resumes the walkthrough without rebuilding it.
