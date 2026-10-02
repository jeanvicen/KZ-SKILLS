# Skill quality standards

Use this checklist before publishing a skill.

## Discoverability

- [ ] The skill name is specific, lowercase, hyphen-separated, and matches its directory.
- [ ] The description explains both what the skill does and when it should activate.
- [ ] The skill lives in the closest existing category.

## Useful instructions

- [ ] The scope is focused and the workflow is actionable.
- [ ] Inputs, decision points, output expectations, and important edge cases are clear.
- [ ] Examples are realistic and labeled as examples.
- [ ] Long details are moved to focused references; paths are relative to the skill folder.
- [ ] The main instructions avoid needless repetition and are reasonably concise.

## Honesty and safety

- [ ] The skill does not claim tools, permissions, access, or certainty the host may not have.
- [ ] Any external side effect, sensitive data, or high-impact decision is clearly bounded.
- [ ] Scripts disclose dependencies and handle errors safely.
- [ ] Security instructions are defensive and restricted to authorized environments.
- [ ] External resources and examples can be used lawfully and do not expose private information.

## Validation and maintenance

- [ ] `python3 scripts/validate_skills.py` passes.
- [ ] A reviewer has tried at least one in-scope and one nearby out-of-scope prompt.
- [ ] Known host requirements and limitations are documented.
- [ ] The skill has an owner or a clear plan for keeping time-sensitive guidance current.
