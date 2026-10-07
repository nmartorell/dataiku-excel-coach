# Pacing rationale and pilot evidence

Read when explaining the design or choosing pacing for a substantial process. Research informs lesson structure; it does not directly establish the best execution mode for Dataiku/Codex migrations.

## Observed pilot

Source: user-provided session `rollout-2026-10-06T16-03-22-01a112d0-4847-7cf1-855f-a34a43508418.jsonl`, 6 October 2026. UTC timestamps:

| Unit | User reply/start anchor | Completed checkpoint | Elapsed |
| --- | --- | --- | --- |
| Source ingestion | 20:12:22 | 20:19:43 | 7.35 minutes |
| Monthly reshape/Stack | 20:28:22 | 20:39:21 | 10.97 minutes |
| Annual averages/report rules | 20:40:14 | 20:45:33 | 5.31 minutes |

These are wall-clock intervals after learner replies, including orchestration, construction, and verification. They do not isolate MCP approval time, backend processing, or effective learning time. They are observations from one workbook, not general estimates.

The initial response reported the active instance without first requesting instance choice. After process selection, a migration plan appeared before a separate conceptual confirmation. The implementation plan/project proposal worked well according to learner feedback. Three completed learning checkpoints asked only for number matches; replies were “It does,” “I do,” and “yes.” There were useful concept explanations in commentary, but no explicit faster-pacing offer, concise ongoing plan status, or recipe-centered walkthrough at those checkpoints. The fourth unit was still being corrected when the learner requested the log; do not count that log response as completion of the unit.

These observations support separating construction waits from instructional turns. They do not prove the learner failed to learn or that permissions caused the delay.

## Research informing lesson design

[Atkinson, Renkl, and Merrill (2003), Transitioning From Studying Examples to Solving Problems](https://doi.org/10.1037/0022-0663.95.4.774), experiments on probability tasks, found benefits from combining prompts about underlying principles with gradually removed worked solution steps. This supports using a verified Flow as a worked example, prompting explanation of recipe choices, and adding small learner tasks as support decreases. It does not establish that agent construction should happen live. [Full paper](https://mrbartonmaths.com/resourcesnew/8.%20Research/Making%20the%20most%20of%20examples/Fading%20out%20and%20Prompts.pdf).

[Tabbers and de Koeijer (2010), Learner control in animated multimedia instructions](https://link.springer.com/article/10.1007/s11251-009-9119-4), found better transfer with learner-paced presentation alongside increased time on task and substantial individual variation. This supports learner control over lesson progression while cautioning against assuming every pause improves efficiency. Its multimedia setting differs from inspecting a Dataiku Flow.

## Design inference

Recommend building the confirmed process first when substantial construction is expected, then offer a segmented walkthrough with recipe inspection, exact Excel comparisons, and progressively independent practice. Retain guided/batched construction for learners who prefer watching the build. Full construction can still take time; batching primarily reduces repeated waiting/checkpoint cycles and does not guarantee less backend work. Test learning separately from construction speed: can the learner explain a key, choose an aggregation, or repeat a comparable operation?
