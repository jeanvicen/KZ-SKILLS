# Creating a skill

A skill should be a compact, reusable playbook for a task an AI assistant can recognize. Start with a real workflow, not a broad topic label.

## 1. Choose a clear scope

Write one sentence: “Use this skill when the user needs to ___.” If the sentence combines unrelated outcomes, split the idea into smaller skills. A skill for “design” is too broad; a skill for “audit a mobile checkout flow for usability and accessibility” is easier to discover and test.

## 2. Create the folder

Choose the closest category and a lowercase, hyphen-separated name:

```text
skills/<category>/<skill-name>/SKILL.md
```

The `name` in the YAML frontmatter must match the skill directory name. Follow the [official specification](https://agentskills.io/specification) for exact metadata requirements.

## 3. Write the activation description

The `description` is a routing hint. Say what the skill does, when an assistant should use it, and include specific task words people may use. Avoid vague claims such as “helps with everything.”

## 4. Write actionable instructions

A useful `SKILL.md` usually covers:

- Purpose and activation conditions.
- Inputs to inspect and clarifying questions to ask only when needed.
- A numbered process with decision points.
- Quality checks, edge cases, and safe stopping conditions.
- A concise example of a good input and expected output.
- What the skill must not assume or claim.

Prefer direct verbs, observable checks, and explicit boundaries. Do not claim that the assistant has access to a tool, file, website, or permission unless the host actually provides it.

## 5. Keep details modular

Keep `SKILL.md` focused; move long reference material to `references/` and link to it with a relative path. Add scripts only when they materially improve the workflow, document dependencies, and provide helpful error messages. Use `assets/` for templates or diagrams the skill genuinely needs. Avoid deep chains of linked documents.

## 6. Test it

Try realistic prompts that should activate the skill and nearby prompts that should not. Check that the instructions are understandable without author context, that examples are labeled, and that optional files are referenced correctly. Run:

```bash
python3 scripts/validate_skills.py
```

The validator checks repository conventions only; test the skill with a human reviewer and the intended AI host as well.

## 7. Submit a focused pull request

Use the checklist in [CONTRIBUTING.md](../CONTRIBUTING.md). Include the skill's target user, intended activation situations, test prompts, known limitations, and any external dependencies.

## Starter

Copy [`templates/skill-template/`](../templates/skill-template/) into the appropriate category, then rename the folder and update its metadata and content.
