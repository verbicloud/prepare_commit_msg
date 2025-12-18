from pathlib import Path
import sys


INSTRUCTION = """
# Version Bump Triggers:
#   - fix: Bug fixes (patch version bump)
#   - feat: New features (minor version bump)
#   - perf: Performance improvements (patch version bump by default)
#
# No Version Bump:
#   - docs: Documentation only changes
#   - style: Code style changes (formatting, missing semicolons, etc.)
#   - refactor: Code refactoring without fixing bugs or adding features
#   - test: Adding or updating tests
#   - build: Changes to build system or dependencies
#   - ci: CI/CD changes
#   - chore: Other changes that don't modify src or test files
#   - revert: Reverting previous commits
#
"""


def main():
    commit_msg_filepath = Path(sys.argv[1])
    message = commit_msg_filepath.read_text()
    commit_msg_filepath.write_text(f"{message}{INSTRUCTION.strip()}")
    

if __name__ == "__main__":
    main()
