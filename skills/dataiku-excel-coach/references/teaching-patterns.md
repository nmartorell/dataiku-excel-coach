# Teaching patterns

Ground every lesson in actual workbook evidence and read-back Dataiku settings. Examples below use the fleet trial to illustrate the pattern; never assume these names or addresses apply to another workbook.

## Conceptual confirmation before implementation

“Your fleet process starts with monthly aircraft counts and annual flying hours/cycles. It averages the monthly counts, combines the fleets specified by the workbook, and calculates stage length, daily utilization, and year-over-year changes. We will reproduce the main B767 budget figures and leave maintenance costs out of scope. Is that the process you want to reproduce?”

Include actual source references and consequential conventions. Ask even if inspection found no ambiguity. Keep this checkpoint in business/Excel language; propose Dataiku objects only after confirmation.

## A recipe-centered lesson

Show the stable plan and current position, for example:

| Step | Operation | Build | Learning |
| --- | --- | --- | --- |
| 1 | Read original inputs | Verified | Reviewed |
| 2 | Reshape months and combine years | Verified | Reviewed |
| 3 | Calculate annual fleet averages | Verified | Current |
| 4 | Connect flying statistics and calculate comparisons | Verified | Next |
| 5 | Validate, document, and rebuild | Verified | Pending |

These statuses illustrate a completed build with a partially completed walkthrough. Use actual status, not this example's assumed completion.

“Step 3 turns monthly records into annual averages. In `Fleet plan 2025!O5`, `=AVERAGE(C5:N5)` averages the twelve A319/AC month counts. `O31` uses `=IFERROR(AVERAGE(C31:N31),0)` for the prior year. In Dataiku, `average_fleet_by_year` groups by year, aircraft variant, and operator, and averages `aircraft_count`. This changes one row from a month into an annual aircraft/operator result. A following Prepare handles the report's population and zero conventions.”

Provide the verified project/object link, then concise UI indications: “Open `average_fleet_by_year` from the Flow and inspect its grouping keys and average aggregation. To create this operation yourself, start from `fleet_monthly` in the Flow, choose a Group recipe, select those keys, and add an average of `aircraft_count`.” Adapt exact UI labels to known version/settings; avoid claiming visual inspection without it.

“I verified all 34 annual report rows against Excel. In `fleet_annual`, filter A319/AC and compare 2025's 1.9167 with `Fleet plan 2025!O5`, and 2024's 4.9167 with `O31`. These displayed values are rounded; the calculation uses full precision.”

Then invite one meaningful action: “Inspect the grouping keys. Keeping operator as a key preserves AC and Rouge separately; combining operators would require a different aggregation rule. Would you like to discuss that or move to step 4?” Do not imply averaging all monthly rows is automatically the correct way to combine fleet counts.

The agent's independent validation establishes correctness. The learner comparison connects a familiar spreadsheet result to the transformation. Use “I verified …; inspect … to see how …” rather than repetitive “Do the numbers match?” If evidence is sampled, say so.

## Preview and continuation

At a guided-construction checkpoint:

“Next is step 4: the cross-sheet references and comparison formulas in `Stats 2025 vs 2024!G3:U13`. We will create the family fleet totals, calculate the hours-share denominator, and join the flying statistics to calculate stage length and utilization. This involves several verified units and can take several minutes; I do not have a reliable finish time for this unit. Shall I start step 4, batch steps 4–5, or complete the remaining construction and then walk you through it?”

Use current plan IDs, dependencies, remaining work, and actual timing evidence. This is a learning/continuation choice, not a tool-permission request. Ask before starting unless that scope was already approved. Do not bury pacing offers in progress commentary: put them at the checkpoint where the user can choose.

At a completed-flow checkpoint, the next step is inspection, not construction: “Step 4 is already built and verified. Next we can inspect the Join keys and utilization formula, combine the remaining familiar lessons, or pause here.” Do not quote construction time as walkthrough time.

## Pacing and latency

- Build then walkthrough: agree on scope/mode, construct in verified units, then pause between short lessons on the completed Flow.
- Guided construction: explain/preview, wait for the start choice, construct the authorized step, then inspect and choose the next action.
- Batched construction: agree on explicit step IDs, verify dependent units, then teach the batch in manageable segments.

Offer mode/batch choices with the initial plan and again after the first guided checkpoint. Repeat when the workload changes or the user requests faster pacing. Retain the current choice otherwise.

When evidence permits a duration estimate, use an approximate range, name its basis, and explain uncertainty from setup/corrections. If no comparable history exists, state that construction may take several minutes and no dependable estimate is available. “You can step away while this run continues” is different from promising work after the session stops. Keep polling and progress communication within harness constraints.

## Vocabulary bridges and practice

| Excel operation | Likely Dataiku concept | Inspect or explain |
| --- | --- | --- |
| Source table/range | Dataset | Selected sheet, schema, row meaning |
| Formula copied down | Prepare formula | Expression, types, blanks |
| Lookup | Join | Keys, uniqueness, unmatched rows |
| Pivot summary | Group or Pivot | Grouping keys and grain |
| Append similar tables | Stack | Column alignment, origin |
| Month columns | Fold in Prepare | Folded columns, month/count outputs |
| Refresh sequence | Flow/build | Dependencies and execution |

These are candidates. Follow installed guides and preserve lookup/order, rounding, date, and null semantics. Alternate inspection with small prediction/explanation tasks; later offer an agreed edit or a comparable new example. Identify the asset, inspect the learner's result, and give feedback. Support can decrease as understanding is demonstrated. Avoid turning every checkpoint into a quiz or forcing an exercise before continuing.
