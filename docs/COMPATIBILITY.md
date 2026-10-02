# Compatibility notes

## Portable core

KZ-SKILLS uses a text-first directory format built around `SKILL.md`, YAML frontmatter, Markdown instructions, and optional companion files. The repository follows the public [Agent Skills specification](https://agentskills.io/specification) as its baseline.

## Compatibility is host-dependent

There is no blanket promise that every AI product can install or execute every skill. Hosts may differ in:

- Whether they discover skills automatically or require an import step.
- Which frontmatter fields they recognize.
- Whether they can read folders, attachments, scripts, or image assets.
- Whether they allow tool execution, network access, or persistent instructions.
- Context limits and how instructions are prioritized.

Use the host's current documentation for its supported workflow. When native support is absent, the manual copy/paste method in [Using Skills](USING-SKILLS.md) may work for text instructions, with reduced functionality.

## Compatibility metadata for future skills

Skill authors should document only requirements that matter, such as a specific host, local runtime, permission, or dependency. Do not list a product as supported merely because the skill is plain text. Platform-specific setup guides or adapters may be added later after they are tested and maintained.
