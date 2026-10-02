# Contributing to KZ-SKILLS

Thanks for helping make this library more useful. Contributions can add a skill, improve an existing one, fix documentation, or improve the validator.

## Before you open a pull request

1. Read [how to create a skill](docs/CREATING-SKILLS.md) and the [quality standards](docs/QUALITY-STANDARDS.md).
2. Check the category index to avoid duplicating an existing skill.
3. Keep the skill focused on one recognizable kind of task.
4. Include only resources that the instructions actually use. Document dependencies and permissions.
5. Run `python3 scripts/validate_skills.py` locally.
6. In the pull request, describe the intended user, when the skill should activate, and how you tested it.

## Proposing a new category

Open an issue or pull request explaining why existing categories do not fit. Prefer adding a skill to the closest category when that keeps discovery clear.

## Safety and quality

Do not include secrets, personal data, unlicensed content, or instructions that claim nonexistent tools or permissions. Security-related skills must be defensive and clearly scoped. See [SECURITY.md](SECURITY.md) for reporting a vulnerability.

## License status

The repository license has not yet been selected. Until a license is added, do not assume that contributions or files are available for unrestricted reuse. The project maintainer should resolve the license before accepting outside contributions for redistribution.
