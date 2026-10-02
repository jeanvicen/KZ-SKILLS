# Repository architecture

## Goals

- Keep skills discoverable by task and domain.
- Use a portable, text-first skill format with optional supporting resources.
- Separate user-facing library content from authoring guidance and repository tooling.
- Allow categories and platform adapters to grow without reorganizing existing skills.
- Make the initial repository useful before the first skill is published.

## Top-level map

```text
.
├── README.md                     # English landing page and quick start
├── CONTRIBUTING.md               # Contribution workflow
├── SECURITY.md                   # Responsible security reporting
├── assets/                       # Original README illustrations
├── docs/                         # Architecture, authoring, compatibility, quality, roadmap
├── skills/                       # Published skills, grouped by category
├── templates/skill-template/     # Copyable authoring starter
├── scripts/                      # Local validation utilities
└── .github/workflows/             # Automated checks
```

A published skill belongs at `skills/<category>/<skill-name>/`. The skill directory contains `SKILL.md` and may contain `references/`, `scripts/`, or `assets/` when useful.

## Skill discovery

Category README files are the human-readable indexes. A machine-readable catalog can be added once there are enough real skills to maintain it reliably. Until then, avoid a generated or hand-maintained catalog that merely repeats an empty directory tree.

## Authoring model

The format follows the [Agent Skills specification](https://agentskills.io/specification): a skill is a directory with a `SKILL.md` containing YAML frontmatter and Markdown instructions. The repository validator enforces a practical subset of naming and file-layout rules; it does not replace a full YAML parser, security review, or editorial review.

## Compatibility model

The source of truth is the portable skill directory. Platform-specific installation steps belong in documentation or future adapters, not duplicated in every skill. See [compatibility notes](COMPATIBILITY.md).

## Decisions intentionally left open

- Repository and contribution license.
- Whether to add platform-specific packaging or install tooling.
- Whether a catalog should be generated from validated skill metadata.

These choices should be made when actual skills and contributor needs provide evidence.
