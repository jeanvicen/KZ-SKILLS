---
name: replace-with-skill-name
description: Describe what this skill does, when an assistant should use it, and the concrete task terms that should activate it.
---

# Skill title

## Purpose

Explain the specific outcome this skill helps produce.

## When to use this skill

Use it when the user asks for:
- A clear, in-scope task.
- A second recognizable task in the same workflow.

Do not use it for unrelated requests or claim access to tools the host does not provide.

## Workflow

1. Inspect the user's request and available context.
2. Identify missing information; ask only for details that change the result.
3. Perform the task using available tools and follow applicable safety constraints.
4. Check the result against the quality criteria below.
5. State limitations and what remains for the user to decide.

## Output

Describe the expected deliverable, format, and level of detail.

## Quality checks

- Verify facts, paths, and assumptions that matter.
- Label examples or estimates clearly.
- Do not claim actions that were not performed.

## Edge cases

Describe how to handle ambiguity, unavailable tools, sensitive information, or failed checks.

## Examples

### In-scope request

> Add a concise example that should activate this skill.

### Out-of-scope request

> Add a nearby example that should not activate this skill.
