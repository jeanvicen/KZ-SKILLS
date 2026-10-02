#!/usr/bin/env python3
"""Lightweight repository checks for published KZ-SKILLS directories."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, "SKILL.md must begin with YAML frontmatter delimited by ---"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "YAML frontmatter is not closed with ---"
    values = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            value = match.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            values[match.group(1)] = value
    body = parts[2].strip()
    return (values, body), None


def main() -> int:
    errors = []
    if not SKILLS.exists():
        print("ERROR: skills/ directory is missing")
        return 1

    skill_files = sorted(SKILLS.rglob("SKILL.md"))
    for skill_file in skill_files:
        skill_dir = skill_file.parent
        relative = skill_file.relative_to(ROOT)
        parsed, error = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
        if error:
            errors.append(f"{relative}: {error}")
            continue
        metadata, body = parsed
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not name:
            errors.append(f"{relative}: missing required name")
        elif len(name) > 64 or not NAME_RE.fullmatch(name):
            errors.append(f"{relative}: name must be lowercase letters, digits, and single hyphens (max 64 chars)")
        elif name != skill_dir.name:
            errors.append(f"{relative}: name '{name}' must match directory '{skill_dir.name}'")
        if not description:
            errors.append(f"{relative}: missing required description")
        elif len(description) > 1024:
            errors.append(f"{relative}: description exceeds 1024 characters")
        if not body:
            errors.append(f"{relative}: Markdown instructions after frontmatter are empty")
        if len(skill_file.read_text(encoding="utf-8").splitlines()) > 500:
            errors.append(f"{relative}: keep SKILL.md at or below 500 lines; move detail to references/")
        for link in re.findall(r"\]\(([^)]+)\)", skill_file.read_text(encoding="utf-8")):
            if not link.startswith(("http://", "https://", "#")):
                target = (skill_dir / link.split("#", 1)[0]).resolve()
                if not target.exists():
                    errors.append(f"{relative}: referenced local path does not exist: {link}")

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed ({len(skill_files)} published skill(s) checked).")
    if not skill_files:
        print("No skills are published yet; the scaffold is ready for its first skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
