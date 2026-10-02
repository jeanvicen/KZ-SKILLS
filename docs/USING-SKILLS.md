# Using KZ-SKILLS

A skill is a set of instructions and optional supporting files. The exact way to load it depends on the AI product.

## Option A: Native skill support

If the assistant documents support for Agent Skills or compatible skill folders:

1. Follow that product's official import or installation instructions.
2. Add the complete skill folder when supported, not just its frontmatter.
3. Confirm the host can access any referenced resource or script.
4. Ask for a task that matches the skill's description.

Do not assume that a command or installation path for one product works in another.

## Option B: Manual text-based use

For an AI that can follow pasted instructions but has no skill manager:

1. Open the desired `SKILL.md` in this repository.
2. Copy its full contents into the conversation or the product's custom instructions.
3. If it references companion files, attach or paste the relevant ones when the product supports that.
4. State the concrete task and provide the context needed to do it.
5. Review the answer and verify important facts or actions.

Example prompt:

> Follow the instructions below as a task guide. Use them for this request, be clear about any missing inputs or tools, and do not claim you performed actions you could not perform. [Paste the skill.] Now help me with: [your task and context].

This is a manual fallback, not a guarantee that every AI product supports persistent instructions, attachments, code execution, or the same context size.

## What a skill can and cannot do

A skill can describe a process, provide checklists, and supply reusable references. By itself, it cannot install software, grant account access, authorize external actions, or create tools that the host does not have. Treat generated output as work to review, especially for high-impact decisions.
